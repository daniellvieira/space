# Generated by Django 5.2.4 on 2025-07-21 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='category',
            field=models.IntegerField(choices=[(1, 'Galáxia'), (2, 'Planeta'), (3, 'Estrela'), (4, 'Outro')], default=4),
        ),
    ]
