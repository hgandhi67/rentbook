# Generated by Django 4.2.13 on 2024-06-17 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_rent_task', '0006_alter_books_total_book_renters'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='books',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='rental_books_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rent_start_at', models.DateTimeField(auto_now_add=True)),
                ('rent_complete_at', models.DateTimeField(auto_now_add=True)),
                ('renter_duration', models.DurationField(default=0)),
                ('renter_page_book', models.IntegerField(default=0)),
                ('rent_of_book', models.IntegerField(default=0)),
                ('book', models.ForeignKey(blank=True, db_column='book_for_rent', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_rental', to='book_rent_task.books')),
                ('user', models.ForeignKey(blank=True, db_column='rental_user', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_rental', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
