import stanza

stanza.download('en')
nlp = stanza.Pipeline(lang='en', processors='tokenize,ner')
def stanza_nlp(text):
    nlp = stanza.Pipeline(lang='en', processors='tokenize,ner')
    doc = nlp(text)
    print(*[f'entity: {ent.text}\ttype: {ent.type}' for sent in doc.sentences for ent in sent.ents], sep='\n')

english_text = '''I want a person available 7 days and with prompt response all most every time. Only Indian
freelancer need I need PHP developer who have strong experience in Laravel and Codeigniter framework for daily 4
hours. I need this work by Monday 27th Jan. should be free from plagiarism . Need SAP FICO consultant for support
project needs to be work on 6 months on FI AREAWe.  Want a same site to be created as the same as this
https://www.facebook.com/?ref=logo, please check the site before contacting to me and i want this site to be ready in
10 days. They will be ready at noon tomorrow . '''

stanza_nlp(english_text)
#
# russian_text = '''Власти Москвы выделили 110 млрд рублей на поддержку населения, системы здравоохранения и городского
# хозяйства. Об этом сообщается на сайте мэра столицы https://www.sobyanin.ru/ в пятницу, 1 мая. По адресу Алтуфьевское
# шоссе д.51 (основной вид разрешенного использования: производственная деятельность, склады) размещен МПЗ? Подпоручик
# Киже управляя автомобилем ВАЗ2107 перевозил автомат АК47 с целью ограбления банка ВТБ24, как следует из записей.
# Взыскать c индивидуального предпринимателя Иванова Костантипа Петровича дата рождения 10 января 1970 года,
# проживающего по адресу город Санкт-Петербург, ул. Крузенштерна, дом 5/1А 8 000 (восемь тысяч) рублей 00 копеек гос.
# пошлины в пользу бюджета РФ Жители требуют незамедлительной остановки МПЗ и его вывода из района. Решение было
# принято по поручению мэра города Сергея Собянина в связи с ограничениями из-за коронавируса. '''
