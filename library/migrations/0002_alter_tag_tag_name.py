# Generated by Django 3.2.7 on 2021-09-24 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(blank=True, max_length=256, verbose_name='Тэг'),
        ),
    ]
