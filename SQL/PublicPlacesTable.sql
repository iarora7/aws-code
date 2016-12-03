
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

INSERT into public_places
(category_id, name, location, st_address, city, state, zip, rating) VALUES
(4, 'Green Dot Public Schools', ST_GeomFromText('POINT(-118.261197 34.040648)' , 4326), '1149 Hill S', 'Los Angles', 'California', '90015', 3)
;

INSERT into public_places
(category_id, name, location, st_address, city, state, zip, rating) VALUES
(2, 'With Love Market & Cafe', ST_GeomFromText('POINT(-118.291839 34.040003)' , 4326), '1969 S Vermont Ave', 'Los Angles', 'California', '90007', 4)
;

INSERT into public_places
(category_id, name, location, st_address, city, state, zip, rating) VALUES
(2, 'Ralphs', ST_GeomFromText('POINT(-118.291152 34.033246)' , 4326), '2600 S Vermont Ave', 'Los Angles', 'California', '90007', 4)
;

INSERT into public_places
(category_id, name, location, st_address, city, state, zip, rating) VALUES
(2, 'Superior Grocers', ST_GeomFromText('POINT(-118.251499 34.023856)' , 4326), '2000 S Central Ave', 'Los Angles', 'California', '90011', 4)
;

INSERT into public_places
(category_id, name, location, st_address, city, state, zip, rating) VALUES
(1, 'Lyon Center', ST_GeomFromText('POINT(-118.288335 34.025349)' , 4326), '1026 W 34th St', 'Los Angles', 'California', '90089', 4)
;

INSERT into public_places
(category_id, name, location, st_address, city, state, zip, rating) VALUES
(1, 'City of Angels Boxing', ST_GeomFromText('POINT(-118.272671 34.023073)' , 4326), '3000 Hill St', 'Los Angles', 'California', '90007', 4)
;

INSERT into public_places
(category_id, name, location, st_address, city, state, zip, rating) VALUES
(1, 'Planet Fitness', ST_GeomFromText('POINT(-118.252114 34.025563)' , 4326), '1000 E Washington Blvd', 'Los Angles', 'California', '90021', 4)
;




UPDATE public_places
SET st_address = '3670 Trousdale Pkwy'
where id=4

SELECT ST_AsText(location)
       FROM public_places;