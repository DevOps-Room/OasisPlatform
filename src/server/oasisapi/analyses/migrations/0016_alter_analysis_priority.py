# Generated by Django 3.2.5 on 2021-11-17 17:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyses', '0015_alter_analysis_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='priority',
            field=models.IntegerField(help_text='Priority of this analysis for input generation and execution. Set from 0 to 10 where 0 is the highest priority.', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
