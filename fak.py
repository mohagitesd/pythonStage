from faker import Faker
fake = Faker("fr_FR")

for i in range(10):
    print(fake.date_this_month().isoformat())
    print(fake.company())
    print(fake.url())
    print(fake.job())
    print("-"*10)

