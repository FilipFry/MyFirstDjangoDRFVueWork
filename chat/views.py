# from django.shortcuts import render
from .models import Message, User
#from .forms import MessageForm
# from django.views.generic import ListView, CreateView
# from django.http import JsonResponse
# from django.urls import reverse_lazy
from rest_framework.viewsets import ModelViewSet
from .serializers import MessageSerializer, CurrentUserSerializer, UsersSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

class CurrentUserView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        if not request.user.is_authenticated:
            return Response({"is_authenticated": False, "user": None})

        return Response(
            {
                "is_authenticated": True,
                "user": CurrentUserSerializer(
                    request.user, context={"request": request}
                ).data,
            }
        )

class MessageFilter(filters.FilterSet):
    class Meta:
        model = Message
        fields = "__all__"

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

class MessageViewSet(ModelViewSet):
#DRF - создаём класс для работы с Django Rest Framework
    queryset = Message.objects.all()
    #Создаём список объектов (массив?) который достаёт всю информацию, хранящуюся в таблице Сообщения
    serializer_class = MessageSerializer
    
    def perform_create(self, serializer):
        serializer.save(usermessage=self.request.user)

# def vue_app(request):
#     return render(request, "index.html")


# def chat_view(request):
#      chat = Message.objects.all()
#      context = {"chat": chat}
#      return render(request,"message_list.html", context)

# class ChatViewList(ListView):
#     model = Message
# #Имя таблицы БД, на основании которой будет строиться отображение информации. 
#     template_name = "message_list.html"
# #Имя шаблона, который будет генерировать результат    
#     context_object_name = "messages"
# #context_object_name - переменная, которую мы передаём в шаблон.
    
#     def get_queryset(self):
#         return Message.objects.all()
    
# class MessageCreateView(CreateView):
#     model = Message
#     form_class = MessageForm
#     template_name = "message_form.html"
#     success_url = reverse_lazy("json")

    
# #Как сгенерировать JSON-последовательность для вывоза из базы ? 
# class ChatViewJSON(ListView):
# #Создаём класс с любым именем, беря за основу классовый (встроенный в Django) вью ЛистВью.
#     model = Message
# #Указываем, из какой таблицы базы данных он будет браться
#     def get_queryset(self):
#         return Message.objects.all()
# #Вот тут надо уточнить, что делает get_queryset
    
#     def render_to_response(self, context, **response_kwargs):
#         messages = context["object_list"]
#         data =[]
# #data - создаём пустой массив данных, который потом будем заполнять
#         for message in messages:
#             data.append(
#                 {
#                     "id": message.id,
#                     #"iduser": message.get_usermessage_display(),
#                     "textmessage": message.textmessage,
#                     "date": message.datemessage,
#                     "reactiosncount": message.reactionscount,
#                     "isprivate": message.is_private,
#                 }
#             )
# #В цикле заполняем массив data данными из БД в формате: "имя_поля_которое_будет_отражено_в_json": данные поля из Бады Данных
#         return JsonResponse(data, safe=False)
    
    
# # def chat_view(request):
# #     messages = Message.objects.all().order_by("datemessage")
# #     context = {
# #         "messages": messages
# #     }
# #     return render(request, "chat_window.html", context)
# #Поправьте меня, если я ошибаюсь.
# #Выполняем Селект_релатед (более оптимизированный запрос к базе данных и дёргаем из БД все данные. ) и грузим в массив messages (типа переменная) все данные. 

# # def sent_message(request):
# #     if request.user.is_anonymous:
# #         if request.method == "POST":
# #             form = MessageForm(request.POST)
# #             if form.is_valid():
# #                 form.save()
# #         else:
# #             form = MessageForm()
# #     else:
# #         return redirect('home')
# #     return render(request, "message_form.html", {"form":form})