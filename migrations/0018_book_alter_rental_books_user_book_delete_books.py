# Generated by Django 5.0.6 on 2024-06-19 09:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_rent_task', '0017_alter_rental_books_user_renter_duration'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default='', max_length=60)),
                ('pages', models.CharField(default='', max_length=40)),
                ('author', models.CharField(default='', max_length=60)),
                ('is_free', models.BooleanField(default=False)),
                ('total_renters', models.IntegerField(default=0)),
                ('renter', models.ForeignKey(blank=True, db_column='user_renter', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rented_books', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='rental_books_user',
            name='book',
            field=models.ForeignKey(blank=True, db_column='book_for_rent', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_rental', to='book_rent_task.book'),
        ),
        migrations.DeleteModel(
            name='books',
        ),
    ]
