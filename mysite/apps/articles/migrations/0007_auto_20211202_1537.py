# Generated by Django 3.2.9 on 2021-12-02 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_item_todolist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='ToDoList',
        ),
    ]