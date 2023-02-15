import django_filters

from authy.models import *
from authy.services import get_birth_year


class StudentFilter(django_filters.FilterSet):
    age = django_filters.CharFilter(
        field_name="date_of_birth", method="filter_students_by_age"
    )

    class Meta:
        model = Student
        fields = {
            "student_name": ["icontains"],
        }

    @staticmethod
    def filter_students_by_age(queryset, _, age) -> List:
        '''
        Take queryset, and student age
        returns a filtered queryset  
        '''
        birth_year = get_birth_year(int(age))
        return queryset.filter(date_of_birth__year__gt=birth_year)
