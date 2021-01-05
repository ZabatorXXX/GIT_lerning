''' Super simple module to create basic random data for tutorials'''
import random

first_names = ['Iscah', 'Mirko', 'Parker', 'Edwyn', 'Octavia']

last_names = ['Kohar', 'Somhairle', 'Ellie', 'Joanne', 'Silvanus']

street_names = ['Fox Way', 'Star Way', 'Milky Way', 'Greenfield Lane', 'Gravel Lane', 'Dirt Lane']

road_type = ['Avenue', 'Bay', 'Campus', 'Street'] 

cities = ['Istanbul', 'Moscow', 'London', 'Berlin', 'Warsaw', 'Łódź', 'Zagreb', 'Nice']

fake_states = ['XL', 'GI', 'AL', 'FI', 'AD', 'ML', 'OX', 'EC']

mail_type = ['Gmail', 'Yahoo', 'Hotmail', 'Outlook', 'iCloud', 'Mozilla', 'Mail']

mail_code = ['.se', '.com', '.az', '.eu', '.net', '.dk', '.uk']

for num in range(15):
    first = random.choice(first_names)
    last = random.choice(last_names)

    phone = f'{random.randint(100, 999)}-555-{random.randint(1000,9999)}'

    street_num = random.randint(100, 999)
    street = random.choice(street_names + road_type)
    city = random.choice(cities)
    state = random.choice(fake_states)
    zip_code = random.randint(10000, 99999)
    address = f'{street_num} {street} St., {city} {state} {zip_code}'
    
    mail = random.choice(mail_type)
    dot_code = random.choice(mail_code)

    email = first.lower() + last.lower() + '@' + mail.lower() + dot_code

    print(f'{first} {last}\n{phone}\n{address}\n{email}\n')
