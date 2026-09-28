"""Over-ear headphones have a broad curved headband and tall padded earcups. A cable emerges from the right cup, loops downward and runs left to a small connector plug.
Symbol plan: Symmetric arched headphones with compact circular cups and a long right-hand cable curling left into an outlined plug. Simplify padded cups to circles; cable and plug remain attached physical parts.
Keyshape: VRECT_L; centerline extremes (8,4)-(40,44).
Construction reference: headset; local original and atomic geometry inspected for Lucide.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3166725a-0332-4cff-bea4-228fc51449c2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__headphones-with-long-cable/20260927T061835Z-thuan-mac-1/reference/headphones cable_3166725a-0332-4cff-bea4-228fc51449c2.svg'
AUTHOR = "gpt-6"

class BatchSolo(Solo48):
    icon_id = 'headphones-with-long-cable'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'audio'
    categories = ('audio', 'primitives')
    aliases = ()
    keywords = ('headphones', 'with', 'long', 'cable')

    def build(self):

        def segments(name,*points):
            for j,(a,b) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{j}',a,b)

        def circle(name,cx,cy,r):
            self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        def rect(name,l,t,r,b,q=0):
            if not q:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
                return
            points=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
            ids=[]
            for j,(a,z) in enumerate(zip(points,points[1:])):
                if a==z:continue
                n=f'{name}-{j}'
                if j%2:self.add_arc(n,a,z,radius_x=q)
                else:self.add_line(n,a,z)
                ids.append(n)
            self.add_contour(name,*ids,closed=True)

        # Padded rectangular earcups replace the tiny rings; the wire still
        # exits the right pad and curls left into a visible plug.
        self.add_arc('band',(13,22),(35,22),radius_x=11,radius_y=18)
        for n,left in [('left',8),('right',28)]:
         rect(n,left,22,left+12,36,4)
         self.relate('connect',n,'band')
        self.add_line('cord-start',(35,36),(35,39))
        self.add_arc('cord-bend',(35,39),(30,44),radius_x=5)
        self.add_line('cord-end',(30,44),(18,44))
        self.add_contour('cord','cord-start','cord-bend','cord-end')
        self.relate('connect','cord','right')
        self.add_line('plug',(8,44),(18,44))
        self.relate('connect','cord','plug')
