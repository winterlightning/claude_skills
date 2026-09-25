"""Tram with pantograph; authored directly on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8dc80b79-4f64-4193-a2da-bdeb072566a5'
SOURCE_PATH = 'pictographic-primitives/transportation/railroad locomotive_8dc80b79-4f64-4193-a2da-bdeb072566a5.svg'
AUTHOR = 'gpt-6'

class TramWithPantograph(Solo48):
    icon_id = 'tram-with-pantograph'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('tram', 'streetcar', 'trolley', 'pantograph', 'railway', 'light rail', 'electric', 'transport')

    def build(self) -> None:
        def wheel(name,x,y,r):
            self.add_arc(name+'-right',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(name+'-left',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(name,name+'-right',name+'-left',closed=True)
        # HRECT_L (6,8)-(42,40). Symmetric diamond pickup over a broad tram.
        self.add_polyline('body',(4,24),(14,24),(24,24),(34,24),(44,24),(44,32),(34,32),(14,32),(4,32),closed=True)
        self.add_polyline('roof-bar',(4,24),(4,24),(24,24),(44,24),(44,24))
        self.add_polyline('pantograph',(24,8),(32,16),(24,24),(16,16),closed=True)
        self.relate('connect','roof-bar','body')
        self.relate('connect','pantograph','roof-bar')
        self.relate('connect','pantograph','body')
        self.add_polyline('rail',(4,40),(14,40),(34,40),(44,40))
        for name,x in [('left',14),('right',32)]:
            self.add_line(name+'-end-panel',(x,24),(x,32))
            self.relate('connect',name+'-end-panel','body')
            self.relate('connect',name+'-end-panel','roof-bar')
            wheel(name+'-wheel',x,36,4)
            self.relate('connect',name+'-wheel','body')
            self.relate('connect',name+'-wheel',name+'-end-panel')
            self.relate('connect',name+'-wheel','rail')

