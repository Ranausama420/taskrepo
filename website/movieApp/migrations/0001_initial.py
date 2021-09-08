# Generated by Django 3.2.7 on 2021-09-07 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='moviedata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('imgPath', models.TextField()),
                ('duration', models.IntegerField()),
                ('genre', models.TextField()),
                ('language', models.TextField()),
                ('mpaaRating', models.TextField()),
                ('userRating', models.TextField()),
            ],
        ),
    ]
