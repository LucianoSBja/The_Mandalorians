# Generated by Django 4.2.3 on 2023-12-12 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(blank=True, default='usuario/default-user.png', null=True, upload_to='usuario'),
        ),
    ]
