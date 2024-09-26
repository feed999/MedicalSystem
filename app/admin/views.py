from sqladmin import ModelView

from app.appointments.models import Appointments
from app.doctors.models import Doctors
from app.documents.models import Documents
from app.records.models import Records
from app.roles.models import Roles
from app.rooms.models import Rooms
from app.timetables.models import Timetables
from app.users.models import Users


class RolesAdmin(ModelView,model=Roles):
    column_list = [Roles.id,Roles.role,Roles.user]
    name = "Роль"
    name_plural = "Роли"
class RoomsAdmin(ModelView,model=Rooms):
    column_list = [Rooms.id,Rooms.name,Rooms.floor,Rooms.doctor]
    name = "Кабинет"
    name_plural = "Кабинеты"
class DocumentsAdmin(ModelView,model=Documents):
    column_list = [Documents.id,Documents.user]
    name = "Документы"
    name_plural = "Документы"
class UsersAdmin(ModelView,model=Users):
    column_list = [Users.id,Users.email,Users.user_role]
    name = "Пользователь"
    name_plural = "Пользователи"
    page_size = 25
class DoctorsAdmin(ModelView,model=Doctors):
    column_list = [Doctors.id,Doctors.user,Doctors.room,Doctors.specialization,Doctors.years_of_experience,Doctors.about]
    name = "Доктор"
    name_plural = "Доктора"
    page_size = 25
class TimetablesAdmin(ModelView,model=Timetables):
    column_list = [Timetables.id,Timetables.doctor,Timetables.monday,Timetables.tuesday,Timetables.wednesday,Timetables.thursday,Timetables.friday]
    name = "Расписание"
    name_plural = "Расписание Докторов"
    page_size = 25
class AppointmentsAdmin(ModelView,model=Appointments):
    column_list = [Appointments.id,Appointments.user,Appointments.doctor,Appointments.appointment_date,Appointments.date_regist]
    name = "Запись на прием"
    name_plural = "Записи на прием"
    page_size = 25
class RecordsAdmin(ModelView,model=Records):
    column_list = [Records.id,Records.user,Records.doctor,Records.appointment_date,Records.date_regist]
    name = "История"
    name_plural = "История записей"
    page_size = 25
    