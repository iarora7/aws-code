Select * 
from public_places p, category c
where p.category_id = c.id
and c.category_type = 'Hospital'