# Generated by Django 2.1.4 on 2018-12-10 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
        ('response', '0002_affectiveresponse_feature_set'),
    ]

    operations = [
        migrations.AddField(
            model_name='affectiveresponse',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='place.Location'),
        ),
        migrations.AlterField(
            model_name='affectiveresponse',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='classification.Category'),
        ),
    ]
