###### Django imports #####
from django.db.models.signals import post_save
from django.dispatch import receiver
###### End Django imports ######

###### Local imports ######

from authy.models import Student
from authy.services import generate_student_id
###### End Local imports ######


@receiver(post_save, sender=Student)
def create_inventory(sender, instance: Student, created: bool, **kwargs: dict):
    if created:
        instance.student_number = generate_student_id(instance.student_name)
        instance.save()