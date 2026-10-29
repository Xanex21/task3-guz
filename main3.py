from googletrans import Translator, LANGUAGES, LANGCODES

translator = Translator()

def CodeLang(lang):
    lang = lang.strip().lower()
    if lang in LANGCODES:
        return LANGCODES[lang]
    elif lang in LANGUAGES:
        return LANGUAGES[lang]
    else:
        return "Помилка: мову не знайдено"

def LangDetect(txt):
    result = translator.detect(txt)
    return result.lang, result.confidence


def TransLate(str, lang):
    lang = lang.strip().lower()
    if lang in LANGCODES:
        lang = LANGCODES[lang]
    if lang not in LANGUAGES:
        return "Помилка: мову не знайдено"
    try:
        result = translator.translate(str, dest=lang)
        return result.text
    except Exception as e:
        return "Помилка перекладу: " + str(e)


demo = "Сьогодні чудова погода, тому ми підемо гуляти до парку."
lang = "English"

print("Текст:", demo)
print("Мова тексту:", LangDetect(demo))
print("Код мови:", CodeLang(lang))
print("Переклад:", TransLate(demo, lang))