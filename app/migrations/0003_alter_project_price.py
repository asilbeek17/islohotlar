# Generated by Django 4.2.4 on 2023-08-06 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_project_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='price',
            field=models.CharField(choices=[('0.5 - 1 million $', '0.5 - 1 million $'), ('1 - 5 million $', '1 - 5 million $'), ('5 - 10 million $', '5 - 10 million $'), ('10 - 15 million $', '10 - 15 million $'), ('15 - 20 million $', '15 - 20 million $'), ('20 - 25 million $', '20 - 25 million $'), ('25 - 30 million $', '25 - 30 million $'), ('30 + million $', '30 + million $')], max_length=155),
        ),
    ]
