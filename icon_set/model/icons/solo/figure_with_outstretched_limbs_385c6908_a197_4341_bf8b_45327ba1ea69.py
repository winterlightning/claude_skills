"""Human figure with limbs thrown wide. SQUARE (2,2)-(46,46). Lucide person-standing: ring head and single-stroke body; retained source asymmetric action pose, simplified outlined limbs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '385c6908-a197-4341-bf8b-45327ba1ea69'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/warrior_385c6908-a197-4341-bf8b-45327ba1ea69.svg'


class FigureWithOutstretchedLimbs(Solo48):
    icon_id = 'figure-with-outstretched-limbs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('figure', 'warrior', 'human', 'action', 'pose', 'dance', 'movement', 'person')

    def build(self) -> None:
        self.add_arc('head-top', (19, 7), (29, 7), radius_x=5, sweep=True)
        self.add_arc('head-bottom', (29, 7), (19, 7), radius_x=5, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('arms', (2,8), (20,22), (46,20))
        self.add_line('torso', (20,22), (18,32))
        self.add_polyline('legs', (2,46), (18,32), (34,38), (38,46))
        self.relate('connect', 'arms','torso')
        self.relate('connect', 'legs','torso')
