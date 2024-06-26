# Generated by Django 4.2.13 on 2024-06-17 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_rent_task', '0004_delete_user_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(default='', max_length=60)),
                ('book_pages', models.CharField(default='', max_length=40)),
                ('book_author', models.CharField(default='', max_length=60)),
                ('book_free', models.BooleanField(default=False)),
                ('total_book_renters', models.IntegerField(default=0, max_length=100)),
                ('book_renter', models.ForeignKey(blank=True, db_column='user_renter', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_renter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
