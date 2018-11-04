# Generated by Django 2.1.1 on 2018-10-30 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_auto_20181010_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(max_length=100)),
                ('update', models.DateTimeField(auto_now_add=True)),
                ('creative', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postTime', models.DateTimeField(auto_now=True)),
                ('like', models.IntegerField(blank=True, default=0, null=True)),
                ('isopen', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AddField(
            model_name='profile',
            name='isactive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='rezome',
            field=models.TextField(default='None', max_length=600),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
