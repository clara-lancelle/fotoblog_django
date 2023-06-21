# Generated by Django 4.2.1 on 2023-06-16 11:44

from django.db import migrations

def author_to_contributors(apps, schema_migration):
    User = apps.get_model('authentication', 'User')
    Blog = apps.get_model('blog', 'Blog')
    Contributor = apps.get_model('blog', 'BlogContributor')
    
    for blog in Blog.objects.all():
        author = blog.author
        blog.contributors.add(author, through_defaults={'contribution': 'Auteur principal'})

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogcontributor_blog_contributors'),
    ]

    operations = [
        migrations.RunPython(author_to_contributors)
    ]
