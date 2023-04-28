from faker import Faker
import pandas as pd
import numpy as np
import os
import datetime
import random

from password_generator import PasswordGenerator

def get_data():
     pwo = PasswordGenerator()
     fake = Faker()

     gender = np.random.choice(["M", "F"], p=[0.5, 0.5])
     first_name = fake.first_name_male() if gender =="M" else fake.first_name_female()
     last_name = fake.last_name()
     address = fake.address()
     from random import randint

     year = randint(1990, 2000)
     month = randint(1, 12)
     day = randint(1, 30)
     output ={
          "firstname": first_name,
          "lastname": last_name,
          "address": address,
          "gender": gender,
          "birth_month": 'Apr',
          'birth_year': str(year),
          'birth_day': str(day),
          "email": f"{first_name}.{last_name}@{fake.domain_name()}",
          "pass": pwo.generate(),
     }
     print(output)
     return output
