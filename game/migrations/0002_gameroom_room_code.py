# Generated by Django 4.2.11 on 2024-04-24 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameroom',
            name='room_code',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
