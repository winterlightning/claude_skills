"""An open palm wears a rounded wrist bracelet; four fingers plus thumb, without palm creases.

Construction references: Lucide rose, heart, gem and hand as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2887055-760f-49bf-891b-ea35d76e023d'
SOURCE_PATH = 'pictographic-primitives/romance/lgbt bracelet hand_a2887055-760f-49bf-891b-ea35d76e023d.svg'
AUTHOR = 'gpt-6'


class OpenHandWithRoundedBracelet(Solo48):
    icon_id = 'open-hand-with-rounded-bracelet'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('hand', 'bracelet', 'wrist', 'palm', 'jewelry', 'gesture')

    def build(self) -> None:
        self.add_line('index-side',(12,26),(12,16))
        self.add_arc('index-tip',(12,16),(20,16),radius_x=4)
        self.add_line('middle-rise',(20,16),(20,12))
        self.add_arc('middle-tip',(20,12),(28,12),radius_x=4)
        self.add_line('middle-fall',(28,12),(28,14))
        self.add_arc('ring-tip',(28,14),(36,14),radius_x=4)
        self.add_line('ring-fall',(36,14),(36,18))
        self.add_arc('little-tip',(36,18),(44,18),radius_x=4)
        self.add_line('palm-r',(44,18),(40,32))
        self.add_line('thumb-side',(16,32),(4,24))
        self.add_arc('thumb-tip',(4,24),(12,24),radius_x=4)
        self.add_line('thumb-inner',(12,24),(12,26))
        self.add_contour('hand','thumb-side','thumb-tip','thumb-inner','index-side','index-tip','middle-rise','middle-tip','middle-fall','ring-tip','ring-fall','little-tip','palm-r')
        for x,y in [(20,16),(28,14),(36,18)]:
            n=f'finger-crease-{x}'
            self.add_line(n,(x,y),(x,24))
            self.relate('connect','hand',n)
        self.add_line('bracelet-top',(16,32),(40,32))
        self.add_arc('bracelet-r',(40,32),(40,40),radius_x=4)
        self.add_line('bracelet-bottom',(40,40),(16,40))
        self.add_arc('bracelet-l',(16,40),(16,32),radius_x=4)
        self.add_contour('bracelet','bracelet-top','bracelet-r','bracelet-bottom','bracelet-l',closed=True)
        self.relate('connect','hand','bracelet')
