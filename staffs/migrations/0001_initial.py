# Generated by Django 5.2.3 on 2025-06-26 18:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportLog',
            fields=[
                ('import_log_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=255)),
                ('import_type', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
                ('error_report', models.TextField(null=True)),
                ('created_at', models.TimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Import Log',
                'verbose_name_plural': 'Import Logs',
                'db_table': 'import_logs',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=1)),
                ('dob', models.DateField()),
                ('avatar_url', models.TextField(null=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Staff',
                'verbose_name_plural': 'Staffs',
                'db_table': 'staffs',
                'managed': True,
            },
        ),
    ]
