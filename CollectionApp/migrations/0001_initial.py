# Generated by Django 3.2.6 on 2021-08-29 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('collection_frequency', models.IntegerField()),
                ('last_collection', models.DateTimeField()),
                ('bin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CollectionApp.bin')),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CollectionApp.operation')),
            ],
            options={
                'unique_together': {('bin', 'operation')},
            },
        ),
    ]
