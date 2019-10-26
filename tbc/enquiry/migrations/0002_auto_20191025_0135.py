# Generated by Django 2.2.1 on 2019-10-24 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('companyname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=20)),
                ('phoneno', models.CharField(max_length=12)),
                ('venue', models.CharField(max_length=30)),
                ('typeofevent', models.CharField(max_length=100)),
                ('datetimestartofevent', models.DateTimeField()),
                ('datetimeendofevent', models.DateTimeField()),
                ('preflanguage', models.CharField(blank=True, max_length=10, null=True)),
                ('audiencecount', models.CharField(blank=True, max_length=10, null=True)),
                ('budget', models.CharField(blank=True, max_length=10, null=True)),
                ('otherinfo', models.CharField(blank=True, max_length=200, null=True)),
                ('comedians', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='email',
            field=models.EmailField(max_length=20),
        ),
    ]
