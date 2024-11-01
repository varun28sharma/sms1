# Generated by Django 5.0.7 on 2024-10-15 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_studentlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(default='example@example.com', max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
    ]
