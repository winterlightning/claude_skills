'A right-facing fish inside a rimmed aquarium tank.\nPlan: SQUARE matches the tank enclosure.\nReduction: Omitted the crowded floor wave and fish fins; rebuilt the fish as an oval body with an open forked tail.\nConstruction: Lucide fish: a coherent directional body and forked tail; reduced detail for the enclosing tank.'

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48


SOURCE_ICON_ID = "4fb53005-bb60-46fd-bc0e-7ea549f599e9"
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/aquarium_4fb53005-bb60-46fd-bc0e-7ea549f599e9.svg'
AUTHOR = 'gpt-6'


class FishInAnAquariumTank(Solo48):
    icon_id = "fish-in-an-aquarium-tank"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/aquatic"
    aliases = ("fish-swimming-in-a-tank", "aquarium-fish")
    keywords = ("aquarium", "fish", "tank", "water", "pet", "swimming")

    def build(self) -> None:
        # A rounded-square tank owns its rim; an oval fish and open tail sit inside.
        self.add_line("tank-top", (10, 6), (38, 6))
        self.add_arc("tank-top-right", (38, 6), (42, 10), radius_x=4)
        self.add_line("tank-right", (42, 10), (42, 38))
        self.add_arc("tank-bottom-right", (42, 38), (38, 42), radius_x=4)
        self.add_line("tank-bottom", (38, 42), (10, 42))
        self.add_arc("tank-bottom-left", (10, 42), (6, 38), radius_x=4)
        self.add_line("tank-left", (6, 38), (6, 10))
        self.add_arc("tank-top-left", (6, 10), (10, 6), radius_x=4)
        self.add_contour(
            "tank-outline",
            "tank-top",
            "tank-top-right",
            "tank-right",
            "tank-bottom-right",
            "tank-bottom",
            "tank-bottom-left",
            "tank-left",
            "tank-top-left",
            closed=True,
        )

        self.add_line("upper-rim", (6, 14), (42, 14))
        self.relate("connect", "tank-outline", "upper-rim")

        # Omit the crowded floor wave; use a clear oval fish and open forked tail.
        self.add_arc('fish-top',(19,28),(33,28),radius_x=7,radius_y=5)
        self.add_arc('fish-bottom',(33,28),(19,28),radius_x=7,radius_y=5)
        self.add_contour('fish-body','fish-top','fish-bottom',closed=True)
        self.add_polyline('fish-tail',(15,24),(19,28),(15,32))
        self.relate('connect','fish-body','fish-tail')
