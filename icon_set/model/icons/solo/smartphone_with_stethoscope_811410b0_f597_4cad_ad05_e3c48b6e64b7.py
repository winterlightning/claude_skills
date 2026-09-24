"""medical app smartphone listen: standalone repair of supplied reference.

Plan: Phone inside U with chestpiece at lower right. Keyshape SQUARE.
Reduction: Shortened phone and lifted U to give the lower hose clearance; chestpiece uses radius-2 circle.
Construction references: local Lucide originals and atomic-debug: smartphone, stethoscope.

All geometry is authored for SOLO48; earlier runs remain unchanged.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "811410b0-f597-4cad-ad05-e3c48b6e64b7"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/medical app smartphone listen_811410b0-f597-4cad-ad05-e3c48b6e64b7.svg"
AUTHOR = "gpt-6"


class SmartphoneWithStethoscope(Solo48):
    icon_id = 'smartphone-with-stethoscope'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "medical/devices"
    aliases = ("medical app smartphone", "phone stethoscope")
    keywords = ("health", "telemedicine", "listen", "phone")

    def build(self) -> None:
        r = 3
        self.add_line("phone-top", (18, 6), (26, 6))
        self.add_arc("phone-ne", (26, 6), (29, 9), radius_x=r, sweep=True)
        self.add_line("phone-right", (29, 9), (29, 17))
        self.add_arc("phone-se", (29, 17), (26, 20), radius_x=r, sweep=True)
        self.add_line("phone-bottom", (26, 20), (18, 20))
        self.add_arc("phone-sw", (18, 20), (15, 17), radius_x=r, sweep=True)
        self.add_line("phone-left", (15, 17), (15, 9))
        self.add_arc("phone-nw", (15, 9), (18, 6), radius_x=r, sweep=True)
        self.add_contour("phone", "phone-top", "phone-ne", "phone-right", "phone-se", "phone-bottom", "phone-sw", "phone-left", "phone-nw", closed=True)

        self.add_line("u-left-stem", (6, 12), (6, 15))
        self.add_arc("u-left-bend", (6, 15), (22, 31), radius_x=16, sweep=False)
        self.add_arc("u-right-bend", (22, 31), (38, 15), radius_x=16, sweep=False)
        self.add_line("u-right-stem", (38, 15), (38, 12))
        self.add_contour("stethoscope-u", "u-left-stem", "u-left-bend", "u-right-bend", "u-right-stem")
        self.add_polyline("lower-tube", (22, 31), (22, 40), (38, 40))
        self.relate("connect", "u-left-bend", "lower-tube")
        self.relate("connect", "u-right-bend", "lower-tube")

        self.add_arc("chestpiece-top", (40, 38), (42, 40), radius_x=2, sweep=True)
        self.add_arc("chestpiece-right", (42, 40), (40, 42), radius_x=2, sweep=True)
        self.add_arc("chestpiece-bottom", (40, 42), (38, 40), radius_x=2, sweep=True)
        self.add_arc("chestpiece-left", (38, 40), (40, 38), radius_x=2, sweep=True)
        self.add_contour("chestpiece", "chestpiece-top", "chestpiece-right", "chestpiece-bottom", "chestpiece-left", closed=True)
        self.relate("connect", "lower-tube", "chestpiece-left")
