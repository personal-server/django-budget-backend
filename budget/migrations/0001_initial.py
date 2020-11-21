# Generated by Django 2.2.14 on 2020-07-12 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('type', models.CharField(choices=[('income', 'income'), ('expense', 'expense')], max_length=7)),
                ('category', models.CharField(max_length=100)),
                ('budget', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Budget')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('type', models.CharField(choices=[('income', 'income'), ('expense', 'expense')], max_length=7)),
                ('merchant', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('date', models.DateField()),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('line_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.LineItem')),
                ('user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]