import cookielib
import os

import quizduell


class Scraper:
    def __init__(self, username, password):
        cookie_jar = cookielib.MozillaCookieJar('cookie_file')
        self.api = quizduell.QuizduellApi(cookie_jar)

        if os.access(cookie_jar.filename, os.F_OK):
            cookie_jar.load()
        else:
            self.api.login_user(username, password)

        cookie_jar.save()
        result = self.api.top_list_rating()

        if 'access' in result:
            # Session invalid, re-login:
            self.api.login_user('name', 'password')

    def give_up_all(self):
        curr_games = self.api.current_user_games()
        for game in curr_games['user']['games']:
            self.api.give_up(game['game_id'])

    def fetch_game(self):
        new_game = self.api.start_random_game()['game']
        result = new_game['questions']
        self.api.give_up(new_game['game_id'])
        return result
