"""A geisha with a high bun, paired hairpins and wrapped kimono. VRECT_XL extremes (5,2)-(43,46). Lucide user informs rounded shoulders; omit facial marks and secondary hair strands."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8294bb7e-b135-54c0-9464-4ea256245719'
SOURCE_PATH = 'pictographic-primitives/culture/batch-03/geisha_8294bb7e-b135-54c0-9464-4ea256245719.svg'


class GeishaBust(Solo48):
    icon_id = 'geisha-bust'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture/objects"
    aliases = ()
    keywords = ('geisha', 'japanese', 'kimono', 'hairpin', 'traditional', 'woman', 'culture', 'asian')

    def build(self) -> None:
        self.add_arc('bun',(16,10),(32,10),radius_x=8)
        self.add_polyline('pin-left',(5,2),(16,10))
        self.add_polyline('pin-right',(32,10),(43,2))
        self.relate('connect','bun','pin-left')
        self.relate('connect','bun','pin-right')
        self.add_line('hair-top',(16,10),(32,10))
        self.add_arc('hair-right',(32,10),(36,20),radius_x=14)
        self.add_arc('chin',(36,20),(12,20),radius_x=12,radius_y=12)
        self.add_arc('hair-left',(12,20),(16,10),radius_x=14)
        self.add_contour('head','hair-top','hair-right','chin','hair-left',closed=True)
        self.relate('connect','head','bun')
        self.relate('connect','head','pin-left')
        self.relate('connect','head','pin-right')
        self.add_arc('shoulder-left',(5,46),(14,37),radius_x=9)
        self.add_line('collar-1',(14,37),(24,46))
        self.add_line('collar-2',(24,46),(34,37))
        self.add_arc('shoulder-right',(34,37),(43,46),radius_x=9)
        self.add_line('hem-right',(43,46),(24,46))
        self.add_line('hem-left',(24,46),(5,46))
        self.add_contour('garment','shoulder-left','collar-1','collar-2','shoulder-right','hem-right','hem-left',closed=True)
