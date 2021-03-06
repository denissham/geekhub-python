# Generated by Django 4.0.1 on 2022-02-23 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_id', models.IntegerField(default=None, null=True)),
                ('story_type', models.CharField(max_length=200)),
                ('by', models.CharField(max_length=200)),
                ('timestamp', models.IntegerField(default=None, null=True)),
                ('title', models.TextField(default=None, null=True)),
                ('text', models.TextField(default=None, null=True)),
                ('url', models.TextField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_id', models.IntegerField(default=None, null=True)),
                ('story_type', models.CharField(max_length=200)),
                ('by', models.CharField(max_length=200)),
                ('timestamp', models.IntegerField(default=None, null=True)),
                ('title', models.TextField(default=None, null=True)),
                ('text', models.TextField(default=None, null=True)),
                ('url', models.TextField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_id', models.IntegerField(default=None, null=True)),
                ('story_type', models.CharField(max_length=200)),
                ('by', models.CharField(max_length=200)),
                ('timestamp', models.IntegerField(default=None, null=True)),
                ('title', models.TextField(default=None, null=True)),
                ('text', models.TextField(default=None, null=True)),
                ('url', models.TextField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_id', models.IntegerField(default=None, null=True)),
                ('story_type', models.CharField(max_length=200)),
                ('by', models.CharField(max_length=200)),
                ('timestamp', models.IntegerField(default=None, null=True)),
                ('title', models.TextField(default=None, null=True)),
                ('text', models.TextField(default=None, null=True)),
                ('url', models.TextField(default=None, null=True)),
            ],
        ),
    ]
