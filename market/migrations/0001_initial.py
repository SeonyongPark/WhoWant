# Generated by Django 3.2 on 2021-08-13 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='registe time')),
            ],
        ),
        migrations.CreateModel(
            name='MarketPost',
            fields=[
                ('id', models.BigAutoField(help_text='Post ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('post_time', models.DateTimeField(auto_now_add=True, verbose_name='등록 시간')),
                ('body', models.CharField(max_length=500)),
                ('thumbnail', models.ImageField(null=True, upload_to='market/', verbose_name='썸네일')),
            ],
        ),
    ]