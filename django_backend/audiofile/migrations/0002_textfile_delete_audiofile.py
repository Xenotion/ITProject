# Generated by Django 4.2.3 on 2023-09-18 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audiofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='text_files/')),
            ],
        ),
        migrations.DeleteModel(
            name='AudioFile',
        ),
    ]