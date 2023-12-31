# Generated by Django 4.2 on 2023-07-14 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("boards", "0008_topic_views_alter_post_pic"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="updated_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="post", name="updated_dt", field=models.DateTimeField(null=True),
        ),
    ]
