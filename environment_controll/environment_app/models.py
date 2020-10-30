from django.db import models

class Collection(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='collections')
    owner_id = models.CharField(max_length=100)
    is_disabled = models.BooleanField(default=False)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=255)
    image = models.ImageField(upload_to='units')
    is_disabled = models.BooleanField(default=False)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Node(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    is_disabled = models.BooleanField(default=False)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.pk

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    data_type = models.CharField(max_length=100)
    data_size = models.CharField(max_length=100)
    min_value = models.FloatField()
    max_value = models.FloatField()
    technology = models.CharField(max_length=255)
    working_voltage = models.FloatField()
    dimensions = models.CharField(max_length=255) 
    special_facts = models.TextField()
    image = models.ImageField(upload_to='sensors')
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class NodeSensor(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    min_value = models.FloatField()
    max_value = models.FloatField()
    is_disabled = models.BooleanField(default=False)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.pk

class Data():
    node = models.ForeignKey(Node)
    nodeSensor = models.ForeignKey(NodeSensor)
    data = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pk


