from django.db import models
from django.utils import timezone


class Planets(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    climate = models.CharField(max_length=255, null=True, blank=True)
    diameter = models.IntegerField(null=True, blank=True)
    orbital_period = models.IntegerField(null=True, blank=True)
    population = models.BigIntegerField(null=True, blank=True)
    rotation_period = models.IntegerField(null=True, blank=True)
    surface_water = models.FloatField(null=True, blank=True)
    terrain = models.CharField(max_length=255, null=True, blank=True)
    # NOTE: `auto_now_add`/`auto_now` cannot be combined with `default`
    # (Django raises fields.E160), and we need a `default` so that
    # `manage.py loaddata` can insert rows from ex09_initial_data.json even
    # when created/updated are omitted from a fixture record. We therefore
    # use plain DateTimeFields with a default, and set `updated` by hand in
    # save() below to reproduce the "auto_now" behaviour on normal saves.
    created = models.DateTimeField(default=timezone.now, editable=False)
    updated = models.DateTimeField(default=timezone.now, editable=False)

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class People(models.Model):
    name = models.CharField(max_length=64, null=False)
    birth_year = models.CharField(max_length=32, null=True, blank=True)
    gender = models.CharField(max_length=32, null=True, blank=True)
    eye_color = models.CharField(max_length=32, null=True, blank=True)
    hair_color = models.CharField(max_length=32, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    mass = models.FloatField(null=True, blank=True)
    # NOTE: the subject describes `homeworld` as "a foreign key referencing the
    # name column" of Planets, but the provided ex09_initial_data.json fixture
    # stores homeworld as the numeric primary key of a Planets row (standard
    # Django loaddata behaviour for a ForeignKey). We therefore implement a
    # regular ForeignKey (pointing at Planets' pk) so that
    # `manage.py loaddata ex09_initial_data.json` loads the provided fixture
    # correctly.
    homeworld = models.ForeignKey(
        Planets, on_delete=models.CASCADE, null=True, blank=True, related_name='people'
    )
    created = models.DateTimeField(default=timezone.now, editable=False)
    updated = models.DateTimeField(default=timezone.now, editable=False)

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
