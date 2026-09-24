'Desk lamp: retain the tilted shade, circular hinge and curved base while joining both arms at an exact common hinge point.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8fffde25-08b0-46d2-9123-537377f28274'
SOURCE_PATH = 'pictographic-primitives/office/lamp_8fffde25-08b0-46d2-9123-537377f28274.svg'
AUTHOR = 'gpt-6'

class Lamp(Solo48):
    icon_id = 'lamp'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('lamp', 'office')

    def build(self) -> None:
        # Square envelope: tilted shade, articulated arm and semicircular weighted base.
        self.add_line('shade-lip',(6,12),(18,24))
        self.add_arc('shade-corner',(18,24),(22,20),radius_x=4,sweep=False)
        self.add_bezier('shade-upper',(22,20),((22,17),(21,15),(20,12)),((20,9),(24,8),(22,6)),((20,6),(18,9),(15,10)),((11,10),(7,9),(6,12)))
        # Keep the polyline's existing contour separate and declare the real shared endpoints.
        self.add_contour('shade-lower','shade-lip','shade-corner')
        self.relate('connect','shade-upper','shade-lower')
        self.add_line('upper-arm',(20,12),(34,22))
        self.add_line('lower-arm',(34,22),(30,34))
        self.relate('connect','upper-arm','shade-upper');self.relate('connect','upper-arm','lower-arm')
        self.add_arc('pivot-a',(34,22),(42,22),radius_x=4)
        self.add_arc('pivot-b',(42,22),(34,22),radius_x=4)
        self.add_contour('pivot','pivot-a','pivot-b',closed=True)
        self.relate('connect','upper-arm','pivot');self.relate('connect','lower-arm','pivot')
        self.add_arc('base-left',(22,42),(30,34),radius_x=8)
        self.add_arc('base-right',(30,34),(38,42),radius_x=8)
        self.add_line('base-bottom',(38,42),(22,42))
        self.add_contour('base','base-left','base-right','base-bottom',closed=True)
        self.relate('connect','lower-arm','base')
