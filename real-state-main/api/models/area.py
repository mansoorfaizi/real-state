from django.db import models

class Area(models.Model):
    name = models.CharField(max_length=45) 
    district = models.ForeignKey(
        "District",               
        on_delete=models.CASCADE, 
        related_name="areas",
        db_index=True            
    )

    timestamp = models.ForeignKey(
        "Timestamp",              
        on_delete=models.CASCADE, 
        related_name="areas",
        db_index=True             
    )

    def __str__(self):
        return self.name
