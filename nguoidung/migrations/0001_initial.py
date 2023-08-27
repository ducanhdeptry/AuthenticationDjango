# Generated by Django 4.2.1 on 2023-08-13 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('shortDesc', models.TextField()),
                ('body', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
