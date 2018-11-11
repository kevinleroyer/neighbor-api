# Generated by Django 2.1 on 2018-11-11 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='title')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='SkillsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='title')),
                ('thumbnail', models.ImageField(upload_to='skills')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=150, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.SkillsCategory'),
        ),
        migrations.AddField(
            model_name='user',
            name='skills',
            field=models.ManyToManyField(to='accounts.Skill'),
        ),
    ]
