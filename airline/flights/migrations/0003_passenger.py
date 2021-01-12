# Generated by Django 3.1.5 on 2021-01-12 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20210112_0405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights.Flight')),
            ],
        ),
    ]