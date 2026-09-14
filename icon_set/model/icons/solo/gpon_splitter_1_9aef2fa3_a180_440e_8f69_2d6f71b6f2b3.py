'Three-way splitter: a circular hub and three clearly connected outgoing arrows, with matching arrowheads.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9aef2fa3-a180-440e-8f69-2d6f71b6f2b3'
SOURCE_PATH = 'icons-json/networks/gpon splitter 1_9aef2fa3-a180-440e-8f69-2d6f71b6f2b3.json'
AUTHOR = 'gpt-6'

class GponSplitter1(Solo48):
    icon_id = 'gpon-splitter-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    aliases = ()
    keywords = ('gpon', 'splitter', 'networks')

    def build(self) -> None:
        # Three outgoing paths share one real junction; ring keeps a legible central opening.
        self.add_arc('hub-a',(12,24),(24,24),radius_x=6)
        self.add_arc('hub-b',(24,24),(12,24),radius_x=6)
        self.add_contour('hub','hub-a','hub-b',closed=True)
        self.add_line('input',(4,24),(12,24));self.relate('connect','input','hub')
        self.add_polyline('branches',(38,8),(24,24),(44,24))
        self.add_line('lower',(24,24),(38,40))
        self.relate('connect','branches','hub');self.relate('connect','lower','hub');self.relate('connect','branches','lower')
        for name,pts,owner in (('top-head',((31,8),(38,8),(38,15)),'branches'),('right-head',((39,19),(44,24),(39,29)),'branches'),('lower-head',((31,40),(38,40),(38,33)),'lower')):
            self.add_polyline(name,*pts);self.relate('connect',name,owner)
