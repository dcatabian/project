# Generated by Django 4.0.3 on 2022-04-15 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_item_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logininfo',
            name='username',
            field=models.CharField(max_length=31, unique=True),
        ),
    ]
