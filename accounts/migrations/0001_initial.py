# Generated by Django 3.2.7 on 2021-09-24 21:15

import accounts.models
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
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(blank=True, max_length=100, verbose_name='Псевдоним')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('first_name', models.CharField(blank=True, max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=100, verbose_name='Фамилия')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Статус Администратора')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['first_name'],
            },
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
    ]
