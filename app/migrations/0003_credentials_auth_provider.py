# Generated by Django 5.1.4 on 2025-03-03 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_credentials_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='credentials',
            name='auth_provider',
            field=models.CharField(choices=[('Facebook', 'Facebook'), ('Instagram', 'Instagram')], default='Instagram', max_length=100, verbose_name='Authentication Provider'),
        ),
    ]
