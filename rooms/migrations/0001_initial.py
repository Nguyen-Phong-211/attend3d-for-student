# Generated by Django 5.2.3 on 2025-06-26 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('room_name', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=5, max_digits=10)),
                ('room_type', models.CharField(max_length=20)),
                ('capacity', models.IntegerField()),
                ('status', models.CharField(default='1', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
                'db_table': 'rooms',
                'managed': True,
            },
        ),
    ]
