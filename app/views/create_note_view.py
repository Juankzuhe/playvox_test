from django.contrib import messages
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View

from app.services.note_service import NoteService


class CreateNoteView(View):

    def post(self, request, *args, **kwargs):
        data = request.POST

        data = dict(
            title=data['title'],
            body=data['body'],
        )

        note_service = NoteService()
        note = note_service.create_note(self.kwargs['email'], data)

        if note:
            messages.success(request, 'Note created successfully')
            return redirect(reverse('detail_user', kwargs={'email': self.kwargs['email']}))
        else:
            return HttpResponseBadRequest()
