
#Input map:
inp = ''''''


inptest='''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''
#This should be 36

inp=inptest

global trails
trails = []
global trail_interm
trail_interm=[]


def gettrails(map, rn,en,num):
    global trail_interm
    global trails

    rn = int(rn)
    en = int(en)
    steps=[[-1,0],[0,-1],[0,1],[1,0]]

    for stepnum,step in enumerate(steps):
        if rn==0:
            if stepnum==0:
                continue
        if en == 0:
            if stepnum==1:
                continue
        if rn == len(map)-1:
            if stepnum==3:
                continue
        if en == len(map[0])-1:
            if stepnum == 2:
                continue
        try:
            nextnum=int(map[rn+step[0]][en+step[1]])
        except:
            #If a character is not a number for testing
            continue
        if nextnum==num+1:
            rnnext=rn+step[0]
            ennext=en+step[1]
            trail_interm.append([rnnext,ennext, nextnum])
            if nextnum==9:
                trails.append(trail_interm)
                trail_interm = []
                continue
            #Found a higher num, go one level deeper from there
            gettrails(map,rnnext,ennext,nextnum)

    #After the loop, 9 has been already added to trails
    #or not found higher num and need to revert to previous depth,
    #delete this step     
    if len(trail_interm)>0: del trail_interm[-1]

    return

map=[]
trailsall=[]
map = inp.split('\n')
startnum = 0
totalpaths = 0
for rn,r in enumerate(map):
    for en,e in enumerate(r):
        if e == "0":
            trail_interm.append([rn,en,0])
            trails = []
            gettrails(map, rn, en, startnum)
            trail_interm=[]
            #Get only the positions of 9 in this iter
            trailendscurr=[line[-1] for line in trails]
            #Remove duplicates
            unique_listcurr = [x for i, x in enumerate(trailendscurr) if x not in trailendscurr[:i]]
            #Add trail numbers from this iter to total
            totalpaths=totalpaths+len(unique_listcurr)
            #All the possible trails
            trailsall.append(trails)

for l in trailsall:
    print(f"All paths from",l[0][0])
    print("row col num")
    for ll in l:
        print(ll)
    print("\n")
    
print("Input file:")
print(inp+"\n")
print("\n"+"Total paths = "+str(totalpaths)+"\n")
