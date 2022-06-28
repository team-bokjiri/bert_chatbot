from django.urls import path


from . import views

app_name = 'accounts'

urlpatterns = [
    path('create/', views.Registration.as_view()),
    path('login/', views.Login.as_view()),
    path('user/', views.PostListMixins.as_view()),
    path('password_change/', views.ChangePasswordView.as_view()),
    path('userinformation/', views.UserInformationViewSet.as_view({'get': 'show_list',
                                                                   'post': 'save_information',
                                                                   'delete': 'delete_information'})),
    path('user_delete/', views.UserDelete.as_view()),
]
