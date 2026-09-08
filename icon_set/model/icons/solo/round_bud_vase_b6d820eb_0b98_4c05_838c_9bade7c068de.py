"""Four circular buds on an uneven fan of stems rising from a small round vase."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b6d820eb-0b98-4c05-838c-9bade7c068de'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/cherry blossom vase_b6d820eb-0b98-4c05-838c-9bade7c068de.svg'
AUTHOR = 'gpt-6'


class RoundBudVase(Solo48):
    icon_id = 'round-bud-vase'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('vase', 'buds', 'flowers', 'stems', 'bouquet', 'plant', 'decor')

    def build(self) -> None:
        self.add_polyline('mouth',(16,30),(24,30),(32,30))
        self.add_arc('vase-right',(32,30),(24,46),radius_x=10,radius_y=10)
        self.add_arc('vase-left',(24,46),(16,30),radius_x=10,radius_y=10)
        self.add_contour('vase-body','vase-right','vase-left')
        self.relate('connect','mouth','vase-body')
        for name,x,y in [('left',8,12),('top',22,5),('right',40,9),('side',40,23)]:
            self.add_arc(name+'-bud-a',(x,y+3),(x,y-3),radius_x=3)
            self.add_arc(name+'-bud-b',(x,y-3),(x,y+3),radius_x=3)
            self.add_contour(name+'-bud',name+'-bud-a',name+'-bud-b',closed=True)
            self.add_line(name+'-stem',(x,y+3),(24,30))
            self.relate('connect',name+'-stem',name+'-bud')
            self.relate('connect',name+'-stem','mouth')
        for a,b in [('left','top'),('left','right'),('left','side'),('top','right'),('top','side'),('right','side')]:
            self.relate('connect',a+'-stem',b+'-stem')
