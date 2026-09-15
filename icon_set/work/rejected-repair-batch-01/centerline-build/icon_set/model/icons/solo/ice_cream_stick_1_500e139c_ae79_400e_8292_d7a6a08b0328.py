"""ice-cream-stick-1: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '500e139c-ae79-400e-8292-d7a6a08b0328'
SOURCE_PATH = 'pictographic-primitives/food/ice cream stick 1_500e139c-ae79-400e-8292-d7a6a08b0328.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class IceCreamStick1(Solo48):
    icon_id = 'ice-cream-stick-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('ice', 'cream', 'stick', 'food')

    def build(self):
        # Plan: VRECT_L; symmetric elliptical crest and centered stick.
        # Reference: Geometric half ellipse; retain source seam.
        self.add_arc('top',(8,18),(40,18),radius_x=16,radius_y=14)
        self.add_polyline('body',(40,18),(40,32),(8,32),(8,18))
        self.add_contour('outline','top','body-1','body-2','body-3',closed=True)
        self.contours.pop(0)
        self.add_line('seam',(8,18),(40,18))
        self.add_line('stick',(24,32),(24,44))
        self.relate('connect','seam','outline')
        self.relate('connect','stick','outline')
