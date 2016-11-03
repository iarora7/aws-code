--create a user_profile table

 drop table if exists user_profile;
 CREATE TABLE user_profile (
 	id BIGINT PRIMARY KEY,
 	full_name CHAR(100),
 	first_name CHAR(50),
 	last_name CHAR(50),
 	phone_number CHAR(12),
 	email CHAR(100)
 );


--insert a sample row in the user_profile table

INSERT INTO user_profile (id, full_name, first_name, last_name, phone_number, email)
VALUES ('111222', 'S N', 'S', 'N', '4444444444', 'sn@gmail.com');
COMMIT;
