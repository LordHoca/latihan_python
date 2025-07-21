
# Ubah aja Graphnya di sini
gr1 = ["c", "c", "d",] # Dari simpul ini
gr2 = ["b", "d", "a",] # Ke simpul ini
#-----------------------------------------
sim = set()
for i in range (len(gr1)) :
    sim.add(gr1[i]), sim.add(gr2[i])
sim = sorted(sim)
simpulIdx = {}
matrix = [[0] * len(sim) for _ in range(len(sim))]
for i in range(len(sim)) :
    simpulIdx[sim[i]] = i
print(sim, simpulIdx)
for i in range(len(gr1)) :
    uIdx = simpulIdx[gr1[i]]
    vIdx = simpulIdx[gr2[i]]
    matrix[uIdx][vIdx] = 1
    matrix[vIdx][uIdx] = 1
def printMatrix():
    print("matriks adjc", "\n  ", " ".join(sim))
    for i in range(len(matrix)):
        print(sim[i], matrix[i])
printMatrix()
