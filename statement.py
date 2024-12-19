from datetime import datetime


def verification_password(password):
    if len(password) < 8 :
        print("Le mot de passe doit contenir au moins 8 caractères.")

    elif password!='Jesuisespuissant':
        print('Le mot de passe est incorrect')
    else:
        print('bon mot de passe.')


def leap_year(year):
    if( year%400==0) or ((year % 4==0) and (year % 100!=0)):
        print(f'{year} est une année bissextile.')
    else:
        print(f'{year} n\'est pas une année bissextile.')

def year_count(year):
    pass_year = year
    while year<2025:
        year += 1
        print(year,"old: ",year - pass_year)

def piramid_triangle(n):
    letters=''
    i=0

    for element in n:
        i+=1
        letters= '*' * i
        print(letters)

if __name__ == '__main__':
    verification_password('Jesuisespuissant')
    leap_year(2020)
    piramid_triangle("Bonjour les ZER0S")