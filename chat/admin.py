from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Message
class UserAdminCreationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password", "gender", "about")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = UserAdminCreationForm
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "first_name", "last_name", "email", "password", "gender", "about"),
            },
        ),
    )
    list_filter = (
        "gender",
        "is_superuser",
        "is_banned"
    )
#Фильтр (справа) по вышеперечисленным параметрам
    search_filter = (
        "id",
        "last_login",
        "is_superuser",
        "username",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_active",
        "date_joined",
        "gender",
        "about",
        "is_banned"
    )
#Поиск (сверху) по всем полям кроме пароля и аватарки

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "avatar",
#         "username",
#         "first_name",
#         "last_name",
#         "gender",
#         "date_joined",
#         "about",
#         "is_superuser",
#         "is_banned"
#     )

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "usermessage",
        "textmessage",
        "datemessage",
        "reactionscount",
        "is_private"
    )
    ordering = ("-datemessage",)
# Вывод в Админке данных таблицы Сообщения (Мессадж) - ID пользователя, тело сообщения, дата, кол-во лайков, является ли личным. + сортировка по убыванию даты.

@admin.display(description="ФИО")
def user_full_name(self, obj):
    return obj.user.get_full_name()
