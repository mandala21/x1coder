# Generated by Django 3.0.5 on 2020-05-16 23:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challegen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='challegen',
            name='winner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='victories', to=settings.AUTH_USER_MODEL),
        ),
    ]
