# Generated by Django 3.2.9 on 2021-12-01 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20211201_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_alias',
            field=models.CharField(max_length=50, verbose_name='Псевдоним'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_shorttext',
            field=models.TextField(verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_status',
            field=models.BooleanField(verbose_name='Статус'),
        ),
    ]