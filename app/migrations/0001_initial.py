# Generated by Django 4.2.4 on 2023-08-06 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Base_Category/')),
                ('title', models.CharField(max_length=155)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Project/')),
                ('title', models.CharField(max_length=155)),
                ('pdf', models.FileField(upload_to='PDF/')),
                ('price', models.CharField(choices=[('0.5-1 Million', '0.5 - 1 million $'), ('1-5 Million', '1 - 5 million $'), ('5-10 Million', '5 - 10 million $'), ('10-15 Million', '10 - 15 million $'), ('15-20 Million', '15 - 20 million $'), ('20-25 Million', '20 - 25 million $'), ('25 + Million', '25 + million $')], max_length=155)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
    ]