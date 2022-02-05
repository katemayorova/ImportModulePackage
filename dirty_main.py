from application.people import *
from application.salary import *
from datetime import datetime

if __name__ == '__main__':
    print('Starting program at', datetime.today())
    print('--> main.py')
    calculate_salary()
    get_employees()
