# Generated by Django 2.1.7 on 2019-03-13 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstaImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_link', models.CharField(max_length=255, unique=True)),
                ('post_link', models.CharField(max_length=255, unique=True)),
                ('post_description', models.TextField(blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
