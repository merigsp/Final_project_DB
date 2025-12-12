
CREATE TABLE tournear(
  tur_id int primary key,
  date_ date,
  city varchar(20),
  country varchar(20),
  t_name varchar(20),
  qualification_level int
 
);

CREATE TABLE participance(
  tur_id int references tournear(tur_id),
  part_id int primary key,
  start_number int,
  zanyatoye_mesto int
 
);


CREATE TABLE player(
  p_id int primary key,
  par_id int references participance(part_id),
  second_name varchar(20),
  country varchar(20),
  titul varchar(10),
  rating int
);


