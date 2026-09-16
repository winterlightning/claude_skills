"""Over-ear headphones have a broad curved headband and tall padded earcups. A cable emerges from the right cup, loops downward and runs left to a small connector plug.
Symbol plan: Symmetric arched headphones with compact circular cups and a long right-hand cable curling left into an outlined plug. Simplify padded cups to circles; cable and plug remain attached physical parts.
Keyshape: VRECT_L; centerline extremes (8,4)-(40,44).
Construction reference: headset; local original and atomic geometry inspected for Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3166725a-0332-4cff-bea4-228fc51449c2'
SOURCE_PATH = 'pictographic-primitives/audio/headphones cable_3166725a-0332-4cff-bea4-228fc51449c2.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'headphones-with-long-cable'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'audio'
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

        self.add_arc('band',(12,20),(36,20),radius_x=12,radius_y=16)
        for n,x in [('left',12),('right',36)]:
         self.add_arc(n+'-a',(x,20),(x,28),radius_x=4)
         self.add_arc(n+'-b',(x,28),(x,20),radius_x=4)
         self.add_contour(n,n+'-a',n+'-b',closed=True)
         self.relate('connect',n,'band')
        self.add_line('cord-start',(36,28),(36,32))
        self.add_arc('cord-bend',(36,32),(28,40),radius_x=8)
        self.add_line('cord-end',(28,40),(16,40))
        self.add_contour('cord','cord-start','cord-bend','cord-end')
        self.relate('connect','cord','right')
        self.add_polyline('plug',(8,36),(16,36),(16,40),(16,44),(8,44),closed=True)
        self.relate('connect','cord','plug')
