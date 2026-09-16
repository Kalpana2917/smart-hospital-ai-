create table Patients( id varchar(10), name varchar(50), age int);
create table Doctors( id varchar(10), name varchar(50), patient_id varchar(10));
insert into Patients values('P1', 'Annu', 23);
insert into Patients values('P2', 'Sagun', 27);
insert into Doctors values('D01', 'Arvi', 'P1');
insert into Doctors values('D03', 'Zelda', 'P2');
select Patients.name as Patient, Doctors.name as Doctor
From Patients 
inner join Doctors on Paients.id=Doctors.patient_id;
