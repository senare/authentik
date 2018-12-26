# Generated by Django 2.1.4 on 2018-12-26 22:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passbook_core', '0007_auto_20181226_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='passbook_core.Group'),
        ),
        migrations.RemoveField(
            model_name='group',
            name='children',
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together={('name', 'parent')},
        ),
    ]
