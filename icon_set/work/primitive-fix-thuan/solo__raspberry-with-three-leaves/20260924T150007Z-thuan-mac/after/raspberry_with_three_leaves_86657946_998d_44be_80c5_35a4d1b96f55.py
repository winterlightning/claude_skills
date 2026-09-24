"""boysenberry. Revision: Use three clean crown leaves and a tapered berry cluster with balanced rounded lobes. Reduce seven source drupelets to four broad cells.
Construction: Lucide grape: repeated rounded fruit cells, adapted to a tapered berry. Preserve source-facing direction and arrangement.
Keyshape VRECT_L; exact contract extremes, stroke four. No validation exceptions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='86657946-998d-44be-80c5-35a4d1b96f55'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__raspberry-with-three-leaves/20260924T150007Z-thuan-mac/reference/boysenberry_86657946-998d-44be-80c5-35a4d1b96f55.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='raspberry-with-three-leaves'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('boysenberry',)

    def build(self):
        # Each contour owns its shape. Repeated parts share dimensions and axes.
        def path(n,start,steps,closed=False):
            p=start; members=[]
            for j,s in enumerate(steps):
                k=f'{n}-{j}';kind,q,*v=s
                if kind=='L': self.add_line(k,p,q)
                elif kind=='A': self.add_arc(k,p,q,radius_x=v[0],radius_y=v[1],sweep=v[2])
                elif kind=='C': self.add_bezier(k,p,(v[0],v[1],q))
                members.append(k);p=q
            self.add_contour(n,*members,closed=closed)
        def line(n,a,b):self.add_line(n,a,b)
        def poly(n,*p):self.add_polyline(n,*p)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def join(a,b):self.relate('connect',a,b)

        path('outline',(16,20),[('C',(8,8),(10,18),(8,12)),('C',(20,14),(14,8),(18,10)),('C',(24,4),(20,10),(22,6)),('C',(28,14),(26,6),(28,10)),('C',(40,8),(30,10),(34,8)),('C',(32,20),(40,12),(38,18)),('A',(40,28),8,8,True),('C',(34,36),(40,32),(38,36)),('C',(24,44),(34,42),(28,44)),('C',(14,36),(20,44),(14,42)),('C',(8,28),(10,36),(8,32)),('A',(16,20),8,8,True)],True)
        poly('crown-base',(16,20),(24,20),(32,20))
        path('cells',(8,28),[('C',(16,35),(8,32),(12,35)),('C',(24,28),(20,35),(24,32)),('C',(32,35),(24,32),(28,35)),('C',(40,28),(36,35),(40,32))]);join('cells','outline')
        line('middle',(24,20),(24,28));join('middle','crown-base');join('middle','cells')

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)
