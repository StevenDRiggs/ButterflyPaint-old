from flask_seeder import Seeder, Faker, generator

from bpaint.model import *


class UserSeeder(Seeder):
    def run(self):
        faker = Faker(
                cls=User,
                init={
                    'id': generator.Sequence(),
                    'name': generator.String('\c{15}'),
                    'email': generator.String('\c{6}@email.com'),
                    'password': generator.String('password'),
                }
        )

        for user in faker.create(10):
            print(f'Adding user {user.name}.')
            self.db.session.add(user)

class ColorSeeder(Seeder):
    def run(self):
        faker = Faker(
                cls=Color,
                init={
                    'id': generator.Sequence(),
                    'name': generator.String('\c{15}'),
                    'manufacturer': generator.String('\c{15}'),
                    'image_url': generator.String('\c{5,7}.\c{3}/\c{3,4}'),
                }
        )

        for color in faker.create(10):
            print(f'Adding color {color.name}.')
            self.db.session.add(color)

class RecipeSeeder(Seeder):
    def run(self):
        faker = Faker(
                cls=Recipe,
                init={
                    'id': generator.Sequence(),
                    'parent_color_id': generator.Integer(1,10),
                    'ingredient_color_id': generator.Integer(1,10),
                    'quantity': generator.Integer(1,4),
                }
        )

        for i, recipe in enumerate(faker.create(10)):
            print(f'Adding recipe {i}.')
            self.db.session.add(recipe)

class InventorySeeder(Seeder):
    def run(self):
        faker = Faker(
                cls=Inventory,
                init={
                    'id': generator.Sequence(),
                    'color_id': generator.Integer(1,10),
                    'in_stock': generator.Integer(1,5),
                    'minimum_stock': generator.Integer(-1,8),
                }
        )

        for i, inv in enumerate(faker.create(10)):
            print(f'Adding inv {i}.')
            self.db.session.add(inv)
