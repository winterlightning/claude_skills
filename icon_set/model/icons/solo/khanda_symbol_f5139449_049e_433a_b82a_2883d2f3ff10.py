"""A Khanda with central blade, circular chakkar and paired curved kirpans crossing below. Reduce the blades to coherent strokes; preserve all three swords and the ring."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5139449-049e-433a-b82a-2883d2f3ff10'
SOURCE_PATH = 'pictographic-primitives/religion/sikhism symbol_f5139449-049e-433a-b82a-2883d2f3ff10.svg'
AUTHOR = 'gpt-6'

class KhandaSymbol(Solo48):
    icon_id = 'khanda-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture/religion"
    aliases = ()
    keywords = ('khanda', 'sikhism', 'sword', 'ring', 'emblem', 'symbol', 'religion')

    def oval(self,name,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(name+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Centerline box (6,6)-(42,42), symmetry axis x=24.
        self.add_arc('ring-tr',(24,11),(33,20),radius_x=9)
        self.add_arc('ring-br',(33,20),(24,29),radius_x=9)
        self.add_arc('ring-bl',(24,29),(15,20),radius_x=9)
        self.add_arc('ring-tl',(15,20),(24,11),radius_x=9)
        self.add_contour('ring','ring-tr','ring-br','ring-bl','ring-tl',closed=True)
        self.add_polyline('blade',(24,6),(24,11),(24,29),(24,38),(24,42))
        self.relate('connect','blade','ring')
        for side in (-1,1):
         def p(x,y):return (24+side*x,y)
         name='kirpan-'+str(side)
         self.add_arc(name+'-upper',p(14,8),p(18,22),radius_x=25,sweep=side<0)
         self.add_arc(name+'-lower',p(18,22),p(8,34),radius_x=20,sweep=side<0)
         self.add_line(name+'-grip1',p(8,34),(24,38))
         self.add_line(name+'-grip2',(24,38),p(-8,42))
         self.add_contour(name,name+'-upper',name+'-lower',name+'-grip1',name+'-grip2')
         self.relate('connect',name,'blade')
        self.relate('connect','kirpan--1','kirpan-1')
