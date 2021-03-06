# Generated by Django 2.2 on 2020-12-07 11:53

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0002_county'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldOffice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('area_of_coverage', models.IntegerField()),
                ('physical_features', models.TextField(max_length=250, null=True)),
                ('number_of_staff', models.IntegerField()),
                ('issues_addressed', models.TextField(max_length=800, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('designation', models.CharField(default='Field Office', max_length=400)),
            ],
            options={
                'verbose_name_plural': 'Field Offices',
            },
        ),
        migrations.CreateModel(
            name='HeadOffice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('area_of_coverage', models.IntegerField()),
                ('physical_features', models.TextField(max_length=250, null=True)),
                ('number_of_staff', models.IntegerField()),
                ('issues_addressed', models.TextField(max_length=800, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('designation', models.CharField(default='Head Office', max_length=400)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RegionalOffice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('area_of_coverage', models.IntegerField()),
                ('physical_features', models.TextField(max_length=250, null=True)),
                ('number_of_staff', models.IntegerField()),
                ('issues_addressed', models.TextField(max_length=800, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('designation', models.CharField(default='Regional Office', max_length=400)),
                ('head_office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.HeadOffice')),
            ],
            options={
                'verbose_name_plural': 'Regional Offices',
            },
        ),
        migrations.DeleteModel(
            name='Incidence',
        ),
        migrations.AlterModelOptions(
            name='county',
            options={'verbose_name_plural': 'Counties'},
        ),
        migrations.RenameField(
            model_name='county',
            old_name='cty_code',
            new_name='city_code',
        ),
        migrations.RenameField(
            model_name='county',
            old_name='codes',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='county',
            old_name='counties',
            new_name='name',
        ),
        migrations.AddField(
            model_name='fieldoffice',
            name='regional_office',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.RegionalOffice'),
        ),
    ]
