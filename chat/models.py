from django.db import models
from django.contrib.auth.models import AbstractUser

class gender(models.TextChoices):
    MALE = "male", "Мужчина",
    FEMALE = "female", "Женщина"
# Создаём текстовый выбор из 2х вариаций - Мужчина|Женщина. 

#АбстрактныйПользователь по умолчанию уже имеет поля: 
# id
# password - Пароль
# last_login - Видимо, время последнего входа
# is_superuser - Проверка, есть ли права быть СуперПользователем
# username - Ник, Имя Пользователя
# first_name - Имя
# last_name - Фамилия
# email - Эл.Почта
# is_staff - Является ли персоналом (потом почитать
# is_active - Активен ?
# date_joined - Дата присоединения (Видимо как дата регистрации)

class User(AbstractUser):
#Добавляем к АбстрактномуПользователю свои поля
    gender = models.CharField(verbose_name="Пол пользователя", choices=gender.choices, default=gender.MALE)
# Пускай будет пол пользователя, описан выбором выше.
    avatar = models.ImageField(verbose_name="Аватар пользователя", upload_to="avatars/", blank=True)
# Аватарка
    about = models.TextField(verbose_name="О пользователе", max_length=255, blank=True)
# Поле "пара строк о себе"
    is_banned = models.BooleanField(verbose_name="Забанен ли пользователь? (Да|Нет)", default=False)
# Забанен ли пользователь
    
    class Meta(AbstractUser.Meta):
        verbose_name = "Участник чата"
        verbose_name_plural = "Участники чата"
# Класс мета - для Админкми
    
    def __str__(self):
        return self.username
# Код, который в админке заменяет "Участник чата (<- Определяется в Классе Мета чуть выше.) “User object (6) (<- вот это заменяется на  удобочитаемое имя)“ был у" На удобочитаемое имя, из поля НикНейм.
# Вывесли много параметров - return f"{self.id} {self.username}
    
class Message(models.Model):
    usermessage = models.ForeignKey("User", verbose_name="Имя пользователя, отправившего сообщение", on_delete=models.CASCADE)
# Связь таблиц "Юзер" и "Мессадж", чтобы имя пользователя и информация о нём-же бралась из таблички "Юзер". Связь 1 ко Многим - у одного пользователя может быть сколько угодно сообщений, но у одного сообщения может быть только один пользователь.
    textmessage = models.TextField(verbose_name="Текст сообщения", max_length=255, blank=False)
# Сам текст сообщения, по хорошему надо конечно зашифровать, но будем как в MAXе
    datemessage = models.DateTimeField(verbose_name="Дата отправки сообщения", auto_now=False, auto_now_add=True)
# Дата и время сообщения 
    reactionscount = models.PositiveIntegerField(verbose_name="Количество реакций(Лайков)", default=0)
# Количество реакций (лайков)
    is_private = models.BooleanField(verbose_name="Личное ли это сообщение?(Да|Нет)", default=False)
# Личное или общее сообщение
    
    class Meta:
        verbose_name = 'Сообщение чата'
        verbose_name_plural = 'Сообщения чата'
# Класс мета - для Админкми

    def __str__(self):
       return f"Сообщение от {self.usermessage} (ID: {self.id})"
# Код, который в админке заменяет "Сообщение чата (<- Определяется в Классе Мета чуть выше.) “Message object (6) (<- вот это заменяется на  удобочитаемое имя)“ был у" На удобочитаемое имя, из поля Пока что ID сообщения.

# class PrivateMessageRouter(models.Model):
#     from_user = 
#     to_user = 
#     message_id = 

#     class Meta:
#         verbose_name = 'Роутер личных сообщений чата'
#         verbose_name_plural = 'Роутеры личных сообщений чата'

#     def __str__(self):
#         return f"Личное сообщение от {self.from_user} для {self.to_user}"