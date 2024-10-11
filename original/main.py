from flask import Flask, render_template, request

app = Flask(__name__)

def result_calculate(size, lights, device):
    #Переменные для энергозатратности приборов
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

#Приветствие
@app.route('/')
def welcome():
    return render_template('index_welcome.html')

#Главная страница
@app.route('/home')
def home():
    return render_template('home.html')

#Код калькулятора
@app.route('/calculator')
def index():
    return render_template('index.html')
#Вторая страница
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

#Третья страница
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

#Расчет
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )

#Конец кода калькулятора

#Код для главной страницы статей
@app.route('/articles')
def articles():
    return render_template('science_main.html')

#Код страницы для детей
@app.route('/for_kids')
def for_kids():
    return render_template('for_kids.html')

app.run(debug=True)
