from django.views.generic import TemplateView

from app.services.user_service import UserService
from app.services.note_service import NoteService


class DetailUserView(TemplateView):
    template_name = 'detail_user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_service = UserService()
        note_service = NoteService()
        context['user'] = user_service.get_user(self.kwargs['email'])
        context['notes'] = note_service.get_notes_by_user(self.kwargs['email'])
        return context
