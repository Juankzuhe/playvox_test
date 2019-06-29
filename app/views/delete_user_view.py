from django.contrib import messages
from django.views.generic import View
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.urls import reverse

from app.services.user_service import UserService


class DeleteUserView(View):
    def get(self, request, **kwargs):
        user_service = UserService()
        user = user_service.delete_user(self.kwargs['email'])

        if user:
            messages.success(request, 'User {} deleted successfully'.format(self.kwargs['email']))
            return redirect(reverse('home'))
        else:
            return HttpResponseBadRequest()
