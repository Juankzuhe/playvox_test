from django.contrib import messages
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView

from app.services.user_service import UserService


class UpdateUserView(TemplateView):
    template_name = 'update_user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_service = UserService()
        context['user'] = user_service.get_user(self.kwargs['email'])
        return context

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

        user = user_service.update_user(self.kwargs['email'], data)

        if user:
            messages.success(request, 'User {} updated successfully'.format(data['email']))
            return redirect(reverse('home'))
        else:
            return HttpResponseBadRequest()
