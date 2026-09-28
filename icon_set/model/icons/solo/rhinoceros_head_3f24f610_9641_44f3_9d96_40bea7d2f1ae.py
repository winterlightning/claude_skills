'Rebuilt the rhino profile around one broad horn and a flowing jaw; removed cramped secondary notches.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f24f610-9641-44f3-9d96-40bea7d2f1ae'
SOURCE_PATH = 'pictographic-primitives/animals/rhinoceros head_3f24f610-9641-44f3-9d96-40bea7d2f1ae.svg'
AUTHOR = 'gpt-6'


class RhinoHeadProfile(Solo48):
    icon_id = 'rhino-head-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("animals", "primitives")
    aliases = ()
    keywords = ('rhino', 'rhinoceros', 'head', 'horn', 'ears', 'profile', 'animal', 'wildlife')

    def build(self) -> None:
        # Broad primary horn and an open forehead replace crowded stacked notches.
        self.add_bezier('forehead',(40,6),((35,12),(30,16),(25,18)))
        self.add_line('bridge',(25,18),(20,25))
        self.add_bezier('horn-inner',(20,25),((15,21),(10,12),(8,4)))
        self.add_line('horn-outer',(8,4),(8,28))
        self.add_bezier('nose',(8,28),((8,32),(12,32),(12,34)))
        self.add_bezier('jaw-left',(12,34),((8,34),(8,38),(8,39)),((8,42),(12,44),(16,44)))
        self.add_line('jaw-bottom',(16,44),(29,44))
        self.add_bezier('jaw-right',(29,44),((35,44),(39,40),(40,35)))
        self.add_contour('profile','forehead','bridge','horn-inner','horn-outer','nose','jaw-left','jaw-bottom','jaw-right')
        self.add_dot('eye',(29,28))
