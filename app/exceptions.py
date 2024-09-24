from fastapi import HTTPException, status

UserAlreadyExistsException =HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Пользователь уже существует"
)
UserEmailAlreadyExistsException =HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Пользователь с таким email уже существует"
)
UserPhonelreadyExistsException =HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Пользователь с таким номером телефона уже существует"
)
# Exception for Users
IncorrectEmailException =HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверная Почта")
IncorrectPasswordException =HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверный Пароль")
IncorrectPhoneException =HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверный Номер телефона")
IncorrectFirstNameException =HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверное Имя")
IncorrectLastNameException =HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверная Фамилия")

# Exception for Token
TokenAbsentException =HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Необходимо авторизоваться")
TokenExpiredException =HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Время сеанса истекло")
TokenAdminException =HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="У вас нет прав")
# Exception for Documents 
IncorrectExistsException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="У вас уже заполнены документы")
IncorrectNotExistsException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="У вас не заполнены документы")
IncorrectPassportException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверный Паспорт")
IncorrectSnilsException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверный СНИЛС")
IncorrectPolisException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверная Полис")

IncorrectAddException= HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неудалось добавить документы")
#Exception for appointment
AppointmentCannotBeRegister = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="В данное время уже есть запись")


#Exception for record
AppointmentCannotBeRegister = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="В данное время уже есть запись")

RecordCannotBeRegister = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Не удалост добавить в истории записей")

