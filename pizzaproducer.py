import json
from kafka import KafkaProducer
from faker import Faker
import random
from faker.providers import BaseProvider

class PizzaProvider(BaseProvider):
    def pizza_name(self):
        validPizzaNames= ['Margherita',
                          'Marinara',
                          'Diavola',
                          'Mari & Monti',
                          'Salami',
                          'Pepperoni'
                        ]
        return validPizzaNames[random.randint(0,len(validPizzaNames)-1)]

    def pizza_shop(self):
        pizza_shops = [
            'Marios Pizza',
            'Luigis Pizza',
            'Circular Pi Pizzeria',
            'Ill Make You a Pizza You Can''t Refuse',
            'Mammamia Pizza',
            'Its-a me! Mario Pizza!'
        ]
        return random.choice(pizza_shops)

    def pizza_topping(self):
        available_pizza_toppings = [
            '🍅 tomato',
            '🧀 blue cheese',
            '🥚 egg',
            '🫑 green peppers',
            '🌶️ hot pepper',
            '🥓 bacon',
            '🫒 olives',
            '🧄 garlic',
            '🐟 tuna',
            '🧅 onion',
            '🍍 pineapple',
            '🍓 strawberry',
            '🍌 banana'
        ]
        return random.choice(available_pizza_toppings)
