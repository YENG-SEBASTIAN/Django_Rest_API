# Generated by Django 4.0 on 2021-12-19 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('patient_records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
