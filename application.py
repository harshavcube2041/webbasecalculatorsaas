from flask import Flask, request, render_template,jsonify
application = Flask(__name__)
def do_something(text1,text2):
    try:
        combine = int(text1) + int(text2)
        return combine
    except Exception as error:
        return str(error)
@application.route('/')
def home():
    return render_template('home.html')
@application.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    word = request.args.get('text1')
    text2 = request.form['text2']
    combine = do_something(text1,text2)
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0', port=5000)