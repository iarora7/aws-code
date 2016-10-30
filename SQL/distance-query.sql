SELECT a.name, ST_AsText(a.location), ST_Distance(ST_GeomFromtext('SRID=4326;POINT(-118.289962 34.031114)'), a.location)
FROM global_points_tbl a
WHERE 
ST_Distance(ST_GeomFromtext('SRID=4326;POINT(-118.289962 34.031114)'), a.location) < 0.45
LIMIT 15;