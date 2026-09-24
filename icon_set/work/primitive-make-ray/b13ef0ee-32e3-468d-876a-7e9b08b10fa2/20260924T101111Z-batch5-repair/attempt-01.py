"""A person rides an escalator rising right, with a direction arrow below.

Symbol plan: one round detached head aligns with the vertical upper torso;
the torso and arms meet exact nodes on the sloped rail. The escalator is a
single thick diagonal band and the detached arrow points right. Human style
references: human_ref/full_body_ref.png and human_ref/user.svg; the head
radius is 4 at (20,10), and torso starts at (20,22), giving exactly 8 units
centerline and 4 units ink head-to-body clearance. Lucide arrow-right informed
the direction mark. The escalator rise is intentional asymmetry.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b13ef0ee-32e3-468d-876a-7e9b08b10fa2"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/moving walkway_b13ef0ee-32e3-468d-876a-7e9b08b10fa2.svg"
AUTHOR = "gpt-6"


class PersonOnRisingEscalator(Solo48):
    icon_id = "person-on-rising-escalator"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/escalators"
    aliases = ("moving walkway rider", "person riding escalator")
    keywords = ("person", "up", "stairs", "direction")

    def build(self) -> None:
        self.add_arc("head-right", (20, 6), (20, 14), radius_x=4, sweep=True)
        self.add_arc("head-left", (20, 14), (20, 6), radius_x=4, sweep=True)
        self.add_contour("head", "head-right", "head-left", closed=True)
        self.add_line("torso", (20, 22), (20, 29))
        # Single torso with one reaching arm; omit the enclosing rear arm pocket.
        self.add_line("right-arm", (20,22), (28,23))
        self.relate("connect", "torso", "right-arm")
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
        self.relate("connect", "right-arm", "rail-upper-middle")
        self.relate("connect", "right-arm", "rail-upper-right")

        self.add_line("direction-shaft", (35, 40), (42, 40))
        self.add_polyline("direction-head", (38, 38), (42, 40), (38, 42))
        self.relate("connect", "direction-shaft", "direction-head-1")
        self.relate("connect", "direction-shaft", "direction-head-2")
