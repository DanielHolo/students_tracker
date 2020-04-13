import time
from django.contrib.auth.models import User

from students.models import Logger

from students import model_choices as mch


class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        last_user = 'adminadmin@a.com'  # не разобрался как из входа в админку вытянуть username
        user_id = list(User.objects.filter(username=last_user).values_list('id', flat=True))

        diff = time.time() - start_time

        admin_url = '/admin/'
        if request.path.startswith(admin_url):
            Logger.objects.create(
                path=request.path,
                method=mch.METHOD_CHOICES_REVERSED[request.method],
                time_delta=diff,
                user_id=user_id[0]

            )

        return response
