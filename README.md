# Quizduell Scraper

Being stupid sucks.
As I recently started playing quizduell, I realized, that I often had no chance against my friends. To improve my odds, I created this project. The goal of this project is, to create a rather complete database of all quizduell questions with answers and additional metadata.

**DISCLAIMER**: I never used this project to actually cheat. This is rather a interesting research project.

## How to use

The scraper can be started from the commandline.

```commandline
python . username password [--db Database.sqlite]
```

## How it works
During my research, I found out, that quizduell sends all possible questions and answers right after starting a match. Therefore, we can persist the required data and immediately give up.

This allows us to receive a huge amount of data without having to wait for our opponent to play.

## Credit
- quizduellapi by [mtschirs](https://github.com/mtschirs/): In this project, I use my own fork of the library, which can be found [here](https://github.com/beatbrot/quizduellapi). The library is licensed under GPLv3
- [PyCharm](https://www.jetbrains.com/pycharm/) by Jetbrains: A great, free and open source IDE.