"""wine-glass: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f90eeb6e-787b-5f51-8bb0-0f4ffe811c20'
SOURCE_PATH = 'pictographic-primitives/drinks/wine glass_f90eeb6e-787b-5f51-8bb0-0f4ffe811c20.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class WineGlass(Solo48):
    icon_id = 'wine-glass'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    categories = ('drinks', 'primitives')
    aliases = ()
    keywords = ('wine', 'glass', 'drinks')

    def build(self):
        # Plan: VRECT_L; mirrored bowl, exact shared stem attachment and centered foot.
        # Reference: Geometric ellipse-to-wall tangency.
        self.add_line('rim',(11,4),(37,4))
        self.add_bezier('right-wall',(37,4),((38,8),(40,12),(40,17)))
        self.add_arc('bowl-right',(40,17),(24,29),radius_x=16,radius_y=12)
        self.add_arc('bowl-left',(24,29),(8,17),radius_x=16,radius_y=12)
        self.add_bezier('left-wall',(8,17),((8,12),(10,8),(11,4)))
        self.add_contour('bowl','rim','right-wall','bowl-right','bowl-left','left-wall',closed=True)
        self.add_line('stem',(24,29),(24,44))
        self.add_line('foot',(13,44),(35,44))
        self.relate('connect','stem','bowl')
        self.relate('connect','stem','foot')
