# Generated by Django 5.0.6 on 2024-06-19 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_rent_task', '0013_books_created_at_books_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental_books_user',
            name='rent_complete_at',
        ),
        migrations.RemoveField(
            model_name='rental_books_user',
            name='rent_start_at',
        ),
    ]
