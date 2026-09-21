CREATE DATABASE AMOLDB ;
USE AMOLDB;

	CREATE TABLE USERS (
    ID INT auto_increment primary KEY ,
    NAME VARCHAR(100) NOT NULL , 
    EMAIL VARCHAR (100) unique NOT NULL, 
    GENDER enum( 'Male' , 'female' , 'other' ),
    DATE_OF_BIRTH DATE , 
    CREATE_DATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
    );
    
SELECT * FROM USERS ;

select NAME , EMAIL from users;
RENAME TABLE  USERS TO CUSTOMERS ;
RENAME TABLE CUSTOMERS TO USERS ;

ALTER TABLE USERS ADD COLUMN IS_ACTIVE BOOLEAN DEFAULT TRUE ;
ALTER TABLE USERS DROP COLUMN IS_ACTIVE ;

ALTER TABLE USERS modify COLUMN  EMAIL VARCHAR (100) AFTER ID ;

insert into users values (1 , 'amol@gmail.com', 'amol', 'male', '2020-06-09' , default );
alter table users add column salary decimal(10 , 2) after date_of_birth;


alter table users modify column name varchar(100) after id ;