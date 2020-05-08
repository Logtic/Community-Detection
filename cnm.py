import snap
import csv
import time

def buildG(G, file_, delimiter_):
    reader = csv.reader(open(file_), delimiter=delimiter_)
    for line in reader:
        if len(line) > 2:
            if float(line[2]) != 0.0:
                #line format: u,v,w
                try:
                    G.AddNode(int(line[0]))
                    G.AddNode(int(line[1]))
                    G.AddEdge(int(line[0]),int(line[1]))
                except RuntimeError:
                    try:
                        G.AddNode(int(line[1]))
                        G.AddEdge(int(line[0]),int(line[1]))
                    except RuntimeError:
                        try:
                            G.AddEdge(int(line[0]), int(line[1]))
                        except RuntimeError:
                            continue


G = snap.TUNGraph.New()
buildG(G, 'dota_100_player_info.csv', ',')
UGraph = G#snap.GenRndGnm(snap.PUNGraph, 100, 1000)
startTime = time.time()
CmtyV = snap.TCnComV()

modularity = snap.CommunityCNM(UGraph, CmtyV)
endTime = time.time()
con = ""
for Cmty in CmtyV:
    con = con+ "{"
    for NI in Cmty:
        con = con + str(NI)+", "
    con = con+"}, "
print(con)
print("The modularity of the network is %f" % modularity)
print(endTime-startTime)

tempGraph = snap.GenRndGnm(snap.PUNGraph, 10, 20)
snap.DrawGViz(UGraph, snap.gvlDot, "cnm.png", "graph 1", True)
