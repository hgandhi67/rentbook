# Generated by Django 5.0.6 on 2024-06-19 10:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_rent_task', '0019_alter_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental_books_user',
            name='renter_duration',
            field=models.DateTimeField(default=datetime.timedelta(days=30)),
        ),
    ]
