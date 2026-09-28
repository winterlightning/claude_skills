"""Motor scooter with raised seat, covered rear wheel and exposed front wheel.
HRECT_L: (4,8)-(44,40). Seat uses equal eight-unit spans. Steering owns
body attachment (34,16); wheel attaches at its top. Lucide scooter supplies
wheel/fork contour principle. Omit small headlamp at this profile.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '8ce52ac4-8cd4-4f1c-996b-cf71cccf69bd'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_34/sidecar_8ce52ac4-8cd4-4f1c-996b-cf71cccf69bd.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'low-motor-scooter-in-right-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ['Vintage Motor Scooter']
    keywords = ['scooter','motorcycle','wheels','vehicle','seat','transport']
    def build(self):
        self.add_arc('rear-cowl',(4,32),(12,24),radius_x=8)
        self.add_line('seat-bottom',(12,24),(20,24))
        self.add_line('deck-top',(20,24),(21,24))
        self.add_line('body-rise',(21,24),(34,16))
        self.add_bezier('body-bottom',(21,24),((21,30),(21,32),(20,32)))
        self.add_line('deck-bottom',(20,32),(18,32))
        self.add_line('rear-bottom',(18,32),(4,32))
        self.add_contour('body','rear-cowl','seat-bottom','deck-top','body-bottom','deck-bottom','rear-bottom',closed=True)
        self.relate('connect','body-rise','deck-top')
        self.relate('connect','body-rise','body-bottom')
        self.add_polyline('seat',(12,24),(12,16),(20,16),(20,24))
        for a,b in [('seat-1','rear-cowl'),('seat-1','seat-bottom'),('seat-3','seat-bottom'),('seat-3','deck-top')]:self.relate('connect',a,b)
        self.add_arc('rear-wheel',(20,32),(4,32),radius_x=8)
        for x in ['deck-bottom','rear-cowl','body-bottom']:self.relate('connect','rear-wheel',x)
        self.add_polyline('handlebar',(26,8),(32,8),(34,16))
        self.add_line('fork',(34,16),(37,26))
        for a,b in [('handlebar-2','fork'),('handlebar-2','body-rise'),('fork','body-rise')]:self.relate('connect',a,b)
        self.add_arc('front-right',(37,26),(37,40),radius_x=7)
        self.add_arc('front-left',(37,40),(37,26),radius_x=7)
        self.add_contour('front-wheel','front-right','front-left',closed=True)
        for a in ['front-right','front-left']:self.relate('connect','fork',a)
