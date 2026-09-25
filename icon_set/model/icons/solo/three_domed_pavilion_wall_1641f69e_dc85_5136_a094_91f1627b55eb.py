"""SQUARE (6,6)-(42,42) centerlines. Preserve three domed pavilions, central finial, wall band and vertical divisions. Merge pavilion bases into one skyline; omit side finials and extra horizontal bands. Mirrored about x=24.
Lucide church and castle inform clear roof/wall structure and simple arch construction.
Re-authored on the active SOLO48 contract from the supplied landmark render.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1641f69e-dc85-5136-a094-91f1627b55eb'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-01/red fort india_1641f69e-dc85-5136-a094-91f1627b55eb.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'three-domed-pavilion-wall'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "landmarks"
    aliases = ()
    keywords = ('fort', 'palace', 'dome', 'pavilion', 'wall', 'landmark', 'india', 'architecture', 'heritage')

    def build(self):
        self.add_line('left-wall-1',(6,42),(6,30))
        self.add_line('left-wall-2',(6,30),(6,28))
        self.add_arc('left-dome',(6,28),(16,28),radius_x=5,radius_y=7)
        self.add_line('left-neck',(16,28),(16,30))
        self.add_line('center-left',(16,30),(18,24))
        self.add_arc('center-dome-left',(18,24),(24,16),radius_x=8,radius_y=8)
        self.add_arc('center-dome-right',(24,16),(30,24),radius_x=8,radius_y=8)
        self.add_line('center-right',(30,24),(32,30))
        self.add_line('right-neck',(32,30),(32,28))
        self.add_arc('right-dome',(32,28),(42,28),radius_x=5,radius_y=7)
        self.add_line('right-wall-1',(42,28),(42,30))
        self.add_line('right-wall-2',(42,30),(42,42))
        self.add_contour('skyline','left-wall-1','left-wall-2','left-dome','left-neck','center-left','center-dome-left','center-dome-right','center-right','right-neck','right-dome','right-wall-1','right-wall-2')
        self.add_polyline('cross-stem',(24,6),(24,9),(24,16))
        self.add_polyline('cross-bar',(20,9),(24,9),(28,9))
        self.relate('connect','cross-stem','cross-bar')
        self.relate('connect','cross-stem','skyline')
        self.add_polyline('wall-band',(6,30),(16,30),(32,30),(42,30))
        self.relate('connect','wall-band','skyline')
        for x in (16,32):
            self.add_line(f'wall-division-{x}',(x,30),(x,42))
            self.relate('connect',f'wall-division-{x}','wall-band')
            self.relate('connect',f'wall-division-{x}','skyline')
