# Generated by Django 3.0.5 on 2022-03-31 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_auto_20220331_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=18),
        ),
    ]
