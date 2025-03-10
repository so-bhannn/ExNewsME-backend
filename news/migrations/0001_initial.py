# Generated by Django 5.1.1 on 2024-09-19 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('category', models.CharField(choices=[('entertainment', 'Entertainment'), ('sports', 'Sports'), ('national', 'National'), ('international', 'International'), ('science_and_tech', 'Science & Tech'), ('business_and_economics', 'Business & Economics')], max_length=22)),
                ('published_date', models.DateTimeField()),
                ('image', models.FileField(blank=True, null=True, upload_to='news_articles/images/')),
            ],
        ),
    ]
