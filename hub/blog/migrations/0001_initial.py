# Generated by Django 4.1.2 on 2023-02-23 20:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=23)),
                ('timeStamp', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
