# Generated by Django 4.2.13 on 2024-06-17 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_rent_task', '0007_books_created_at_books_updated_at_rental_books_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental_books_user',
            name='rent_complete_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='rental_books_user',
            name='rent_start_at',
            field=models.DateTimeField(),
        ),
    ]