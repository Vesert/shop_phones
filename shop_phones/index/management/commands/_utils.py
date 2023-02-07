from faker import Faker


def generate_fake_phones():
    faker = Faker()
    Faker.seed(0)
    def gen():
        brand = faker.random_choices(elements=('Xiaomi', 'Iphone', 'Samsung'))
        model_identifier = faker.bothify(text = '?#')
        price = faker.random_number(digits=3,fix_len=True)
        is_sale_price = faker.pybool()

        return {'model_name':brand[0]+ ' '+ model_identifier,'price':price,'is_sale_price':is_sale_price}

    return gen