# Generated by Django 4.1.3 on 2022-11-16 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_contactprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
