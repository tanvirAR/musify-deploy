# Generated by Django 4.1.4 on 2023-04-18 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authz', '0007_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='888e4f6079ba4f6', max_length=15, primary_key=True, serialize=False, unique=True),
        ),
    ]
