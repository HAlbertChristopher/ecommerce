# Generated by Django 5.1.3 on 2024-11-13 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_user_birthdate_user_is_active_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_admin',
            new_name='is_admmin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_pelanggan',
            field=models.BooleanField(default=False, verbose_name='is admin'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='is admin'),
        ),
    ]
