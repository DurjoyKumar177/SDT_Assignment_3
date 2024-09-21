from django.db import models

class TaskCategory(models.Model):
    category_name = models.CharField(max_length=100)
    tasks = models.ManyToManyField('task.TaskModel', related_name='task_categories', blank=True)  

    def __str__(self):
        return self.category_name
