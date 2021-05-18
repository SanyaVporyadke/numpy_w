import numpy as np

#1 задание.
def make_reverse_np_array(numb):
    a = np.arange(0, numb+1)
    return a[::-1]
#2 задание

ed = np.diag((make_reverse_np_array(10)), k=0)
sum_ = sum(make_reverse_np_array(10))

# 3 задание

""" 4x + 2y + z = 4
x + 3y = 12
5y + 4z = -3 """

x_y_z= np.array([[4, 2, 1], [1, 3, 0], [0, 5, 4]])
c = np.array([4, 12, -3])
res = np.linalg.solve(x_y_z, c)

#4 задание
def cosine( a, b ):
    aLength = np.linalg.norm( a )
    bLength = np.linalg.norm( b )
    
    return np.dot( a, b ) / ( aLength * bLength )

users_stats = np.array(
    [
        [2, 1, 0, 0, 0, 0],
        [1, 1, 2, 1, 0, 0],
        [2, 0, 1, 0, 0, 0],
        [1, 1, 2, 1, 0, 1],
        [0, 0, 1, 2, 0, 0],
        [0, 0, 0, 0, 0, 5],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 3],
        [1, 0, 0, 2, 1, 4]
    ]
)

next_user_stats = np.array([0, 1, 2, 0, 0, 0])

li = []
for i in users_stats:
    li.append(round(cosine(i, next_user_stats), 2))
res = users_stats[li.index(max(li))]



