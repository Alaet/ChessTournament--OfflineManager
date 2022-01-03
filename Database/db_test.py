from tinydb import TinyDB

db_test = TinyDB('db_test.json', indent=4)
players_table_test = db_test.table('players')
tournament_table_test = db_test.table('tournaments')
