from django.db import models
from django.urls import reverse


class Post(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Message = models.TextField(blank=True, null=True)
    featured = models.BooleanField(default=False)

    # Dynamicly linking to URL.
    def get_absolute_url(self):
        print("id: >>>", self.id)
        return f"dynamic/{self.id}"
        # return reverse("dynamic", kwargs={"id": self.id})
