
#Input map:
inp = '''901403454308767601987430010102103430787676
812312567219458912376541023411212321096787
765403498012307433489432196520303234585898
012354321087216524570343787434454100674301
985467891096987019601234378976569981001210
876654102345106508710765234789678972343454
798783287765278710789820105678710169858763
687690196894369821890112344589801258769012
501543285210152152721201453078987340150103
432457894101043043630328762101456498201232
870326543232032154549419234652343567398341
961210012343129069608500165765432985437650
054301456953238778217671876893211076126789
123012387869345632347889956544509089005491
128723498778734101256970987832678179012310
039614595654187214378921078981083238768723
340507680343096785561434563470198740059654
651408971252125896450001412563267651145098
762310564561034587321112303214107892230127
891023453478987878543203474905896543451936
678921962101216969458914985876708712767845
567630879870305456367325676765219603856696
654544567765412343210232110894334564943787
783203498894301210321143029889123765830654
890112985435213456787054334778010894321003
901209876120102365098765245667654784321212
892100125009871074109670123454743065210012
763119834312568983232189812303892178756763
654098701233457654983074505412789109349854
120145610145012523474563676545630201201340
034234543296543210565012985654321347652201
543007665487012365034876501745610458943102
632118978329110874128989432891234367812983
789327659418723923567876541010765298103894
879454341507654010430765430199804105412765
988761030676589012321650321783219876545630
896902321585438543456761230654323401454321
787813490492127654349854345013210562367212
076524582341013434234981016724505678498101
123433671034565521187832109834694989654342
589652180123877610096543258943783878701233
676543091012988987101234567652102107212344'''


inptest='''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''
#This should be 36

inp=inp

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
    #or not found higher num and need to revert to previous depth
    # delete this step     
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
