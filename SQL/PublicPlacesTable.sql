
drop table if exists public_places;
CREATE TABLE public_places
(	ID 	            SERIAL PRIMARY KEY     NOT NULL,
	CATEGORY_ID  integer REFERENCES CATEGORY (id),
	name TEXT,
	location GEOMETRY(POINT,4326),
	st_address TEXT,
	city TEXT,
	state TEXT,
	zip TEXT,
	rating DECIMAL
	);

INSERT into public_places 
(category_id, name, location, st_address, city, state, zip, rating) VALUES
(4, 'Alliance College-Ready Public Schools', ST_GeomFromText('POINT(-118.282387 34.037448)' , 4326), '2023 S Union Ave', 'Los Angles', 'California', '90007', 3)
;
INSERT into public_places 
(category_id, name, location, st_address, city, state, zip, rating) VALUES
(4, 'Vermont Avenue Elementary School', ST_GeomFromText('POINT(-118.292944 34.031473)' , 4326), '1435 W 27th St', 'Los Angles', 'California', '90007', 3.5)
;
INSERT into public_places 
(category_id, name, location, st_address, city, state, zip, rating) VALUES
(4, 'Orthopaedic Medical Magnet High School', ST_GeomFromText('POINT(-118.271443 34.029908)' , 4326), '300 W 23rd St', 'Los Angles', 'California', '90007', 4)
;
INSERT into public_places 
(category_id, name, location, st_address, city, state, zip, rating) VALUES
(4, 'USC Marshall School of Business', ST_GeomFromText('POINT(-118.285774 34.019779)' , 4326), '3670 Trousdale Pkwy', 'Los Angles', 'California', '90007', 4)
;
INSERT into public_places 
(category_id, name, location, st_address, city, state, zip, rating) VALUES
(3, 'Ca Hospital Medical Center', ST_GeomFromText('POINT(-118.266208 34.038906)' , 4326), '1338 S Hope St', 'Los Angles', 'California', '90015', 4)
;
INSERT into public_places 
(category_id, name, location, st_address, city, state, zip, rating) VALUES
(3, 'Los Angeles Center for Women Health', ST_GeomFromText('POINT(-118.266508 34.037519)' , 4326), '1513 S Grand Ave #400', 'Los Angles', 'California', '90015', 4)
;
INSERT into public_places 
(category_id, name, location, st_address, city, state, zip, rating) VALUES
(3, 'Orthopaedic Institute for Children', ST_GeomFromText('POINT(-118.273375 34.028770)' , 4326), '403 W Adams Blvd', 'Los Angles', 'California', '90007', 4)
;

UPDATE public_places
SET st_address = '3670 Trousdale Pkwy'
where id=4

SELECT ST_AsText(location) 
       FROM public_places;