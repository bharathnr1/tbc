# Generated by Django 2.2.1 on 2019-10-27 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comedians', '0006_remove_registercomedian_test_multi_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registercomedian',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pic/'),
        ),
    ]
