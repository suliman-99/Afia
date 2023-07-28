# Generated by Django 4.2.3 on 2023-07-28 20:49

import Auth.models
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('static', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('email_code', models.CharField(blank=True, max_length=500, null=True)),
                ('email_code_time', models.DateTimeField(blank=True, null=True)),
                ('email_verified', models.BooleanField(default=False)),
                ('role', models.PositiveIntegerField(blank=True, choices=[(0, 'Doctor'), (1, 'Patient')], null=True)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.IntegerField(blank=True, choices=[(0, 'Male'), (1, 'Female')], null=True)),
                ('photo', models.ImageField(blank=True, max_length=500, null=True, upload_to=Auth.models.user_photo_path)),
                ('blood_type', models.IntegerField(blank=True, choices=[(0, 'O+'), (1, 'A+'), (2, 'B+'), (3, 'AB+'), (4, 'O-'), (5, 'A-'), (6, 'B-'), (7, 'AB-')], null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('chronic_disease', models.TextField(blank=True, null=True)),
                ('genetic_disease', models.TextField(blank=True, null=True)),
                ('other_info', models.TextField(blank=True, null=True)),
                ('license', models.ImageField(blank=True, max_length=500, null=True, upload_to=Auth.models.user_photo_path)),
                ('available_for_meeting', models.BooleanField(default=False)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='static.city')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('specialization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='static.specialization')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', Auth.models.UserManager()),
            ],
        ),
    ]
