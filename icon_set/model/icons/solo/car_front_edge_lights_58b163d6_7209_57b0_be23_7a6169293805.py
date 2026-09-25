"""A car front with edge-connected headlights and rounded U tyres. SQUARE ink (6,6)-(42,42). Lucide car-front informed mirrored geometry; the reference light and wheel treatment remains distinct."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '58b163d6-7209-57b0-be23-7a6169293805'
SOURCE_PATH = 'pictographic-primitives/transportation/car 1_58b163d6-7209-57b0-be23-7a6169293805.svg'
SOURCE_REFERENCES = (('58b163d6-7209-57b0-be23-7a6169293805', 'pictographic-primitives/transportation/car 1_58b163d6-7209-57b0-be23-7a6169293805.svg'),)
AUTHOR = 'gpt-6'

class CarFrontEdgeLights(Solo48):
    icon_id = 'car-front-edge-lights'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('car', 'front', 'vehicle', 'automobile', 'headlights', 'sedan', 'driving', 'head-on')

    def build(self) -> None:
        self.add_line('body-top-0',(8, 16),(10, 16))
        self.add_line('body-top-1',(10, 16),(38, 16))
        self.add_line('body-top-2',(38, 16),(40, 16))
        self.add_arc('body-top-corner',(40, 16),(42, 18),radius_x=2)
        self.add_line('body-right-0',(42, 18),(42, 25))
        self.add_line('body-right-1',(42, 25),(42, 32))
        self.add_arc('body-right-corner',(42, 32),(40, 34),radius_x=2)
        self.add_line('body-bottom-0',(40, 34),(38, 34))
        self.add_line('body-bottom-1',(38, 34),(32, 34))
        self.add_line('body-bottom-2',(32, 34),(16, 34))
        self.add_line('body-bottom-3',(16, 34),(10, 34))
        self.add_line('body-bottom-4',(10, 34),(8, 34))
        self.add_arc('body-bottom-corner',(8, 34),(6, 32),radius_x=2)
        self.add_line('body-left-0',(6, 32),(6, 25))
        self.add_line('body-left-1',(6, 25),(6, 18))
        self.add_arc('body-left-corner',(6, 18),(8, 16),radius_x=2)
        self.add_contour('body','body-top-0','body-top-1','body-top-2','body-top-corner','body-right-0','body-right-1','body-right-corner','body-bottom-0','body-bottom-1','body-bottom-2','body-bottom-3','body-bottom-4','body-bottom-corner','body-left-0','body-left-1','body-left-corner',closed=True)
        self.add_polyline('cabin',(10,16),(16,6),(32,6),(38,16))
        self.relate('connect','cabin','body')
        self.add_line('left-light',(6,25),(12,25))
        self.add_line('right-light',(36,25),(42,25))
        self.relate('connect','left-light','body')
        self.relate('connect','right-light','body')

        for side,x in [('left',8),('right',32)]:
            self.add_line(side+'-tyre-a',(x,34),(x,38))
            self.add_arc(side+'-tyre-b',(x,38),(x+8,38),radius_x=4,sweep=False)
            self.add_line(side+'-tyre-c',(x+8,38),(x+8,34))
            self.add_contour(side+'-tyre',side+'-tyre-a',side+'-tyre-b',side+'-tyre-c')
            self.relate('connect',side+'-tyre','body')
