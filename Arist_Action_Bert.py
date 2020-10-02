import pandas as pd
from random import randint
import numpy as np
from keras_bert import load_trained_model_from_checkpoint
import tokenization

# папка, куда распаковали преодобученную нейросеть BERT
folder = '/Users/efimberson/Documents/AI/BERT/bert_model'

config_path = folder+'/bert_config.json'
checkpoint_path = folder+'/bert_model.ckpt'
vocab_path = folder+'/vocab.txt'

tokenizer = tokenization.FullTokenizer(vocab_file=vocab_path, do_lower_case=False)

model = load_trained_model_from_checkpoint(config_path, checkpoint_path, training=True)
model.summary()

lib_act = pd.read_csv("/Users/efimberson/Documents/AI/AristoteL/Vocab/ACTION_Verb_Class.csv")

####----- Библиотека логики

# Act_1 = [1,6,8,9]     # Взаимодействие с объектами, Перемещение в пространстве, разрушать, создавать.
# Act_2 = [1,2,3,5,6,7,8,9,11,12,13]   # Взаимодействие с объектами, видеть, говорить, Объединять, Перемещение в пространстве, Разделить ,разрушать, создавать, Тестировать, Фиксировать, Чувствовать
# Act_3 = [4,8,9,12]   # Завершать, разрушать, создавать, Фиксировать


# Act_1 = [1,6]     # Взаимодействие с объектами, Перемещение в пространстве.
# Act_2 = [2,3,5,7,11,13]   # видеть, говорить, Объединять, Разделить , Тестировать, Чувствовать
# Act_3 = [4,8,9,12]   # Завершать, разрушать, создавать, Фиксировать


# Act_1 = [1,6]     # Взаимодействие с объектами, Перемещение в пространстве.
# Act_2 = [2,3,7,11,13]   # видеть, говорить, Разделить , Тестировать, Чувствовать
# Act_3 = [4,8,9,12]   # Завершать, разрушать, создавать, Фиксировать

Act_1 = [6]     # Перемещение в пространстве
Act_2 = [2]   # видеть, говорить
Act_3 = [4,8]   # Завершать, разрушать, создавать, Фиксировать


###------Выбор типов глаголов в Акте

a1 = randint(0,len(Act_1)-1)
a2 = randint(0,len(Act_2)-1)
a3 = randint(0,len(Act_3)-1)

print('type of veb-> ')
print('Act_1 =',a1,'=>',Act_1[a1])
print('Act_2 =',a2,'=>',Act_2[a2])
print('Act_3 =',a3,'=>',Act_3[a3])

### ------ Вытаскиваем глаголы для соответсвующих актов

act1_v = []
act2_v = []
act3_v = []
act1_v_en = []
act2_v_en = []
act3_v_en = []


for i in range(lib_act.index.stop) :
    if lib_act.loc[i].at['NClass_1'] == Act_1[a1] :
        act1_v.append(lib_act.loc[i].at['Действие'])
        act1_v_en.append(lib_act.loc[i].at['Act_Hero'])
    if lib_act.loc[i].at['NClass_1'] == Act_2[a2] :
        act2_v.append(lib_act.loc[i].at['Действие'])
        act2_v_en.append(lib_act.loc[i].at['Act_Hero'])
    if lib_act.loc[i].at['NClass_1'] == Act_3[a3] :
        act3_v.append(lib_act.loc[i].at['Действие'])
        act3_v_en.append(lib_act.loc[i].at['Act_Hero'])

print('Количество глаголов в 1-ой части',len(act1_v))
print('Количество глаголов в 2-ой части',len(act2_v))
print('Количество глаголов в 3-ей части',len(act3_v))

###------Выбор глагола из типа для Акта

a1 = randint(0,len(act1_v)-1)
a2 = randint(0,len(act2_v)-1)
a3 = randint(0,len(act3_v)-1)

print('type of veb-> ')
print('Act_1 =',a1,'=>',act1_v[a1],' ',act1_v_en[a1])
print('Act_2 =',a2,'=>',act2_v[a2],' ',act2_v_en[a2])
print('Act_3 =',a3,'=>',act3_v[a3],' ',act3_v_en[a3])

print('\n','Финальное предложение:')
print('Герой', act1_v[a1],'[Место действие].', 'Он', act2_v[a2],'врага .','Герой', act3_v[a3],'.')
print('Hero', act1_v_en[a1],'.', 'He', act2_v_en[a2],'Men.','Hero', act3_v_en[a3],'.')

sentence = 'Hero '+ act1_v_en[a1] + ' .' + ' He '+ act2_v_en[a2]+' men [MASK].'+' Hero ' + ' [MASK].'
# sentence = 'Hero '+ act1_v_en[a1] + ' .' + ' He '+ act2_v_en[a2]+' men [MASK].'+' Hero ' + act3_v_en[a3] + ' [MASK].'
# sentence = 'Hero '+ act1_v_en[a1] + ' [MASK].' + ' He '+ act2_v_en[a2]+' men.'+' Hero ' + act3_v_en[a3] + ' [MASK].'




#sentence = 'Я пришел в [MASK] и купил [MASK].'
#sentence = 'Земля это третья [MASK] от Солнца'
# sentence = 'He sleeps [MASK]. He goes [MASK]. He does it.'
# print('Введите предложение:')
# sentence: str  = input()
#sentence = 'Why can’t people live in peace? The history of mankind proves that countries fight wars a lot. I can’t actually point to a country which has never been involved in a war or [MASK] conflict. There are lots of [MASK] people can find for fighting. Some [MASK] want to gain control over other countries’ lands and natural resources. War can be [MASK] for political reasons, too. There are wars for independence when colonies fight for freedom and [MASK]. There are territories in which [MASK] movements are very active. There are groups of people that put forward political or economic demands and get [MASK] in order to achieve their aims. But whatever the conflict is about, it always brings [MASK] and death to people who are willingly or unwillingly involved. Social scientists and political scientists, [MASK] and just ordinary people are trying to work out a formula for a war free world. Living in peace is a [MASK] desire, and I hope that we’ll find out how to make the planet happy and safe.'

print(sentence)

sentence = sentence.replace(' [MASK] ','[MASK]'); sentence = sentence.replace('[MASK] ','[MASK]'); sentence = sentence.replace(' [MASK]','[MASK]')  # удаляем лишние пробелы
sentence = sentence.split('[MASK]')             # разбиваем строку по маске

tokens = ['[CLS]']                 # фраза всегда должна начинаться на [CLS]
# обычные строки преобразуем в токены с помощью tokenizer.tokenize(), вставляя между ними [MASK]
for i in range(len(sentence)):
    if i == 0:
        tokens = tokens + tokenizer.tokenize(sentence[i])
    else:
        tokens = tokens + ['[MASK]'] + tokenizer.tokenize(sentence[i])
tokens = tokens + ['[SEP]']       # фраза всегда должна заканчиваться на [SEP]
token_input = tokenizer.convert_tokens_to_ids(tokens)
token_input = token_input + [0] * (512 - len(token_input))

mask_input = [0]*512

mask_input = [0]*512
for i in range(len(mask_input)):
    if token_input[i] == 103:
        mask_input[i] = 1

seg_input = [0] * 512

token_input = np.asarray([token_input])
mask_input = np.asarray([mask_input])
seg_input = np.asarray([seg_input])

predicts = model.predict([token_input, seg_input, mask_input])[0]
predicts = np.argmax(predicts, axis=-1)
predicts = predicts[0][:len(tokens)]    # отрезаем начало фразы, длиной как исходная фраза, чтобы отсечь случайные выбросы среди нулей дальше

out = []
# добавляем в out только слова в позиции [MASK], которые маскированы цифрой 1 в mask_input
for i in range(len(mask_input[0])):
    if mask_input[0][i] == 1:                       # [0][i], т.к. сеть возвращает batch с формой (1,512), где в первом элементе наш результат
        out.append(predicts[i])

out = tokenizer.convert_ids_to_tokens(out)          # индексы в текстовые токены
out = ' '.join(out)                                 # объединяем токены в строку с пробелами
out = tokenization.printable_text(out)              # в удобочитаемый текст
out = out.replace(' ##','')                         # объединяем разъединенные слова: "при ##шел" -> "пришел"

print('Result:', out)

