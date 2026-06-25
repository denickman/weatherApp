from flask import Flask, render_template


'''
Папка templates — обязательна
Да, это стандартное условие Flask.
Flask ищет HTML файлы по умолчанию в папке templates/:
'''


'''
# Flask('Website') = создаёшь новое приложение Flask

Результат: объект app который может:
- Слушать на порту
- Обрабатывать запросы
- Маршрутизировать URL
'''
app = Flask(__name__)


'''
Когда кто-то откроет:
 @app.route('/home') - "слушай URL /home"
 
http://localhost:5000/home
        ↓
Flask видит /home
        ↓
Смотрит: "Есть ли @app.route('/home')?"
        ↓
Находит эту функцию: def home()
        ↓
Вызывает функцию
'''

@app.route('/')          # ← ДЕКОРАТОР
def home_page():     # ← ФУНКЦИЯ
    return render_template('home.html') # обязательно должна быть в папке templates


@app.route('/api/v1/<station>/<date>')
def about_page(station, date):
    # df = pandas.read_csv('data/' + station + '/' + date + '.csv')
    # temperature = df.station(date)

    temperature = 23
    # return str(temperature)  #render_template('about.html')
    return {
        'station': station,
        'date': date,
        'temperature': temperature
    }

if __name__ == '__main__':
    app.run(debug=True, port=5001)