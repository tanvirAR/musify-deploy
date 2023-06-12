# Generated by Django 4.1.4 on 2023-04-20 06:14

import authz.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authz', '0019_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default=authz.models.generate_id, max_length=15, primary_key=True, serialize=False, unique=True),
        ),
    ]
