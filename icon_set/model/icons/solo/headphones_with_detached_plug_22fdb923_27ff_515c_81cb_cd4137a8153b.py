"""Two rounded earcups hang from a high arched headband. Beneath them, a short cable curves into a large horizontal audio plug with a rounded tip facing right.
Symbol plan: Arched headphones with a separate physical cable and plug below. Compact radius-4 earcups reserve space for an 8-unit plug body and short connector pin.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: headphones; local original and atomic geometry inspected for Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '22fdb923-27ff-515c-81cb-cd4137a8153b'
SOURCE_PATH = 'pictographic-primitives/audio/headphones plug_22fdb923-27ff-515c-81cb-cd4137a8153b.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'headphones-with-detached-plug'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'audio'
    aliases = ()
    keywords = ('headphones', 'with', 'detached', 'plug')

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

        self.add_arc('band',(10,20),(38,20),radius_x=14)
        for n,x in [('left',10),('right',38)]:
         self.add_arc(n+'-a',(x,20),(x,28),radius_x=4)
         self.add_arc(n+'-b',(x,28),(x,20),radius_x=4)
         self.add_contour(n,n+'-a',n+'-b',closed=True);self.relate('connect',n,'band')
        self.add_arc('cable-bend',(10,42),(14,38),radius_x=4)
        self.add_line('cable-end',(14,38),(20,38))
        self.add_contour('cable','cable-bend','cable-end')
        self.add_polyline('plug',(20,34),(28,34),(28,38),(28,42),(20,42),(20,38),closed=True)
        self.relate('connect','cable','plug')
        self.add_line('pin',(28,38),(36,38));self.relate('connect','pin','plug')
