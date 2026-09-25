from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8fbdf83e-7f75-5f64-b826-fc7b55c55a27'
SOURCE_PATH = 'pictographic-primitives/money/crypto currency bitcoin_8fbdf83e-7f75-5f64-b826-fc7b55c55a27.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bitcoin-cryptocurrency-coin'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    categories = ('primitives', 'money')
    aliases = ()
    keywords = ('bitcoin', 'cryptocurrency', 'coin')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def rounded_rect(self, name, x0, y0, x1, y1, r):
        pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
        ids=[]
        for i in range(8):
            eid=f'{name}-{i}'
            a,b=pts[i],pts[(i+1)%8]
            if i%2: self.add_arc(eid,a,b,radius_x=r)
            else: self.add_line(eid,a,b)
            ids.append(eid)
        self.add_contour(name,*ids,closed=True)

    def build(self):
        # Plan: circular coin owns B with two equal elliptical bowls, shared middle rail and twin bars.
        # CIRCLE center (24,24), centerline radius20, visible radius22.
        self.circle('coin',24,24,20)
        for i,y in enumerate((16,24)):
            self.add_line(f'cap-{i}',(18,y),(26,y))
            self.add_arc(f'bowl-{i}',(26,y),(26,y+8),radius_x=8,radius_y=4)
        self.add_line('bottom',(26,32),(18,32))
        self.add_line('stem-1',(18,32),(18,24))
        self.add_line('stem-2',(18,24),(18,16))
        self.add_contour('b-outline','cap-0','bowl-0','bowl-1','bottom','stem-1','stem-2',closed=True)
        self.relate('connect','b-outline','cap-1')
        for x in (18,26):
            for label,a,b in [('top',(x,14),(x,16)),('bottom',(x,32),(x,34))]:
                name=f'bar-{x}-{label}'
                self.add_line(name,a,b)
                self.relate('connect','b-outline',name)
