# Generated by Django 3.2.6 on 2021-08-07 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]