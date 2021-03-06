# Generated by Django 2.1.7 on 2019-03-29 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Project Name Here', max_length=256)),
                ('github', models.CharField(default='https:github.com/hackett123', max_length=256)),
                ('description', models.TextField(default='Project Description')),
                ('link_to_details', models.CharField(default='/projects/{{name}}', max_length=256)),
            ],
        ),
    ]
