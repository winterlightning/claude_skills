"""Overalls with shoulder straps, bib, rounded chest pocket and divided legs. VRECT_L x8..40 y4..44. Mirror about24 with matching straps and armholes; pocket is an open U, no small closure line. Source supplies garment. Lucide shirt teaches continuous garment outline and curved arm openings."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '896cefd1-de85-4aba-91db-a60cfa3bf248'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/dungarees_896cefd1-de85-4aba-91db-a60cfa3bf248.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'bib-overalls-with-rounded-chest-pocket'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ['Bib Overalls with Rounded Chest Pocket']
    keywords = ['overalls', 'bib', 'pocket', 'straps', 'clothing', 'workwear', 'trousers']
    def build(self):
        self.add_line('bib',(12,12),(36,12))
        self.add_bezier('right-armhole',(36,12),((36,18),(38,22),(40,24)))
        points=[(40,24),(40,44),(28,44),(28,38),(20,38),(20,44),(8,44),(8,24)]
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'legs-{i}',a,b)
        self.add_bezier('left-armhole',(8,24),((10,22),(12,18),(12,12)))
        self.add_contour('garment','bib','right-armhole',*[f'legs-{i}' for i in range(1,8)],'left-armhole',closed=True)
        for side in (-1,1):
            x=24+side*12
            self.add_line(f'strap-{side}',(x,4),(x,12))
            self.relate('connect','garment',f'strap-{side}')
        self.add_line('pocket-left',(20,21),(20,25))
        self.add_arc('pocket-bottom',(20,25),(28,25),radius_x=4,sweep=False)
        self.add_line('pocket-right',(28,25),(28,21))
        self.add_contour('pocket','pocket-left','pocket-bottom','pocket-right')
