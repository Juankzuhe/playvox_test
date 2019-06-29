from django.conf import settings
from django.urls import path


from app import views as app_views

urlpatterns = [
    path("", app_views.HomePageView.as_view(), name="home"),
    path("user/create", app_views.CreateUserView.as_view(), name="create_user"),
    path("user/update/<str:email>/", app_views.UpdateUserView.as_view(), name="update_user"),
    path("user/delete/<str:email>/", app_views.DeleteUserView.as_view(), name="delete_user"),
    path("user/detail/<str:email>/", app_views.DetailUserView.as_view(), name="detail_user"),
    path("user/create/note/<str:email>/", app_views.CreateNoteView.as_view(), name="create_note"),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
