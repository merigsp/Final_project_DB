
CREATE TABLE tournear(
  tur_id SERIAL primary key,
  date DATE not null,
  city varchar(20) not null,
  country varchar(20) not null,
  t_name varchar(20) not null,
  qualification_level INT not null
);

CREATE TABLE participance(
  tur_id INT references tournear(tur_id),
  part_id SERIAL primary key,
  start_number INT not null,
  zanyatoye_mesto INT not null
);

CREATE TABLE player(
  p_id SERIAL primary key,
  par_id INT references participance(part_id),
  second_name varchar(20) not null,
  country varchar(20) not null,
  titul varchar(10) not null,
  rating int not null
);
