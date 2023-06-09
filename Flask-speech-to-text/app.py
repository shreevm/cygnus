import speech_recognition as sr
from flask import logging, Flask, render_template, request, flash


app = Flask(__name__)
app.secret_key = "cygnus"


@app.route('/')
def index():
    flash("Welcome to Cygnus Survey")
    return render_template('index.html')

@app.route('/audio_to_text/')
def audio_to_text():
    flash(" Press Start to start recording audio and press Stop to end recording audio")
    return render_template('audio_to_text.html')
    

@app.route('/audio', methods=['POST'])
def audio():
    r = sr.Recognizer()
    with open('upload/audio.wav', 'wb') as f:
        f.write(request.data)
    
    with sr.AudioFile('upload/audio.wav') as source:
        audio_data = r.record(source)
        lang= str(request.form.get("lang"))
        print(lang)
        if lang =='Tamil':
                    text = r.recognize_google(audio_data, language='ta-IN', show_all=False)
                    return str(text)
        if lang =='English':
                    text = r.recognize_google(audio_data, language='en-US', show_all=False)
                    return str(text)
        text = r.recognize_google(audio_data, language='ta-IN', show_all=False)

        #text = r.recognize_google(audio_data, language='en-US', show_all=False)
        print(text)
        return_text = "  Did you say : <br> "
    ''' try:



            for num, texts in enumerate(text['alternative']):
                return_text += str(num+1) +") " + texts['transcript']  + " <br> "
        except:
            return_text = " Sorry!!!! Voice not Detected " '''
    
    return str(text)


if __name__ == "__main__":
    app.run(debug=True)
