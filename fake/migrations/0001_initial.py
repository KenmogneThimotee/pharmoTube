# Generated by Django 3.0.3 on 2020-11-03 17:25

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('sexe', models.CharField(max_length=1)),
                ('profilePicture', models.ImageField(null=True, upload_to='imagesProfile')),
                ('baniere', models.ImageField(null=True, upload_to='imagesBanniere')),
                ('abonne', models.ManyToManyField(related_name='_utilisateur_abonne_+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videosFile')),
                ('nom', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('duree', models.BigIntegerField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('coverImage', models.ImageField(upload_to='coverImages')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('video', models.ManyToManyField(to='fake.Video')),
            ],
        ),
        migrations.CreateModel(
            name='Commenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenue', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('dislike', models.ManyToManyField(related_name='comment_dislike', to=settings.AUTH_USER_MODEL)),
                ('like', models.ManyToManyField(related_name='comment_like', to=settings.AUTH_USER_MODEL)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentateur', to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fake.Video')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='commenter',
            field=models.ManyToManyField(through='fake.Commenter', to='fake.Video'),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='dislike',
            field=models.ManyToManyField(related_name='user_dislike', to='fake.Video'),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='like',
            field=models.ManyToManyField(related_name='user_like', to='fake.Video'),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='reponse',
            field=models.ManyToManyField(related_name='user_reponse', to='fake.Commenter'),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='voir',
            field=models.ManyToManyField(related_name='user_voir', to='fake.Video'),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='vue',
            field=models.ManyToManyField(related_name='user_vue', to='fake.Video'),
        ),
    ]
