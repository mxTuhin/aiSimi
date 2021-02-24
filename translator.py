from googletrans import Translator
translator = Translator()
print(translator.translate('Nola zaude Simi?',src='auto', dest='bn').text)