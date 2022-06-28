from django.urls import path
from .views import *

app_name = 'chatting'

urlpatterns = [
    path('chat/', MyChatViewSet.as_view({'get':'show_list', 'post':'create'})),
    path('chat2/', MyChatViewSet2.as_view({'get':'show_list', 'post':'get_detail'})),
    path('chat3/', MyChatViewSet3.as_view({'get':'show_list', 'post':'detail_info'}))
]