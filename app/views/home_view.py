from django.views.generic import TemplateView

from app.services.user_service import UserService


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_service = UserService()
        context['users'] = user_service.get_list_users()
        return context
