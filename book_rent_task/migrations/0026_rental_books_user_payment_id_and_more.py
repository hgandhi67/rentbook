# Generated by Django 5.0.6 on 2024-06-20 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_rent_task', '0025_remove_book_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental_books_user',
            name='payment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rental_books_user',
            name='payment_signature',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
