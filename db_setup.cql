create keyspace smartflaskks with replication  = {'class': 'SimpleStrategy', 'replication_factor': '1' };
use smartflask_ks;

create table student(
id text,
full_name text,
email text,
birth_date date,
number_of_courses int,
PRIMARY KEY((id)));

insert into student (id, full_name, email, birth_date, number_of_courses)
    values('AXS_001', 'Alessio Saltarin', 'alessiosaltarin@smartflask.com', '2001-08-26', 5);
insert into student (id, full_name, email, birth_date, number_of_courses)
    values('AXS_002', 'Elena Zambrelli', 'elenazambrelli@smartflask.com', '2005-06-12', 3);
insert into student (id, full_name, email, birth_date, number_of_courses)
    values('AXS_003', 'Giacomo Filippi', 'giacomofilippi@smartflask.com', '2004-10-22', 2);
insert into student (id, full_name, email, birth_date, number_of_courses)
    values('AXS_004', 'Giuliana Pini', 'giulianapini@smartflask.com', '2005-12-12', 1);
insert into student (id, full_name, email, birth_date, number_of_courses)
    values('AXS_005', 'Cristina Zunin', 'cristinazunin@smartflask.com', '2003-11-03', 3);
insert into student (id, full_name, email, birth_date, number_of_courses)
    values('AXS_006', 'Daniela Sandu', 'danasandu@smartflask.com', '2002-01-20', 4);
