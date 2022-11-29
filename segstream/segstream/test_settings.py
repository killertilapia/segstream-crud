from .settings import *

print("Running Test Settings")

DEBUG = True

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
}

TEST_RUNNER = "django.test.runner.DiscoverRunner"