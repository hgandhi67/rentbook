# Generated by Django 5.0.6 on 2024-06-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_rent_task', '0023_alter_rental_books_user_rent_of_book_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='pdf',
            field=models.FileField(blank=True, default=None, null=True, upload_to='books/pdfs/'),
        ),
    ]
