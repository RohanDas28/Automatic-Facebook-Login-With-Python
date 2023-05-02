from tasks import sign_up
from fake import get_data
print(sign_up.delay(get_data()))
exit()
b = sign_up.delay(get_data())
c = sign_up.delay(get_data())
d = sign_up.delay(get_data())
print(a)
print(b)
print(c)
print(d)


