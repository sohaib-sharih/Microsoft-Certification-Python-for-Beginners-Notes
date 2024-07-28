from datetime import *
from dateutil.relativedelta import *

now = datetime.now()
print(now)

now = now + relativedelta(months=2, weeks=2, hour=1, days=2)
print(now)