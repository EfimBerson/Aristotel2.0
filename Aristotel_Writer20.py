import Arist_Action_Gen

g = []

nstrok = int(input('введите количество строк в сцене'))

#-----------Функция распределения смыла в сцене по актам в процуетах -(в будущем обычить нейроной сетью)----------
Scene_Act1 = 35
Scene_Act3 = 25
Scene_Act2 = 100 - Scene_Act1 - Scene_Act3

s1 = nstrok*Scene_Act1//100
s2 = nstrok*Scene_Act2//100
s3 = nstrok - s1 - s2

print('Строк в акте 1:',s1,' 2:',s2,' 3:',s3)

# ------- Создание матрицы аристотеля ---------------

m_A = []
m_nACT = []
for i in range(s1):
    m_A.append([1,0,0])
    m_nACT.append(1)
for i in range(s2):
    m_A.append([0,1,0])
    m_nACT.append(2)
for i in range(s3):
    m_A.append([0,0,1])
    m_nACT.append(3)


# m_A = [[1,0,0],[0,1,0],[0,0,1]]

# -------- Заполнение матрицы глаголами
for i in range(len(m_A)):
    m_V = Arist_Action_Gen.vebs_random(m_A[i][0], m_A[i][1], m_A[i][2])

    if i > 1:  # --- повторное генерироване глаголов в случае повторения предложений
        while g[i-1] == m_V[0] or g[i-1] == m_V[1] or g[i-1] == m_V[2] :
            m_V = Arist_Action_Gen.vebs_random(m_A[i][0], m_A[i][1], m_A[i][2])


    if m_A[i][0] != 0 : g.append(m_V[0])
    if m_A[i][1] != 0 : g.append(m_V[1])
    if m_A[i][2] != 0 : g.append(m_V[2])

    # g.append(Arist_Action_Gen.vebs_random(m_A[i][0],m_A[i][1],m_A[i][2]))
    print('Акт №',m_nACT[i] ,' ',g[i])
