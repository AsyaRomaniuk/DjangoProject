# Generated by Django 3.2.6 on 2022-06-22 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name="Ім'я")),
                ('login', models.CharField(max_length=50, verbose_name='Логін')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль')),
                ('creation_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата створення')),
                ('profile', models.ImageField(blank=True, default='static/images/user_default_img.png', null=True, upload_to='', verbose_name='Профіль')),
            ],
            options={
                'verbose_name': 'Користувач',
                'verbose_name_plural': 'Користувачі',
            },
        ),
    ]
