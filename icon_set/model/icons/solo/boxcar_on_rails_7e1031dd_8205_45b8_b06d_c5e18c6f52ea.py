"""Boxcar on rails; authored directly on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7e1031dd-8205-45b8-b06d-c5e18c6f52ea'
SOURCE_PATH = 'pictographic-primitives/transportation/railroad locomotive cargo_7e1031dd-8205-45b8-b06d-c5e18c6f52ea.svg'
AUTHOR = 'gpt-6'

class BoxcarOnRails(Solo48):
    icon_id = 'boxcar-on-rails'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('boxcar', 'freight wagon', 'cargo train', 'railway', 'wagon', 'rail', 'goods', 'train')

    def build(self) -> None:
        def wheel(name,x,y,r):
            self.add_arc(name+'-right',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(name+'-left',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(name,name+'-right',name+'-left',closed=True)
        # HRECT_L (6,8)-(42,40). Two bogies replace four crowded tiny wheels.
        self.add_line('roof',(10,8),(38,8))
        self.add_arc('top-right',(38,8),(42,12),radius_x=4)
        self.add_line('right-wall',(42,12),(42,24))
        self.add_arc('bottom-right',(42,24),(38,28),radius_x=4)
        self.add_line('floor-1', (38, 28), (36, 28))
        self.add_line('floor-2', (36, 28), (12, 28))
        self.add_line('floor-3', (12, 28), (10, 28))
        self.add_arc('bottom-left',(10,28),(6,24),radius_x=4)
        self.add_line('left-wall',(6,24),(6,12))
        self.add_arc('top-left',(6,12),(10,8),radius_x=4)
        self.add_contour('body','roof','top-right','right-wall','bottom-right','floor-1','floor-2','floor-3','bottom-left','left-wall','top-left',closed=True)
        self.add_line('left-chassis',(6,28),(10,28))
        self.add_line('right-chassis',(38,28),(42,28))
        self.relate('connect','left-chassis','body')
        self.relate('connect','right-chassis','body')
        for x in [18,30]:self.add_line('door-'+str(x),(x,17),(x,19))
        self.add_polyline('rail',(6,40),(12,40),(36,40),(42,40))
        for name,x in [('rear',12),('front',36)]:
            wheel(name+'-wheel',x,34,6)
            self.relate('connect',name+'-wheel','body')
            self.relate('connect',name+'-wheel','rail')

