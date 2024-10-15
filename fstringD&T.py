#date and time
from datetime import datetime
today=datetime(2024,9,20)
print(f"{today}")
print(f"{today:%d-%b-%Y}")
print(f"{today:%d/%b/%Y}")