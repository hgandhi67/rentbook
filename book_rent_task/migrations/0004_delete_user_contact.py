# Generated by Django 5.0.6 on 2024-06-17 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_rent_task', '0003_delete_terst_alter_user_contact_contact_no'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_contact',
        ),
    ]
