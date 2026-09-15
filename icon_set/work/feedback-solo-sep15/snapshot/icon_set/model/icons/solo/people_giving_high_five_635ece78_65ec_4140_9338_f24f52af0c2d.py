"""Two front-facing people raise their inner arms until their hands meet above the center. Their outer shoulders extend sideways, and three short rays emphasize the joined hands between the circular heads.
Lucide users head and shoulder construction. Two people share raised hands; outer shoulders and torso strokes retained. Three rays reduced to one central dot for space. Bilaterally symmetric.
SQUARE: centerline extremes (6,6)-(42,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '635ece78-65ec-4140-9338-f24f52af0c2d'
SOURCE_PATH = 'pictographic-primitives/work/workflow teamwork user high five_635ece78-65ec-4140-9338-f24f52af0c2d.svg'
AUTHOR = 'gpt-6'


class PeopleGivingHighFive(Solo48):
    icon_id = 'people-giving-high-five'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('people', 'highfive', 'teamwork', 'celebration', 'greeting', 'contact')

    def build(self) -> None:
        self.add_arc('head-left-top', (6, 16), (14, 16), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('head-left-bottom', (14, 16), (6, 16), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('head-left', 'head-left-top', 'head-left-bottom', closed=True)
        self.add_arc('head-right-top', (34, 16), (42, 16), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('head-right-bottom', (42, 16), (34, 16), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('head-right', 'head-right-top', 'head-right-bottom', closed=True)
        self.add_line('outer-left', (6, 42), (6, 38))
        self.add_arc('shoulder-left', (6, 38), (14, 34), radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_line('raised-left', (14, 34), (24, 20))
        self.add_line('raised-right', (24, 20), (34, 34))
        self.add_arc('shoulder-right', (34, 34), (42, 38), radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_line('outer-right', (42, 38), (42, 42))
        self.add_contour('people', 'outer-left', 'shoulder-left', 'raised-left', 'raised-right', 'shoulder-right', 'outer-right', closed=False)
        self.add_line('body-left', (14, 34), (14, 42))
        self.relate("connect", 'body-left', 'people')
        self.add_line('body-right', (34, 34), (34, 42))
        self.relate("connect", 'body-right', 'people')
        self.add_dot('contact-ray', (24, 6))
