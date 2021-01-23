# Generated by Django 3.0.5 on 2021-01-23 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StreamStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_type', models.CharField(blank=True, max_length=255)),
                ('value', models.CharField(blank=True, max_length=255)),
                ('bucket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitch.Bucket')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitch.Game')),
            ],
        ),
    ]
