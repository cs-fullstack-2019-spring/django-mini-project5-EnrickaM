# Generated by Django 2.2 on 2019-03-11 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createnewusermodel',
            name='confirm_password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='createnewusermodel',
            name='email',
            field=models.EmailField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='createnewusermodel',
            name='first_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='createnewusermodel',
            name='foreignkeyToUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='createnewusermodel',
            name='last_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='createnewusermodel',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='createnewusermodel',
            name='username',
            field=models.CharField(default='', max_length=200),
        ),
    ]
