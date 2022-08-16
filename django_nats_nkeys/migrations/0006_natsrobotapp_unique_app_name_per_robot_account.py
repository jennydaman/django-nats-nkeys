# Generated by Django 3.2.7 on 2022-08-16 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_nats_nkeys', '0005_auto_20220814_2329'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='natsrobotapp',
            constraint=models.UniqueConstraint(fields=('app_name', 'account'), name='unique_app_name_per_robot_account'),
        ),
    ]
