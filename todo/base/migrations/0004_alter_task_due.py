# Generated by Django 3.2 on 2021-09-16 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20210916_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due',
            field=models.DateField(blank=True, null=True),
        ),
    ]
