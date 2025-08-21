from django.db import migrations

def create_superuser(apps, schema_editor):
    from django.contrib.auth import get_user_model
    User = get_user_model()

    username = "admin"
    email = "admin@example.com"
    password = "Admin@123"   # change later if you want

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )

class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),  # change "core" if your app name is different
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]