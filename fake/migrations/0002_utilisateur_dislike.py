# Generated by Django 3.0.3 on 2020-10-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fake', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='dislike',
            field=models.ManyToManyField(related_name='user_dislike', to='fake.Video'),
        ),
    ]