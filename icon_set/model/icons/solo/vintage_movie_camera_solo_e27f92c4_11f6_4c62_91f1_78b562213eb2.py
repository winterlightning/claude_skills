"""Vintage Movie Camera. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: inspected local Lucide hand, truck, piggy-bank, globe, zap, video and wallet originals and atomic-debug geometry for coherent outlines, shared radii and simplification.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'e27f92c4-11f6-4c62-91f1-78b562213eb2'
SOURCE_PATH = 'pictographic-primitives/state/video_e27f92c4-11f6-4c62-91f1-78b562213eb2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'vintage-movie-camera-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'vintage movie camera')
    def build(self):
        # Two equal reels; camera body and lens form one joined silhouette.
        for name,x in [('left',14),('right',34)]:
            circle(self,name+'-reel',x,12,6)
        self.add_line('body-top',(10,26),(26,26))
        self.add_arc('body-tr',(26,26),(30,30),radius_x=4)
        self.add_line('lens-1',(30,30),(42,26))
        self.add_line('lens-2',(42,26),(42,42))
        self.add_line('lens-3',(42,42),(30,38))
        self.add_arc('body-br',(30,38),(26,42),radius_x=4)
        self.add_line('body-bottom',(26,42),(10,42))
        self.add_arc('body-bl',(10,42),(6,38),radius_x=4)
        self.add_line('body-left',(6,38),(6,30))
        self.add_arc('body-tl',(6,30),(10,26),radius_x=4)
        self.add_contour('body','body-top','body-tr','lens-1','lens-2','lens-3','body-br','body-bottom','body-bl','body-left','body-tl',closed=True)
