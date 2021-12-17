from chatterbot  import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
my_bot = ChatBot(name='PyBot', read_only=True,
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'])
small_talk = ['Привет',
              'Привет!',
              'Как ты?',
              'Как дела?',
              'Все хорошо.',
              'Хорошо, а у тебя?',
              'Как всегда классно)',
              'Отлично)',
              'Это здорово.',
              'у меня все хорошо',
              'я рад слышать это.',
              'Я чувствую себя отлично',
              'Супер, это хорошие новости.',
              'Нехорошо',
              'Мне жаль слышать это.',
              'Как тебя зовут?',
              'Я умный чат-бот. Задай мне вопрос, я помогу!',
              'Плохо',
              'Мне жаль слышать это(',
              'Что делаешь?',
              'сижу, жду вопросы)']
second_talk = ['Что делаешь?',
               'Сижу, жду вопросы)']

list_trainer = ListTrainer(my_bot)
for item in (small_talk,second_talk):
    list_trainer.train(item)
corpus_trainer=ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.russian')

while True:
    try:
        bot_input=input('you: ')
        bot_response=my_bot.get_response(bot_input)
        print(bot_response)
    except(KeyboardInterrupt,EOFError,SystemExit):
        break;

