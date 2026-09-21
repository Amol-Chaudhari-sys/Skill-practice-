use amoldb ;
CREATE TABLE admin_users (
id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    gender ENUM('Male', 'Female', 'Other'),
    date_of_birth DATE,
    salary INT
);

INSERT INTO admin_users (id, name, email, gender, date_of_birth, salary) VALUES
(101, 'Anil Kumar', 'anil@example.com', 'Male', '1985-04-12', 60000),
(102, 'Pooja Sharma', 'pooja@example.com', 'Female', '1992-09-20', 58000),
(103, 'Rakesh Yadav', 'rakesh@example.com', 'Male', '1989-11-05', 54000),
(104, 'Fatima Begum', 'fatima@example.com', 'Female', '1990-06-30', 62000);

select name from users 
union 
select name from admin_users;

select name , email ,"user" as role from users 
union 
select name ,email , "admin" as role from admin_users ;

alter table users add column reffer_by_id int;

update users set reffer_by_id = 1  where id in (1,3,5,7,9,11,13,15,17,19,21);
update users set reffer_by_id = 2 where id in (2,4,6);
select * from users ;

select a.name as user_name ,
b.name as reffer_by_id 
from users a left join users b on a.reffer_by_id = b.id ;

CREATE VIEW RICH_USERS AS 
SELECT * FROM USERS WHERE SALARY >70000;

SELECT * FROM RICH_USERS;

UPDATE USERS SET SALARY = 72000 WHERE ID = 3;

create index ind_gen_ind on users (gender  , salary );