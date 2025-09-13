from .timestamp import Timestamp, models


class Province(Timestamp):
    name = models.CharField(max_length=45)