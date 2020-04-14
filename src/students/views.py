from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from students.models import Student, Logger
from students.forms import StudentsAddForm, ContactForm, UserRegistrationForm, UserLoginForm
from students.tasks import send_confirmation_mail
from students.tokens import account_activation_token
from django.conf import settings


def generate_student(request):
    student = Student.generate_student()
    return HttpResponse(f'{student.get_info()}')


def students(request):
    queryset = Student.objects.all().select_related('group')

    fn = request.GET.get('first_name')
    if fn:
        queryset = queryset.filter(first_name__istartswith=fn)

    return render(request,
                  'students_list.html',
                  context={'students': queryset})


def students_add(request):
    if request.method == 'POST':
        form = StudentsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentsAddForm()

    return render(request,
                  'students_add.html',
                  context={'form': form})


def students_edit(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return HttpResponseNotFound(f'Student with id {pk} not found')

    if request.method == 'POST':
        form = StudentsAddForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentsAddForm(instance=student)

    return render(request,
                  'students_edit.html',
                  context={'form': form, 'pk': pk})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('contact'))
    else:
        form = ContactForm()
    return render(request,
                  'contact.html',
                  context={'form': form})


def register(request):
    user_form = UserRegistrationForm

    if request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            recipient_list = [settings.EMAIL_HOST_USER, ]
            send_confirmation_mail(mail_subject,message,to_email,recipient_list)
            return HttpResponseRedirect('Please confirm your email address to complete the registration',
                                        reverse('contact'))
    else:
        form = user_form()
    return render(request,
                  'registration.html',
                  context={'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def custom_login(request):
    user_form = UserLoginForm

    if request.GET.get('logout'):
        logout(request)
    if request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            user = authenticate(request,
                                username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            login(request, user)

            return HttpResponseRedirect(reverse('contact'))
    else:
        form = user_form()
    return render(request,
                  'login.html',
                  context={'form': form})
