# Generated by Django 3.2.23 on 2024-03-02 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('body', models.TextField(blank=True, default='')),
                ('poster100x100', models.CharField(blank=True, default='', max_length=200)),
                ('poster100x125', models.CharField(blank=True, default='', max_length=200)),
                ('poster200x250', models.CharField(blank=True, default='', max_length=200)),
                ('poster300x100', models.CharField(blank=True, default='', max_length=200)),
                ('poster300x200', models.CharField(blank=True, default='', max_length=200)),
                ('poster400x200', models.CharField(blank=True, default='', max_length=200)),
                ('poster400x400', models.CharField(blank=True, default='', max_length=200)),
                ('poster600x300', models.CharField(blank=True, default='', max_length=200)),
                ('poster1200x400', models.CharField(blank=True, default='', max_length=200)),
                ('poster1920x500', models.CharField(blank=True, default='', max_length=200)),
                ('poster1920x900', models.CharField(blank=True, default='', max_length=200)),
                ('poster', models.CharField(blank=True, default='', max_length=200)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.post')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to=settings.AUTH_USER_MODEL)),
                ('posts', models.ManyToManyField(blank=True, related_name='categories', to='api.Post')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
    ]
