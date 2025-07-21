# Ubah Graph Aslinya Disini
gr1= ["a", "b", "c", "d", "a", "b"] # Dari Simpul ini
gr2= ["b", "c", "d", "a", "c", "d"] # Ke simpul ini
#-----------------------------------------------------
gras = []
for i in range(len(gr1)) :
    gras.append((gr1[i], gr2[i]))
for i in range(len(gr2)) :
    gras.append((gr2[i], gr1[i]))
print("Graph Asli : ",gras[:(len(gras)//2)])
def classify_walk(user_input):
    path = user_input.split()
    print(f"Input simpul: {path}")
    isTertutup = path[0] == path[-1]
    isWalk = True
    isTrail = True
    isPath = True
    edges = []
    nodeSeen = set()
    for i in range(len(path) - 1):
        edge = (path[i], path[i + 1])
        reverse_edge = (path[i + 1], path[i])
        if edge not in gras or reverse_edge not in gras :
            isWalk = False
        if edge in edges or reverse_edge in edges:
            isTrail = False
        edges.append(edge)
        if path[i] in nodeSeen:
            isPath = False 
        nodeSeen.add(path[i])
    if path[-1] in nodeSeen:
        isPath = False
    print(edges, nodeSeen)
    if isWalk :
        print("Walk Tertutup" if isTertutup else "\nWalk terbuka", "\nMerupakan trail"  if isTrail else "\nBukan Trail", "\nMerupakan path" if isPath else "\nBukan Path")
    else :
        print("Bukan Walk!!")
inp = input("Masukkan urutan simpul (pisahkan dengan spasi, contoh: A B C D B): ")
classify_walk(inp)