# Generated by Django 3.0.6 on 2020-05-17 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='short',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lurl', models.URLField()),
                ('surl', models.URLField()),
                ('views', models.IntegerField()),
            ],
            options={
                'verbose_name': 'url',
                'verbose_name_plural': 'urls',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
