import pandas as pd
from random import randint

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
Act_2 = [2]   # видеть
Act_3 = [4,8,9,12]   # Завершать, разрушать, создавать, Фиксировать



def vebs_random(x1,x2,x3):
    ###------Выбор типов глаголов в Акте

    a1 = randint(0, len(Act_1) - 1)
    a2 = randint(0, len(Act_2) - 1)
    a3 = randint(0, len(Act_3) - 1)
    ### ------ Вытаскиваем глаголы для соответсвующих актов

    act1_v = []
    act2_v = []
    act3_v = []
    act1_v_en = []
    act2_v_en = []
    act3_v_en = []
    # -- процедура собирание листов глаголов по номеру класса глагола --
    for i in range(lib_act.index.stop):
        if lib_act.loc[i].at['NClass_1'] == Act_1[a1]:
            act1_v.append(lib_act.loc[i].at['Действие'])
            act1_v_en.append(lib_act.loc[i].at['Act_Hero'])
            Act_T1 = lib_act.loc[i].at['Class 1']
        if lib_act.loc[i].at['NClass_1'] == Act_2[a2]:
            act2_v.append(lib_act.loc[i].at['Действие'])
            act2_v_en.append(lib_act.loc[i].at['Act_Hero'])
            Act_T2 = lib_act.loc[i].at['Class 1']
        if lib_act.loc[i].at['NClass_1'] == Act_3[a3]:
            act3_v.append(lib_act.loc[i].at['Действие'])
            act3_v_en.append(lib_act.loc[i].at['Act_Hero'])
            Act_T3 = lib_act.loc[i].at['Class 1']


    ###------Выбор глагола из типа для Акта

    a1 = randint(0, len(act1_v) - 1)
    a2 = randint(0, len(act2_v) - 1)
    a3 = randint(0, len(act3_v) - 1)

    # print('----глаголы для трех актов сгенерированы vebs------> ')

    y1 = []
    y2 = []
    y3 = []

    # Вывод глаголов

    if x1 == 1:
        # y1.append(Act_T1)
        y1.append(act1_v_en[a1])
        y1.append(act1_v[a1])
    else:
        y1.append(0)

    if x2 == 1:
        # y2.append(Act_T2)
        y2.append(act2_v_en[a2])
        y2.append(act2_v[a2])
    else:
        y2.append(0)

    if x3 == 1:
        # y3.append(Act_T3)
        y3.append(act3_v_en[a3])
        y3.append(act3_v[a3])
    else:
        y3.append(0)

    return y1,y2,y3




