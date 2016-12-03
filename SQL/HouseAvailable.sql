drop table if exists house_available;
CREATE TABLE house_available (
   id SERIAL PRIMARY KEY,
   st_address CHAR(100),
   apt_no INT,
   city CHAR(100),
   state CHAR(100),
   zip INT,
   spots INT,
   price FLOAT,
   start_date DATE,
   end_date DATE,
   summary TEXT,
   location TEXT
);


INSERT INTO house_available (st_address, apt_no, city, state, zip, spots, price, start_date, end_date, summary, location)
VALUES ('2658 Menlo Ave', 2, 'Los Angeles', 'California', '90007', 2, 2700.00, '2017-04-01', '2017-06-01', 'This is Shivaliks house', POINT(34.031096, -118.289951));



INSERT INTO house_available (st_address, apt_no, city, state, zip, spots, price, start_date, end_date, summary, location)
VALUES ('2658 Menlo Ave', 2, 'Los Angeles', 'California', '90007', 2, 2700.00, '2017-04-01', '2017-06-01', 'This is Shivaliks house', POINT(34.031096, -118.289951));


COMMIT;




INSERT INTO house_available (st_address, apt_no, city, state, zip, spots, price, start_date, end_date, summary, location)
VALUES ('2658 Menlo Ave', 2, 'Los Angeles', 'California', '90007', 2, 2700.00, '2017-04-01', '2017-06-01', 'This is Shivaliks house', 'POINT(34.031096 -118.289951)'),
('2787 Orchard Ave', 5, 'Los Angeles', 'California', '90007', 2, 2700.00, '2017-04-01', '2017-06-01', 'This is Sindhus house', 'POINT(34.029367 -118.287419)'),
('2138 Oak St', NULL, 'Los Angeles', 'California', '90007', 2, 2700.00, '2017-04-01', '2017-06-01', 'This is Ishas house', 'POINT(34.033707 -118.279622)'),
('2656 Ellendale Place', 6, 'Los Angeles', 'California', '90007', 2, 2700.00, '2017-04-01', '2017-06-01', 'This is Patros house', 'POINT(34.031053 -118.288293)');


INSERT INTO house_available (st_address, apt_no, city, state, zip, spots, price, start_date, end_date, summary, location)
VALUES ('1110 Hayne Rd', 2, 'Los Angeles', 'California', '90007', 2, 2700.00, '2017-04-01', '2017-06-01', 'This is Lals house', 'POINT(37.552982 -122.356191)'),


COMMIT;


SELECT *
FROM house_available
WHERE ST_WITHIN(location('POINT(34.031096, -118.289951)', 2000), location('POINT(34.031096, -118.289951)', 3000));


SELECT *
FROM house_available
WHERE ST_WITHIN ( 
                  ST_Buffer(ST_GeomFromText('POINT(34.031096 -118.289951)'), 4000), 
                  ST_Buffer(ST_GeomFromText('POINT(34.031096 -118.289951)'), 3000)
                 );

SELECT *
FROM house_available ha
WHERE ST_WITHIN ( 
                  ST_GeomFromText(ha.location), 
                  ST_Buffer(ST_GeomFromText('POINT(34.031096 -118.289951)'), 3000)
                 );

ALTER TABLE house_available ALTER COLUMN location TYPE TEXT;

address  in irvine 33.712409 -117.782568

SELECT *
FROM house_available
WHERE ST_WITHIN ( 
                  ST_GeomFromText('POINT(34.033707 -118.279622)'), 
                  ST_Buffer(ST_GeomFromText('POINT(34.031096 -118.289951)'), 482.8032)
                 );


// this is a working query to find the points that lie within the given circle
SELECT ha.location, ha.st_address
FROM house_available ha
WHERE ST_WITHIN ( 
                  ST_GeomFromText(ha.location), 
                  ST_Buffer(ST_GeomFromText('POINT(34.031096 -118.289951)'), 0.011)
                 );

ST_DWITHIN(
               ST_GeomFromText('POINT(34.031096 -118.289951)'),
               ST_GeomFromText(ha.location), 
               1000
            )



http://stackoverflow.com/questions/8444753/st-dwithin-takes-parameter-as-degree-not-meters-why



SELECT ha.location, ha.st_address
FROM house_available ha
WHERE ST_DWITHIN(
               ST_GeomFromText('POINT(34.031096 -118.289951)')::geography,
               ST_GeomFromText(ha.location), 
               200
            );


SELECT ha.location, ha.st_address
FROM house_available ha
WHERE ST_DWITHIN(
               ST_GeomFromText('POINT(34.031096 -118.289951)')::geography,
               ST_GeomFromText(ha.location), 
               500000
            );



https://www.youtube.com/watch?v=1HgM_vc-rSc  alvarez