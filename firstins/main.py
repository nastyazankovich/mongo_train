from mongoAPI import MongoDB
import faker
from faker import Faker

dbase = MongoDB(db_name='article', collection='user')
faker_obj = faker.Faker()

# fake = Faker('ru-Ru')
# name = fake.name()
# print(name)
# address = fake.address()
# print(address)
# phone_number = fake.phone_number()
# print(phone_number)
# email = fake.email()
# print(email)
# text = fake.text()
# print(text)
# random_number = fake.random_number()
# print(random_number)
# date = fake.date()
# print(date)
# user_profile = faker_obj.simple_profile()
# user_profile['birthdate'] = user_profile['birthdate'].strftime('%d/%m/%Y')
# print(user_profile)
# dbase.create_user(user_profile)
# result = dbase.get_all_users()
# for i in result:
#     print(i)
# print(dbase.find_by_userneme('Yana'))
# dbase.change_user('ramirezsharon', 'name', 'test')