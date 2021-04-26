#Program to calculate age of a person
import datetime


def calculateAge(dob):
    '''Calulate's a person age'''
    today = datetime.date.today()
    age = today.year - dob.year
    return age


def checkDate(dob):
    '''Checks if date is valid or not'''
    day,month,year = dob.split('/')
    isvaliddate = True

    try:
        datetime.datetime(int(year),int(month),int(day))
    except ValueError:
        isvaliddate = False

    return isvaliddate


if __name__ == "__main__":
    dob = input('Enter Date of birth in dd/mm/yyyy format:')
    isdatevalid = checkDate(dob)
    if isdatevalid:
        dt = datetime.datetime.strptime(dob,"%d/%m/%Y")
        print('Age={} years'.format(calculateAge(dt)))
    else:
        print('Invalid date entered')

