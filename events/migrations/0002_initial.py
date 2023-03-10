# Generated by Django 4.1.5 on 2023-02-07 14:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='participation',
            name='personne',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='participations',
            field=models.ManyToManyField(related_name='Participation', through='events.Participation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='participation',
            unique_together={('personne', 'event')},
        ),
        migrations.AddConstraint(
            model_name='event',
            constraint=models.CheckConstraint(check=models.Q(('dateEvent__gte', datetime.datetime(2023, 2, 7, 15, 1, 9, 697657))), name='la date et invalide'),
        ),
    ]
