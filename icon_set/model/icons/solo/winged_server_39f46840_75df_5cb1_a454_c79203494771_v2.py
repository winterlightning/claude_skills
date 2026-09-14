# Variant of winged-server; parent file remains unchanged.
"""Winged Server. Authored from the supplied visual brief."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '39f46840-75df-5cb1-a454-c79203494771'
SOURCE_PATH = 'pictographic-primitives/websites/server migration wings_39f46840-75df-5cb1-a454-c79203494771.svg'
AUTHOR = 'gpt-6'

class WingedServerVariant2(Solo48):
    icon_id = 'winged-server-v2'
    variant_of = 'winged-server'
    variant_label = 'Server body with recognizable wings'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('server', 'wings', 'migration', 'flying', 'hardware', 'device', 'transfer')

    def build(self) -> None:
        # Three visible rack bays distinguish the server from a tag or a chip.
        self.box('rack',18,18,30,42,r=2,joins=((18,26),(30,26),(18,30),(30,30),(18,34),(30,34)))
        for y in (26,34):
            self.add_line(f'bay-{y}',(18,y),(30,y))
            self.relate('connect',f'bay-{y}','rack')
        for side,sign in [('left',-1),('right',1)]:
            def p(x,y): return (24+sign*x,y)
            self.add_arc(side+'-sweep',p(6,30),p(18,18),radius_x=12,sweep=sign<0)
            self.add_line(side+'-edge',p(18,18),p(18,6))
            self.add_line(side+'-tip',p(18,6),p(6,12))
            self.add_line(side+'-inner',p(6,12),p(6,18))
            self.add_contour(side+'-wing',side+'-sweep',side+'-edge',side+'-tip',side+'-inner')
            self.relate('connect',side+'-wing','rack')

    def box(self, name, x0, y0, x1, y1, r=2, joins=()):
        # A shared corner radius and explicit attachment nodes own this rectangle.
        points=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),
                (x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
        members=[]
        for i,p in enumerate(points):
            q=points[(i+1)%8]
            if i%2:
                name_i=f'{name}-{i}';self.add_arc(name_i,p,q,radius_x=r);members.append(name_i)
            else:
                mid=[v for v in joins if v!=p and v!=q and
                     ((p[0]==q[0]==v[0] and min(p[1],q[1])<v[1]<max(p[1],q[1])) or
                      (p[1]==q[1]==v[1] and min(p[0],q[0])<v[0]<max(p[0],q[0])))]
                run=[p]+sorted(mid,key=lambda v:(v[0]-p[0])**2+(v[1]-p[1])**2)+[q]
                for j,(a,b) in enumerate(zip(run,run[1:])):
                    name_i=f'{name}-{i}-{j}';self.add_line(name_i,a,b);members.append(name_i)
        self.add_contour(name,*members,closed=True)
