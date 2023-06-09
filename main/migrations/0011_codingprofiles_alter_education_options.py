# Generated by Django 4.1.4 on 2022-12-31 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_education_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodingProfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('link', models.CharField(blank=True, max_length=50, null=True)),
                ('icon', models.FileField(blank=True, null=True, upload_to='codingProfiles')),
            ],
            options={
                'verbose_name': 'Coding Profile',
                'verbose_name_plural': 'Coding Profiles',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['date'], 'verbose_name': 'Education', 'verbose_name_plural': 'Educations'},
        ),
    ]
