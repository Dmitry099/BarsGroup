# Generated by Django 2.2.4 on 2019-11-10 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sith', '0005_sith_recruters_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sith',
            name='recruters_count',
            field=models.PositiveIntegerField(default=None, null=True, verbose_name='Количество рекрутов'),
        ),
    ]
