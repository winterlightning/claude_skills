"""Saint Basil's Cathedral. Rebuilt from the supplied silhouette."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aadc2bb4-c5a5-468e-ad1c-a8d76afc257f'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-01/saint basils cathderal_aadc2bb4-c5a5-468e-ad1c-a8d76afc257f.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'saint-basils-cathedral'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('saint basil', 'moscow', 'russia', 'cathedral', 'onion dome', 'landmark', 'church', 'religion')

    def build(self):
        self.add_line("base-1", (8,31), (8,46))
        self.add_line("base-2", (8,46), (40,46))
        self.add_line("base-3", (40,46), (40,31))
        self.add_arc("right-lower", (40,31), (43,25), radius_x=3, radius_y=6, sweep=False)
        self.add_arc("right-upper", (43,25), (38,17), radius_x=5, radius_y=8, sweep=False)
        self.add_arc("right-inner", (38,17), (33,25), radius_x=5, radius_y=8, sweep=False)
        self.add_line("shoulder-right-1", (33, 25), (33, 34))
        self.add_line("shoulder-right-2", (33, 34), (28, 28))
        self.add_line("shoulder-right-3", (28, 28), (28, 22))
        self.add_arc("middle-right", (28,22), (24,2), radius_x=11, radius_y=13, sweep=False)
        self.add_arc("middle-left", (24,2), (20,22), radius_x=11, radius_y=13, sweep=False)
        self.add_line("shoulder-left-1", (20, 22), (20, 28))
        self.add_line("shoulder-left-2", (20, 28), (15, 34))
        self.add_line("shoulder-left-3", (15, 34), (15, 25))
        self.add_arc("left-inner", (15,25), (10,17), radius_x=5, radius_y=8, sweep=False)
        self.add_arc("left-upper", (10,17), (5,25), radius_x=5, radius_y=8, sweep=False)
        self.add_arc("left-lower", (5,25), (8,31), radius_x=3, radius_y=6, sweep=False)
        self.add_contour("outline", "base-1", "base-2", "base-3", "right-lower", "right-upper", "right-inner", "shoulder-right-1", "shoulder-right-2", "shoulder-right-3", "middle-right", "middle-left", "shoulder-left-1", "shoulder-left-2", "shoulder-left-3", "left-inner", "left-upper", "left-lower", closed=True)
