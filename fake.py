from faker import Faker
import pandas as pd
import numpy as np
import os
import datetime
import random
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
     "First name": first_name,
     "Last Name": last_name,
     "address": address,
     "gender": gender,
     "date": day+month+year,
     "E-mail": f"{first_name}.{last_name}@{fake.domain_name()}"
    }


print(output)
