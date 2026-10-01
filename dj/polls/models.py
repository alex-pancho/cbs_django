from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    # Метод для додавання перегляду
    def increment_views(self):
        self.views += 1
        self.save()

    # Метод для отримання короткого зрізу тексту
    def get_preview(self, length=100):
        return self.content[:length] + "..."

    # Властивість (property) — звертаємося як до атрибута
    @property
    def is_popular(self):
        return self.views > 1000


class Tags(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # Українська назва для одного об'єкта (в адмінці)
        verbose_name = "Стаття"
        # Українська назва для множини
        verbose_name_plural = "Статті"
        # Порядок за замовчуванням
        ordering = ["-created_at"]  # від нових до старих
        # Індекс для швидкого пошуку
        indexes = [models.Index(fields=["created_at"])]


class Task(models.Model):
    # Вибір зі списку (choices)
    STATUS_CHOICES = [
        ("new", "Нове"),
        ("in_progress", "У процесі"),
        ("done", "Готово"),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    # Текст, який опціональний
    description = models.TextField(blank=True, null=True)

    # Число з нулевим значенням за замовчуванням
    priority = models.IntegerField(default=0)

    # Email, унікальний для всіх записів
    email = models.EmailField(unique=True)

    # Поле, яке оновлюється автоматично
    updated_at = models.DateTimeField(auto_now=True)
