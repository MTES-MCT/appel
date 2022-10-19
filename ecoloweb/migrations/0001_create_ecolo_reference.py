# Generated by Django 4.1.1 on 2022-10-19 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EcoloReference',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('apilos_model', models.CharField(max_length=64)),
                ('ecolo_id', models.IntegerField()),
                ('apilos_id', models.TextField(max_length=32)),
            ],
            options={
                'unique_together': {('apilos_model', 'ecolo_id'), ('apilos_model', 'ecolo_id', 'apilos_id')},
            },
        ),
    ]
