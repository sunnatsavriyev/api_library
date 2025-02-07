# Generated by Django 5.1 on 2024-09-17 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('subtitle', models.CharField(default='', max_length=200)),
                ('auther', models.CharField(default='', max_length=200)),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
    ]
