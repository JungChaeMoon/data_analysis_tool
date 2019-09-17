from django.db import models


class DataModel(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class DataSaveModel(models.Model):
    data_model = models.ForeignKey('analysis.DataModel', on_delete=models.CASCADE, related_name='data_save_model')
    weight = models.IntegerField()
    gyro = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
