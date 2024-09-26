def is_correct_password(password: str):
    if len(password)<8:
        return False
    return True
    
def is_correct_email(email: str):
    if '@' not in email:
        return False
    if '.' not in email.split('@')[1]:
        return False
    return True

def is_correct_name(name: str):
    if len(name)<3:
        return False
    return True

def is_correct_phone(phone: str):
    if len(phone)!=11:
        return False
    if not phone.isalnum():
        return False
    return True