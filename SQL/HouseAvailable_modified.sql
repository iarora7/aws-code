drop table if exists house_available;
CREATE TABLE house_available (
   id SERIAL PRIMARY KEY,
   user_id bigint REFERENCES user_profile(id),
   st_address CHAR(100),
   apt_no INT,
   city CHAR(100),
   state CHAR(100),
   zip INT,
   spots INT,
   price FLOAT,
   start_date DATE,
   end_date DATE,
   title TEXT,
   description TEXT,
   phone_number CHAR(12),
   available boolean,
   location GEOMETRY(POINT,4326)
);


INSERT INTO public.house_available(
        user_id, st_address, apt_no, city, state, zip, spots, price, 
        start_date, end_date, title, description, phone_number, available, location)
VALUES (1349781218406667, '2658 Menlo Ave', 2, 'Los Angeles', 'California', '90007', 2, 2700.00,
     '2017-04-01', '2017-06-01', 'This is Shivaliks house', 'This is a mnasion at Menlo', 4086007283, true, ST_GeomFromText('POINT(-118.289951 34.031096)' , 4326)),
      (1349781218406667, '2138 Oak St', NULL, 'Los Angeles', 'California', '90007', 2, 2700.00,
       '2017-04-01', '2017-06-01', 'This is Ishas house', '2 BHK at Oak', 4086007283, true, ST_GeomFromText('POINT(-118.279622 34.033707)' , 4326)),
      (1349781218406667, '2827 Orchard Ave', 5, 'Los Angeles', 'California', '90007', 2, 2700.00,
       '2017-04-01', '2017-06-01', 'This is Sindhus house', 'Nearest to Campus', 4086007283, true, ST_GeomFromText('POINT(-118.287419 34.029367)' , 4326)),
      (1349781218406667, '2656 Ellendale Place', 6, 'Los Angeles', 'California', '90007', 2, 2700.00,
       '2017-04-01', '2017-06-01', 'This is Patros house', 'Kahani ghar ghar ki', 4086007283, true, ST_GeomFromText('POINT(-118.288293 34.031053)' , 4326));

INSERT INTO public.house_available(
        user_id, st_address, apt_no, city, state, zip, spots, price,
        start_date, end_date, title, description, phone_number, available, location)
VALUES (1349781218406667, 'Lorenzo 325 W Adams Blvd', '', 'Los Angeles', 'California', '90007', 5, 1700.00,
     '2017-04-01', '2017-06-01', 'The Lorenzo', 'Superior Living', 4086007283, true, ST_GeomFromText('POINT(-118.272978 34.027631)' , 4326))
     returning id;