# Generated by Django 2.1 on 2018-11-11 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20181111_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=255, verbose_name='Address')),
                ('address2', models.CharField(blank=True, max_length=255, verbose_name='Address 2')),
                ('zip_code', models.CharField(max_length=30, verbose_name='Zip code')),
                ('state', models.CharField(choices=[('qc', 'Quebec')], default='qc', max_length=50, verbose_name='State')),
                ('country', models.CharField(choices=[('ca', 'Canada')], default='ca', max_length=3, verbose_name='Country')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=150, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='users', verbose_name='Picture'),
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Address'),
        ),
    ]
