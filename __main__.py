# Load authenticated session from file to prevent unnecessary logins:

from scraper.DBConnection import DBConnection
from scraper.Scraper import Scraper
import argparse

parser = argparse.ArgumentParser(description='Fetch questions with solutions from Quizduell Germany')
parser.add_argument('username', type=str, help='The username of the quizduell account')
parser.add_argument('password', type=str, help='The password of the quizduell account')

parser.add_argument('--db', metavar='--db', type=str, help='Path to the sqlite database', dest='db_file',
                    default='Quizduell.sqlite', required=False)

args = parser.parse_args()

scraper = Scraper(args.username, args.password)
connection = DBConnection(args.db_file)

while True:
    for i in range(0, 10):
        if i == 0:
            scraper.give_up_all()
            connection.commit()
            print(connection.count_questions())
        game = scraper.fetch_game()
        connection.add_question(game)
