Select name,
       cast(EXTRACT(day from payday) as INTEGER) as day
from loan