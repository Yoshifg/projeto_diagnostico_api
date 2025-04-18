# Generated by Django 5.1.6 on 2025-04-02 10:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_useraccount_cnpj'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='is_active',
            new_name='isActive',
        ),
        migrations.RenameField(
            model_name='useraccount',
            old_name='username',
            new_name='username',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='cpf',
            field=models.CharField(default='00000000000',
                                   max_length=14, unique=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='deactivation_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='registration_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]
