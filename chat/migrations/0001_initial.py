# Generated by Django 3.0.7 on 2020-10-25 09:03

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('description', models.TextField(blank=True, help_text='description of the group')),
                ('mute_notifications', models.BooleanField(default=False, help_text='disable notification if true')),
                ('icon', models.ImageField(blank=True, help_text='Group icon', upload_to='chartgroup')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(blank=True, default=False, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, default=None, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('seen', models.BooleanField(blank=True, default=False, null=True)),
                ('blob', models.FileField(default=None, null=True, upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_messages', to=settings.AUTH_USER_MODEL)),
                ('chatgroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.ChatGroup')),
            ],
        ),
    ]
