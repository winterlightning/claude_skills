import math, numpy as np
def _tangent(c1,r1,s1,c2,r2,s2):
    c1=np.array(c1,float); c2=np.array(c2,float); D=c2-c1; L=np.linalg.norm(D); a=(s2*r2-s1*r1)
    for sgn in (1,-1):
        ang=math.atan2(D[1],D[0])+sgn*math.acos(max(-1,min(1,-a/L)))
        m=np.array([math.cos(ang),math.sin(ang)]); d=np.array([-m[1],m[0]])
        p1=c1+s1*r1*m; p2=c2+s2*r2*m; q=p2-p1
        if q@d>0 and abs(q[0]*d[1]-q[1]*d[0])<1e-6*max(1,L): return p1,p2
    raise ValueError('no tangent')
def rounded(nodes):
    """Polyline through circle centres; radius-0 nodes are sharp points. Strokes run tangent to each circle."""
    n=len(nodes); sides=[0]*n
    for i in range(1,n-1):
        A,B,C=(np.array(nodes[k][0],float) for k in (i-1,i,i+1))
        sides[i]=1 if (B-A)[0]*(C-B)[1]-(B-A)[1]*(C-B)[0]>0 else -1
    segs=[_tangent(nodes[i][0],nodes[i][1],sides[i],nodes[i+1][0],nodes[i+1][1],sides[i+1]) for i in range(n-1)]
    d=f"M{segs[0][0][0]:.4g} {segs[0][0][1]:.4g}"
    for i,(p1,p2) in enumerate(segs):
        r=nodes[i][1]
        if i>0 and r>0: d+=f"A{r:g} {r:g} 0 0 {1 if sides[i]>0 else 0} {p1[0]:.4g} {p1[1]:.4g}"
        d+=f"L{p2[0]:.4g} {p2[1]:.4g}"
    return d
