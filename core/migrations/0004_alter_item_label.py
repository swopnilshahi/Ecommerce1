# Generated by Django 3.2.4 on 2021-06-08 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_item_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'Primary'), ('S', 'Secondary'), ('D', 'Danger')], max_length=1),
        ),
    ]
