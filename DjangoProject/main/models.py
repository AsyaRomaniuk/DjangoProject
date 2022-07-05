from django.db import models


class User(models.Model):
    name = models.CharField("Ім'я", max_length=50)
    login = models.CharField("Логін", max_length=50)
    password = models.CharField("Пароль", max_length=50)
    creation_date = models.DateTimeField("Дата створення", auto_now_add=True, db_index=True)
    profile = models.ImageField("Профіль", default="static/images/user_default_img.png", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"
