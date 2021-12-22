from tinydb import TinyDB, Query

db = TinyDB('db.json')


class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age


player = Player(name='John', age=22)
serialized_player = {
    'name': player.name,
    'age': player.age
}

players_table = db.table('player')
players_table.truncate()  # clear the table first
players_table.insert(serialized_player)





