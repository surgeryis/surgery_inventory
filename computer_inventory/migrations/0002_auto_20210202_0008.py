# Generated by Django 3.1.5 on 2021-02-02 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer_inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='computer_name',
            field=models.CharField(max_length=7, null=True),
        ),
    ]
