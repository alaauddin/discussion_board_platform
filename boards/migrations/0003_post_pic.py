# Generated by Django 4.2 on 2023-06-24 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boards", "0002_post_likes_alter_post_topic"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="pic",
            field=models.ImageField(blank=True, null=True, upload_to="post_pictures/"),
        ),
    ]
