# Generated by Django 4.2 on 2023-06-24 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boards", "0004_remove_post_pic"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="pic",
            field=models.ImageField(blank=True, null=True, upload_to="post_pictures/"),
        ),
    ]