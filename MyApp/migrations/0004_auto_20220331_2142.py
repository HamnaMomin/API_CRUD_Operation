# Generated by Django 3.0.5 on 2022-03-31 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_auto_20220331_1602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='father_name',
            new_name='fatherName',
        ),
    ]
