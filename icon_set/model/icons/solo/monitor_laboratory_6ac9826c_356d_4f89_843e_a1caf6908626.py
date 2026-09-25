"""monitor laboratory: complete SOLO48 repair.
Kept the monitor, stand, flask neck and flared flask body. Removed the crowded liquid-level line.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6ac9826c-356d-4f89-843e-a1caf6908626'
SOURCE_PATH = 'pictographic-primitives/other/monitor laboratory_6ac9826c-356d-4f89-843e-a1caf6908626.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'monitor-laboratory'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('monitor laboratory',)



    def monitor(self):
        # Symmetric rounded screen, split bottom edge at actual stand attachment.
        self.add_line('top',(10,6),(38,6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.add_line('right',(42,10),(42,30))
        self.add_arc('br',(42,30),(38,34),radius_x=4)
        self.add_line('bottom-right',(38,34),(24,34))
        self.add_line('bottom-left',(24,34),(10,34))
        self.add_arc('bl',(10,34),(6,30),radius_x=4)
        self.add_line('left',(6,30),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('screen','top','tr','right','br','bottom-right','bottom-left','bl','left','tl',closed=True)
        self.add_line('stand',(24,34),(24,42))
        self.add_polyline('foot',(16,42),(24,42),(32,42))
        self.relate('connect','screen','stand')
        self.relate('connect','stand','foot')


    def build(self):
        # Flask with a narrow neck, sloping walls and a liquid-level bar.
        self.monitor()
        self.add_polyline('flask',(20,15),(28,15),(28,18),(32,25),(16,25),(20,18),closed=True)
