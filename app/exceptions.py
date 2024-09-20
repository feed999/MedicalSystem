from fastapi import HTTPException, status

UserAlreadyExistsException =HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Пользователь уже существует"
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
IncorrectPassportException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверный Паспорт")
IncorrectSnilsException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверный СНИЛ")
IncorrectPolisException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверная Полис")



