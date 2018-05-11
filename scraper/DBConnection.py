import sqlite3


class DBConnection:
    def __init__(self, filename):
        self.conn = sqlite3.connect(filename)
        self.create_db_if_not_exist()

    def add_question(self, questions):
        quest_list = []

        for quest in questions:
            quest_list.append(tuple((quest['q_id'], quest['cat_id'], quest['question'], quest['timestamp'],
                                     quest['correct'], quest['wrong1'], quest['wrong2'], quest['wrong3'],
                                     quest['stats']['wrong1_answer_percent'], quest['stats']['wrong2_answer_percent'],
                                     quest['stats']['wrong3_answer_percent'],
                                     quest['stats']['correct_answer_percent'])))

        command = 'INSERT OR IGNORE INTO question (ID, category, question, timestamp, correct, wrong1, wrong2, wrong3, ' \
                  'wrong1_answer_percent, wrong2_answer_percent, wrong3_answer_percent, correct_answer_percent) ' \
                  'VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'

        cursor = self.conn.cursor()

        cursor.executemany(command, quest_list)

        cursor.close()

    def commit(self):
        self.conn.commit()

    def count_questions(self):
        command = 'SELECT COUNT(ID) FROM question;'
        cursor = self.conn.cursor()
        cursor.execute(command)
        return cursor.fetchone()[0]

    def create_db_if_not_exist(self):
        command_category = 'CREATE TABLE IF NOT EXISTS\"category\" (`ID` INTEGER, `Name` TEXT NOT NULL, PRIMARY KEY(' \
                           '`ID`)) '
        command_question = 'CREATE TABLE IF NOT EXISTS `question` (`ID` INTEGER, `category` INTEGER, `question` TEXT,' \
                           ' `timestamp` TEXT, `correct` TEXT, `wrong1` TEXT, `wrong2` TEXT, `wrong3` TEXT, ' \
                           '`wrong1_answer_percent` INTEGER, `wrong2_answer_percent` INTEGER, `wrong3_answer_percent`' \
                           ' INTEGER, `correct_answer_percent` INTEGER, PRIMARY KEY(`ID`)) '
        cursor = self.conn.cursor()
        cursor.execute(command_category)
        cursor.execute(command_question)
        cursor.close()
