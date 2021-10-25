from pyowm import OWM
import telebot
from pyowm.utils import config as cfg #for change language 

config = cfg.get_default_config()
config['language'] = 'ru' # write language 

owm = OWM('')  #Take if from https://openweathermap.org/
bot = telebot.TeleBot("", parse_mode=None) #Take it from BotFather in telegram

@bot.message_handler(content_types=['text'])

def start(message):
    
    if message.text == '/start' :
        bot.send_message(message.from_user.id, "Привет,я Бот Максим.\nПомогу тебе с прогнозом погоды.\nВведи интересующий тебя город) ");
        bot.register_next_step_handler(message, goodplace); #ловим место поиска
        
    else:
        bot.send_message(message.from_user.id, 'Запусти бота командой /start ');
        
def goodplace(message):
                
    while 1==1:
        try:             
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(message.text)
            w = observation.weather
            
            temp = w.temperature('celsius')["temp_max"]
            wind = w.wind()["speed"]

            answer = "В городе " + message.text + " сейчас " + str(w.detailed_status) + "\n"
            answer += "Температура составляет: " + str(temp) +"°" "\n"
            answer += "Скорость ветра составляет: " + str(wind) + " м\\c"+ "\n\n"
            if temp > 20:
                answer +=("Одевайся легко.")

            elif temp <-10:
                answer +=("Ты видел этот холод!? \nОдевай все что есть дома!")

            else:
                answer +=("Одевайся теплее:3")

        except:
            answer = "Извини, я не знаю такого города."                                                                                                                                                              
                                
        bot.send_message(message.chat.id, answer)
        bot.register_next_step_handler(message, goodplace);
                   
        break

bot.polling( none_stop = True )
