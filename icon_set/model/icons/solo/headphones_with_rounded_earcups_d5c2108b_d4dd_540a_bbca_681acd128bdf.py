"""Two broad rounded earcups sit beneath a tall semicircular headband. Their inner sides are nearly straight, and the open central space extends from the crown to the bottom.
Symbol plan: One shared concept for both rounded-earcup references. Mirror radius-5 capsule pads around x=24 and join the band at each crown. The elliptical arch leaves a generous central opening.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: headphones; local original and atomic geometry inspected for Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd5c2108b-d4dd-540a-bbca-681acd128bdf'
SOURCE_PATH = 'pictographic-primitives/audio/headphones_d5c2108b-d4dd-540a-bbca-681acd128bdf.svg'
AUTHOR = 'gpt-6'

SOURCE_REFERENCES = (('d5c2108b-d4dd-540a-bbca-681acd128bdf', 'pictographic-primitives/audio/headphones_d5c2108b-d4dd-540a-bbca-681acd128bdf.svg'), ('d790d911-eb1f-58e5-91ac-7d9fb1a04fe9', 'pictographic-primitives/audio/headphones_d790d911-eb1f-58e5-91ac-7d9fb1a04fe9.svg'))

class BatchSolo(Solo48):
    icon_id = 'headphones-with-rounded-earcups'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'audio'
    categories = ('audio', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('headphones', 'with', 'rounded', 'earcups')

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

        self.add_arc('band',(11,24),(37,24),radius_x=13,radius_y=18)
        for name,left in [('left',6),('right',32)]:
         rect(name,left,24,left+10,42,5)
         self.relate('connect','band',name)
