"""moving walkway: standalone repair of supplied reference.

Plan: Person on rising escalator with right arrow. Keyshape SQUARE.
Reduction: Omitted both arms to remove enclosed arm pockets; retained detached head, torso, rising belt and right arrow.
Construction references: local Lucide originals and atomic-debug: none.
human_ref/full_body_ref.png: head center (20,10), radius 4; torso starts (20,22), exactly 8 centerline / 4 ink gap. Head and torso share x=20.
All geometry is authored for SOLO48; earlier runs remain unchanged.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "b13ef0ee-32e3-468d-876a-7e9b08b10fa2"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/moving walkway_b13ef0ee-32e3-468d-876a-7e9b08b10fa2.svg"
AUTHOR = "gpt-6"


class PersonOnRisingEscalator(Solo48):
    icon_id = 'person-on-rising-escalator'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("moving walkway rider", "person riding escalator")
    keywords = ("person", "up", "stairs", "direction")

    def build(self) -> None:
        self.add_arc("head-right", (20, 6), (20, 14), radius_x=4, sweep=True)
        self.add_arc("head-left", (20, 14), (20, 6), radius_x=4, sweep=True)
        self.add_contour("head", "head-right", "head-left", closed=True)
        self.add_line("torso", (20, 22), (20, 29))
        # Single torso with one reaching arm; omit the enclosing rear arm pocket.
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")

        self.add_line("rail-landing", (6, 33), (12, 33))
        self.add_line("rail-upper-left", (12, 33), (20, 29))
        self.add_line("rail-upper-middle", (20, 29), (28, 23))
        self.add_line("rail-upper-right", (28, 23), (32, 20))
        self.add_line("rail-top", (32, 20), (37, 20))
        self.add_arc("rail-round", (37, 20), (42, 25), radius_x=5, sweep=True)
        self.add_line("rail-right", (42, 25), (42, 26))
        self.add_line("rail-lower", (42, 26), (16, 42))
        self.add_line("rail-bottom", (16, 42), (6, 42))
        self.add_line("rail-left", (6, 42), (6, 33))
        self.add_contour("escalator", "rail-landing", "rail-upper-left", "rail-upper-middle", "rail-upper-right", "rail-top", "rail-round", "rail-right", "rail-lower", "rail-bottom", "rail-left", closed=True)
        self.relate("connect", "torso", "rail-upper-left")
        self.relate("connect", "torso", "rail-upper-middle")

        self.add_line("direction-shaft", (35, 40), (42, 40))
        self.add_polyline("direction-head", (38, 38), (42, 40), (38, 42))
        self.relate("connect", "direction-shaft", "direction-head-1")
        self.relate("connect", "direction-shaft", "direction-head-2")
