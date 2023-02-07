from django.core.management.base import BaseCommand, CommandError,CommandParser
from typing import Any,Optional
from index.models import Phone,ParameterValue,PhoneParameter
from faker import Faker
from . import _utils as utils
from django.db import connection


class Command(BaseCommand):
    help='Fill models'
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('qty',type=int)

    
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM {0}'.format(ParameterValue._meta.db_table))
        cursor.execute('DELETE FROM {0}'.format(Phone._meta.db_table))
        cursor.execute('DELETE FROM {0}'.format(PhoneParameter._meta.db_table))


        faker = utils.generate_fake_phones()
        
        qty = options['qty']
        if qty < 0:
            CommandError('qty_entities must be greater than 0')
        
        phones = [Phone(**(faker())) for i in range(qty)]

        Phone.objects.bulk_create(phones)

        phone_parameters = [PhoneParameter(name_parameter=parameter) for parameter in ['RAM','Storage','Screen width','Screen height','Battery capacity','Processor']]

        PhoneParameter.objects.bulk_create(phone_parameters)

        ParameterValue.objects.bulk_create([ParameterValue(phone_parameter=phone_parameter,phone=phone, parameter_value='test') for phone in phones for phone_parameter in phone_parameters])
            







        

            
            


