# Generated by Django 2.2 on 2019-03-11 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeApp', '0002_auto_20190311_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewrecipeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('maker', models.CharField(default='', max_length=200)),
                ('datecreated', models.DateField(default=None)),
                ('description', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
