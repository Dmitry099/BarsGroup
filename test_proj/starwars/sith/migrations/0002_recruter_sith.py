# Generated by Django 2.2.4 on 2019-11-10 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sith', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruter',
            name='sith',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recruters', to='sith.Sith', verbose_name='Ситх'),
            preserve_default=False,
        ),
    ]
