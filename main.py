for m in range(0,10):
    for a in range(0,10):
        for r in range(0,10):
            for o in range(0,10):
                for c in range(0,10):
                    for t in range(0,10):
                        for y in range(0,10):
                            for e in range(0,10):
                                if 2*m*10000+2*a*1000+2*r*100+c*10+t*10+o+y == c*100000+a*10000+t*1000+t*100+e*10+r \
                                        and {1, 7, 8, 6, 2}.issubset({m, a, r, o, c, t, y, e}) \
                                        and len({m,a,r,o,c,t,y,e})==8:
                                    print(m,a,r,o,c,t,y,e)
                                    l = {m:'m',a:'a',r:'r',o:'o',c:'c',t:'t',y:'y',e:'e'}
                                    print(l[1],l[7],l[8],l[6],l[2],l[7])