from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=32, primary_key=True)

    def __str__(self) -> str:
        return self.name


class Photo(models.Model):
    """Model definition for generation of migration files.

    imageカラムはnull、blankを許可しない。
    descriptionカラムがnull、blankを許可する。
    created_atカラムは自動で追加。
    tagsカラムはTagテーブルと多対多のリレーションを設定。

    Args:
        models (_type_): _description_
    """

    image = models.ImageField(null=False, blank=False, upload_to="uploads/")
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
