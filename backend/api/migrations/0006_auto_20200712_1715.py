# Generated by Django 2.2.14 on 2020-07-12 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200712_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='sharing',
            field=models.CharField(choices=[('personal', 'personal'), ('shared', 'shared')], editable=False, max_length=8),
        ),
    ]