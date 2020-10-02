import Arist_Action_Gen

g = []

# g.append(Arist_Action_Gen.vebs_random(1,0,0))
# g.append(Arist_Action_Gen.vebs_random(1,1,0))
# g.append(Arist_Action_Gen.vebs_random(0,1,0))
# g.append(Arist_Action_Gen.vebs_random(0,1,1))
# g.append(Arist_Action_Gen.vebs_random(0,0,1))
#
# for i in range(len(g)):
#     print(g[i])

m = [[1,0,0],
     [1,1,0],
     [0,1,0],
     [0,1,1],
     [0,0,1]]

m_A = [[1,0,0],
       [1,0,0],
       [0,1,0],
       [0,1,0],
       [0,0,1],
       [0,0,1]]

for i in range(len(m)):
    g.append(Arist_Action_Gen.vebs_random(m[i][0],m[i][1],m[i][2]))
    print(g[i])
