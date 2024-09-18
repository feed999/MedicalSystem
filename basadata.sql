INSERT INTO users (first_name,last_name,email,phone,hashed_password,role) VALUES
('Сергей','Бурунов','burunov@gmail.com','89996743421','hj1240ashdo94',user_enum_type('PATIENT')),
('Агафон','Богданов','Bogdanov@gmail.com','89496246420','lkerlkqw234',user_enum_type('PATIENT')),
('Эрнест','Морозов','Morozov@gmail.com','89055777420','pqjkerphq09',user_enum_type('PATIENT')),
('Потап','Степанов','Stepanov@gmail.com','89546790523','jahsd798q041',user_enum_type('PATIENT')),
('Гордей','Кириллов','Kirillov@gmail.com','89966643423','aklsjdf29',user_enum_type('PATIENT')),
('Нина','Крылова','Krylova@gmail.com','89906048885','qpolk-1ihsrfq',user_enum_type('PATIENT')),
('Максим','Селиверстов','Seliverstov@gmail.com','89096546427','oiyutasjmne19',user_enum_type('PATIENT')),
('Емельян','Бобров','Bobrov@gmail.com','89906445420','qpowruiyqgor',user_enum_type('PATIENT')),

('Вадим','Доронин','burunov@gmail.com','89034446407','oiyutasjmne19',user_enum_type('DOCTOR')),
('Эммануил','Лобанов','burunov@gmail.com','89017286427','qworpqyur5',user_enum_type('DOCTOR')),
('Пелагея','Дроздова','burunov@gmail.com','89096548564','poqwrifaor',user_enum_type('DOCTOR')),
('Людмила','Мясникова','burunov@gmail.com','89098400925','nqwujrquwpo',user_enum_type('DOCTOR')),
('Тимофей','Чернов','burunov@gmail.com','89005563198','qpqwyruiahs',user_enum_type('DOCTOR')),

('Никита','Борзый','borziy1337@gmail.com','8977657742','qioprusamk4',user_enum_type('ADMIN'))


INSERT INTO documents (user_id,passport,snils,polis) VALUES
(1,'1111-667733','152-778-614 14','9748031728000001'),
(2,'4231-192458','191-182-519 28','5123721958000001'),
(3,'5232-859313','123-431-431 21','5707422788000001'),
(4,'5261-510315','102-183-125 11','5627151358000001'),
(5,'8673-590238','121-598-182 22','5927452758000001'),
(6,'1233-125935','175-581-218 12','9617857758000001'),
(7,'9832-593315','581-481-151 33','2647151730800001'),
(8,'9431-912321','128-941-741 12','5692431758000001'),
(9,'1942-826471','912-123-185 22','5627853758000001')


INSERT INTO rooms (name,floor,capacity) VALUES
('101',1,1),
('101а',1,1),
('102',1,1),
('103',1,1),
('104',1,1),
('104а',1,1),
('105',1,1),
('106',1,1),
('107',1,1)



INSERT INTO doctors (user_id,room_id,image_id,specialization) VALUES
(10,1,1,'Гинеколог'),
(11,4,1,'Ортопед'),
(12,6,1,'Педиатр'),
(13,3,1,'Психиатр'),
(14,2,1,'Стоматолог')

INSERT INTO timetables (doctor_id,available_from,available_to) VALUES
(1,'09:00','18:00'),
(2,'10:00','16:00'),
(3,'09:00','12:00'),
(4,'11:00','19:00'),
(5,'09:00','16:00')


