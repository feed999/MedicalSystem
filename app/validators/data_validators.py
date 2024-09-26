def is_correct_passport(passport: str):
    if not '-' in passport:
        return False
    if len(passport.split('-')[0])!=4 or not passport.split('-')[0].isalnum():
        return False
    if len(passport.split('-')[1])!=6 or not passport.split('-')[1].isalnum():
        return False
    return True

def is_correct_snils(snils: str):
    if len(snils)<12:
        return False
    return True

def is_correct_polis(polis: str):
    if len(polis)!=16 or not polis.isalnum():
        return
    return True
