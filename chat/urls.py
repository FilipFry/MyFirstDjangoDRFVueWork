from django.urls import path, include
#from .views import ChatViewList, ChatViewJSON, MessageCreateView
#from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, CurrentUserView, UserViewSet

router = DefaultRouter()
router.register("message", MessageViewSet)
router.register("users", UserViewSet)
#router.register("user", UserViewSet)

urlpatterns = [
    # path("", vue_app, name="vue_app"),
    path("", include(router.urls), name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api/user/", CurrentUserView.as_view(), name="current-user"),
    path("api/", include(router.urls)),
 #  path("", ChatViewList.as_view(), name="home"),
 #  path("json", ChatViewJSON.as_view(), name="json"),
 #  path("add", MessageCreateView.as_view(), name="add"),
# По пустому Урлу вызываем вьюшку "Чат_вью", которая прописана в views.py
]
