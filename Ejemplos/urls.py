
from django.contrib import admin
from django.urls import include, path
from apis.views import TodoAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/v1/', include('apis.urls')),
    path('todo/',TodoAPIView.as_view()),
]
