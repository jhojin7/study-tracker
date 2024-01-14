-- drop table if exists submission;
create table if not exists submission (
	sid int primary key,
	uid varchar(100),
	pid int,
	result varchar(100),
	timestamp int,
	index time_idx (timestamp)
);
