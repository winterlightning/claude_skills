"""fragile-break: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '92fd8d38-d5e6-50e0-8460-12389b9969ac'
SOURCE_PATH = 'pictographic-primitives/shipping/fragile break_92fd8d38-d5e6-50e0-8460-12389b9969ac.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class FragileBreak(Solo48):
    icon_id = 'fragile-break'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    categories = ('primitives', 'shipping')
    aliases = ()
    keywords = ('fragile', 'break', 'shipping')

    def build(self):
        # Plan: VRECT_L; symmetric bowl and centered stem; retain the intentional crack.
        # Reference: Geometric wine bowl with a deliberate broken rim.
        self.add_polyline('right-rim',(29,4),(37,4))
        self.add_bezier('right-wall',(37,4),((38,8),(40,12),(40,17)))
        self.add_arc('bowl-right',(40,17),(24,29),radius_x=16,radius_y=12)
        self.add_arc('bowl-left',(24,29),(8,17),radius_x=16,radius_y=12)
        self.add_bezier('left-wall',(8,17),((8,12),(10,8),(11,4)))
        self.add_polyline('crack',(11,4),(21,4),(19,9),(25,13),(20,16))
        self.add_contour('bowl','right-rim-1','right-wall','bowl-right','bowl-left','left-wall','crack-1','crack-2','crack-3','crack-4')
        self.contours=self.contours[2:]
        self.add_line('stem',(24,29),(24,44))
        self.add_line('foot',(16,44),(32,44))
        self.relate('connect','stem','bowl')
        self.relate('connect','stem','foot')
