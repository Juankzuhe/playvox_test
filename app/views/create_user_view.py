from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView

from app.services.user_service import UserService


class CreateUserView(TemplateView):
    template_name = 'create_user.html'

    def post(self, request, *args, **kwargs):
        data = request.POST
        user_service = UserService()

        data = dict(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            age=data['age'],
            sex=data['sex'],
        )

        if user_service.get_user(data['email']) is None:
            print('in1')
            user = user_service.create_user(data)

            if user:
                messages.success(request, 'User created successfully')
                return redirect(reverse('home'))
            else:
                return HttpResponseBadRequest()
        else:
            messages.error(request, 'User {} already exist'.format(data['email']))
            return redirect(reverse('home'))
