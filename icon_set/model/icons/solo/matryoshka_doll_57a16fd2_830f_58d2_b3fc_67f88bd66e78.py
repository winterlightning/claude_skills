"""A nesting doll with an egg-shaped body, inset face, and pointed scarf folds; no facial decoration.

Construction: Lucide user-round: circular face and simple curved body; supplied doll supplies scarf and silhouette.
Keyshape VRECT_L; centerline extremes are the visible bounds inset by 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '57a16fd2-830f-58d2-b3fc-67f88bd66e78'
SOURCE_PATH = 'pictographic-primitives/culture/batch-05/babushka_57a16fd2-830f-58d2-b3fc-67f88bd66e78.svg'


class MatryoshkaDoll(Solo48):
    icon_id = 'matryoshka-doll'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('matryoshka', 'babushka', 'nesting doll', 'russian', 'doll', 'toy', 'folk', 'souvenir')

    def build(self) -> None:
        self.add_arc("dome-right", (24,2), (40,30), radius_x=16, radius_y=28)
        self.add_arc("base-right", (40,30), (32,46), radius_x=8, radius_y=16)
        self.add_line("base", (32,46), (16,46))
        self.add_arc("base-left", (16,46), (8,30), radius_x=8, radius_y=16)
        self.add_arc("dome-left", (8,30), (24,2), radius_x=16, radius_y=28)
        self.add_contour("body", "dome-right", "base-right", "base", "base-left", "dome-left", closed=True)
        self.add_arc("face-right", (24,9), (24,23), radius_x=7)
        self.add_arc("face-left", (24,23), (24,9), radius_x=7)
        self.add_contour("face", "face-right", "face-left", closed=True)
        self.add_arc("scarf-left", (8,30), (24,23), radius_x=16, radius_y=7, sweep=False)
        self.add_arc("scarf-right", (24,23), (40,30), radius_x=16, radius_y=7, sweep=False)
        self.add_contour("scarf", "scarf-left", "scarf-right")
        self.relate("connect", "body", "scarf")
        self.relate("connect", "face", "scarf")
