"""A round coin bears a Bitcoin B currency mark.
Symbol plan: Concentric coin; B with a stem, three bars at pitch 8 and two equal round bowls; centered currency extensions.
Keyshape visible bounds: (2, 2, 46, 46).
Construction references: Lucide bitcoin: stem and stacked round bowls; supplied reference: coin enclosure and currency extensions..
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '91a08a40-6b1a-44f8-90e3-1e362a296712'
SOURCE_PATH = 'pictographic-primitives/money/crypto currency bitcoin_91a08a40-6b1a-44f8-90e3-1e362a296712.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'crypto-currency-bitcoin'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('crypto', 'currency', 'bitcoin')
    def build(self):
        self.circle('coin',24,24,20)
        # The B owns three equally spaced horizontal bars and matching semicircular bowls.
        x,y,step=18,16,8
        self.add_line('stem',(x,y),(x,y+2*step))
        for i in range(3): self.add_line(f'bar-{i}',(x,y+i*step),(26,y+i*step))
        for i in range(2):
            self.add_arc(f'bowl-{i}',(26,y+i*step),(26,y+(i+1)*step),radius_x=5,radius_y=4)
            self.relate('connect',f'bowl-{i}',f'bar-{i}')
            self.relate('connect',f'bowl-{i}',f'bar-{i+1}')
        for i in range(3):self.relate('connect','stem',f'bar-{i}')
        self.relate('connect','bowl-0','bowl-1')
        self.add_line('currency-top',(24,13),(24,16))
        self.add_line('currency-bottom',(24,32),(24,35))
        self.relate('connect','currency-top','bar-0')
        self.relate('connect','currency-bottom','bar-2')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+"-top", (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+"-bottom", (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+"-top", name+"-bottom", closed=True)

    def box(self, name, left, top, right, bottom, r=3):
        points = [(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
                  (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f"{name}-{i}"
            if i%2: self.add_arc(part,a,b,radius_x=r)
            else: self.add_line(part,a,b)
            members.append(part)
        self.add_contour(name,*members,closed=True)
