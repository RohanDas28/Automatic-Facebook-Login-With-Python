from tasks import sign_up
from fake import get_data

for i in range(100):
    print(sign_up.delay(get_data()))


