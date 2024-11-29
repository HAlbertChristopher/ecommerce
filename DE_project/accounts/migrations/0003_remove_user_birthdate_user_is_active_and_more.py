# Generated by Django 5.1.3 on 2024-11-12 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_birthdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthdate',
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='is staff'),
        ),
    ]