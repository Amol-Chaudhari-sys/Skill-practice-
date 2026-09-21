use amoldb ;
drop table if exists addreses;

create table addresses (
id int auto_increment primary key ,
user_id int ,
streat varchar(100),
city varchar(100),
state varchar(100),
pincode int ,
constraint fk_user foreign key (user_id) references users(id) on delete cascade 
);

insert into addresses (user_id , streat, city,state,pincode) values 
(1, 'thane' , 'thene' , 'mahareshtra',412345),
(2, 'swargate' , 'pune' , 'mahareshtra',412345),
(3, 'wada' , 'thene' , 'mahareshtra',412765),
(4, 'hadapser' , 'pune' , 'mahareshtra',562345),
(5, 'kalyan' , 'thene' , 'mahareshtra',412396);

select * from addresses ;
select * from users;
select users.name ,addresses.city ,addresses.state from users inner join addresses on users.id = addresses.user_id;
select users.name ,addresses.city ,addresses.state from users left join addresses on users.id = addresses.user_id;
select users.name ,addresses.city ,addresses.state from users right join addresses on users.id = addresses.user_id;

select* from users left join addresses on users.id = addresses.user_id;