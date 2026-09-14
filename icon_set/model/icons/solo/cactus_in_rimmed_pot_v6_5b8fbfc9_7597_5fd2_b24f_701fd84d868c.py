# Variant of cactus-in-rimmed-pot-v5; parent file remains unchanged.
"""Larger, taller cactus arms with rounded tips; SQUARE (6,6)-(42,42) gives the branches more width. Unequal arm heights preserve organic asymmetry. Rimmed pot retained."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5b8fbfc9-7597-5fd2-b24f-701fd84d868c'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_5b8fbfc9-7597-5fd2-b24f-701fd84d868c.svg'
AUTHOR = 'gpt-6'

class CactusInRimmedPotVariant6(Solo48):
    icon_id = 'cactus-in-rimmed-pot-v6'
    variant_of = 'cactus-in-rimmed-pot-v5'
    variant_label = 'Raised arms with open space above rim'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/plants'
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self):
        # SQUARE centerline extremes (6,6)-(42,42).
        # Single-stroke upturned branches remove cramped double-wall forks.
        # Lowest detached branch rail y=17; pot rim y=26: nine-unit clearance.
        self.add_line('stem-top',(24,6),(24,14))
        self.add_line('stem-middle',(24,14),(24,17))
        self.add_line('stem-bottom',(24,17),(24,26))
        self.add_contour('stem','stem-top','stem-middle','stem-bottom')
        self.add_line('left-rise',(6,8),(6,13))
        self.add_arc('left-bend',(6,13),(10,17),radius_x=4,sweep=False)
        self.add_line('left-branch',(10,17),(24,17))
        self.add_contour('left-arm','left-rise','left-bend','left-branch')
        self.add_line('right-branch',(24,14),(38,14))
        self.add_arc('right-bend',(38,14),(42,10),radius_x=4,sweep=False)
        self.add_line('right-rise',(42,10),(42,6))
        self.add_contour('right-arm','right-branch','right-bend','right-rise')
        self.relate('connect','stem','left-arm')
        self.relate('connect','stem','right-arm')
        self.add_polyline('rim',(10,26),(24,26),(38,26),(38,34),(34,34),(14,34),(10,34),closed=True)
        self.add_polyline('pot',(14,34),(16,42),(32,42),(34,34))
        self.relate('connect','rim','pot')
        self.relate('connect','stem','rim')
