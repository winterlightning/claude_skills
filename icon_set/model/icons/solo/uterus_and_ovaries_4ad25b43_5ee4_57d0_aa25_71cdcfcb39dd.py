"""Uterus and Ovaries.

Plan: Central pear-shaped uterus and paired ovaries with arched fallopian tubes; simplify double canal to an open stem. Bounds (4,8)-(44,40). No useful Lucide anatomy match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ad25b43-5ee4-57d0-aa25-71cdcfcb39dd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/pregnancy ovary_4ad25b43-5ee4-57d0-aa25-71cdcfcb39dd.svg'
AUTHOR = 'gpt-6'


class UterusAndOvaries(Solo48):
    icon_id = 'uterus-and-ovaries'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('uterus', 'and', 'ovaries')

    def build(self):
        self.add_arc('uterus-top',(16,16),(32,16),radius_x=8)
        self.add_arc('uterus-r',(32,16),(24,30),radius_x=8,radius_y=14)
        self.add_arc('uterus-l',(24,30),(16,16),radius_x=8,radius_y=14)
        self.add_contour('uterus','uterus-top','uterus-r','uterus-l',closed=True)
        self.add_line('cervix',(24,30),(24,40))
        self.relate('connect','uterus','cervix')
        for p,x in [('left',7),('right',41)]:
            self.add_arc(p+'-ovary-top',(x-3,28),(x+3,28),radius_x=3)
            self.add_arc(p+'-ovary-bottom',(x+3,28),(x-3,28),radius_x=3)
            self.add_contour(p+'-ovary',p+'-ovary-top',p+'-ovary-bottom',closed=True)
        self.add_arc('tube-l',(4,16),(16,16),radius_x=6,sweep=True)
        self.add_arc('tube-r',(32,16),(44,16),radius_x=6,sweep=True)
        self.relate('connect','uterus','tube-l')
        self.relate('connect','uterus','tube-r')
