from datetime import date
from typing import Union

from rest_framework import exceptions

from authy.models import User, Student


def get_user(user_id: int) -> Union[User, Exception]:
    """This function gets a user by its ID."""
    user = User.objects.get(id=user_id)

    if user is None:
        raise exceptions.NotFound({"message": "user does not exist."})

    return user


def get_birth_year(age: int) -> int:
    """
    Take student age and returns the year of birth
    """
    today = date.today()
    birth_year = today.year - age

    return birth_year


def generate_student_id(full_name: str) -> str:
    """
    Take student name and generates the student id
    """
    student_count = Student.objects.count()
    student_id = f"{student_count:05}"
   
    try:
        id_initials = full_name.split(" ")[0][0] + full_name.split(" ")[1][0]
   
    except:
        id_initials = full_name.split(" ")[0][0] + full_name.split(" ")[0][1]
    
    student_number = id_initials + student_id

    return student_number
