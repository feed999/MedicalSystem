from fastapi import HTTPException, status

UserAlreadyExistsException =HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail={"status":409,"message":"Пользователь уже существует"}
)
UserEmailAlreadyExistsException =HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail={"status":409,"message":"Пользователь с таким email уже существует"}
)
UserPhonelreadyExistsException =HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail={"status":409,"message":"Пользователь с таким номером телефона уже существует"}
)
# Exception for Users
IncorrectEmailException =HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail={"status":401,"message":"Неверная Почта"})
IncorrectPasswordException =HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail={"status":401,"message":"Неверный Пароль"})
IncorrectPhoneException =HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail={"status":401,"message":"Неверный Номер телефона"})
IncorrectFirstNameException =HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail={"status":401,"message":"Неверное Имя"})
IncorrectLastNameException =HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail={"status":401,"message":"Неверная Фамилия"})


TokenAbsentException =HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail={"status":401,"message":"Необходимо авторизоваться"})

TokenAbsentAdminException =HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Необходимо авторизоваться")

TokenExpiredException =HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail={"status":401,"message":"Время сеанса истекло"})
TokenAdminException =HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail={"status":401,"message":"У вас нет прав"})
# Exception for Documents 
IncorrectExistsException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail={"status":401,"message":"У вас уже заполнены документы"})
IncorrectNotExistsException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail={"status":401,"message":"У вас не заполнены документы"})
IncorrectPassportException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail={"status":401,"message":"Неверный Паспорт"})
IncorrectSnilsException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail={"status":401,"message":"Неверный СНИЛС"})
IncorrectPolisException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail={"status":401,"message":"Неверная Полис"})

IncorrectAddException= HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail={"status":401,"message":"Неудалось добавить документы"})
#Exception for appointment
AppointmentCannotBeRegister = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail={"status":401,"message":"В данное время уже есть запись"})


#Exception for record
AppointmentCannotBeRegister = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="В данное время уже есть запись")

RecordCannotBeRegister = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Не удалост добавить в истории записей")

