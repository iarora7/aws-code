-- distance in meters
Select c.name, c.location, ST_Distance(
	ST_Transform(ST_GeomFromtext('POINT(-121.937444 37.410294)', 4326), 26986),
	ST_Transform(ST_GeomFromtext(c.latlon, 4326), 26986)) as dist_meter
from coach c

-- distance in miles
Select c.name, c.location, ST_Distance(
	ST_Transform(ST_GeomFromtext('POINT(-121.937444 37.410294)', 4326), 26986),
	ST_Transform(ST_GeomFromtext(c.latlon, 4326), 26986)) / 1609 as dist_miles
from coach c

-- coaches within 10 miles
Select c.name, c.location, ST_Distance(
	ST_Transform(ST_GeomFromtext('POINT(-121.937444 37.410294)', 4326), 26986),
	ST_Transform(ST_GeomFromtext(c.latlon, 4326), 26986)) / 1609 as dist_miles
from coach c
WHERE ST_DWithin(
	ST_Transform(ST_GeomFromtext('POINT(-121.937444 37.410294)', 4326), 26986),
	ST_Transform(ST_GeomFromtext(c.latlon, 4326), 26986), 1609*10)
