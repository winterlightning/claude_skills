"""Infinity loop containing minus and plus signs.
Plan: HRECT_M gives horizontal room for both loops and marks.
Reduction: No subject components omitted; signs shortened to fit.
Construction: Lucide infinity reviewed for coherent loop curves; supplied reference governs the two signs.
Layout: The plus loop is wider to accommodate a recognizable cross with certified clearance."""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = 'ed08c4ae-cd2f-485c-a2ad-1642f69c286c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/arduino plus minus_ed08c4ae-cd2f-485c-a2ad-1642f69c286c.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'infinity-loop-with-plus-and-minus'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbol'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.HRECT_M.bounds_for(Profile.SOLO48)
    def build(self):
        # Left minus loop and slightly wider plus loop share one continuous crossing.
        self.add_bezier('left-top',(22,24),((22,16),(17,10),(12,10)),((7,10),(4,14),(4,20)))
        self.add_line('left-wall',(4,20),(4,28))
        self.add_bezier('left-bottom',(4,28),((4,34),(7,38),(12,38)),((17,38),(22,32),(22,24)))
        self.add_bezier('right-top',(22,24),((22,16),(31,10),(36,10)),((41,10),(44,14),(44,20)))
        self.add_line('right-wall',(44,20),(44,28))
        self.add_bezier('right-bottom',(44,28),((44,34),(41,38),(36,38)),((31,38),(22,32),(22,24)))
        # Keep straight sidewalls independent so exact eight-unit mark clearance is certifiable.
        for a,b in [('left-top','left-wall'),('left-wall','left-bottom'),('left-top','left-bottom'),('left-top','right-top'),('left-top','right-bottom'),('left-bottom','right-top'),('left-bottom','right-bottom'),('right-top','right-wall'),('right-wall','right-bottom'),('right-top','right-bottom')]:self.relate('connect',a,b)
        self.add_line('minus',(12,24),(13,24))
        self.add_line('plus-h',(31,24),(35,24))
        self.add_line('plus-v',(33,22),(33,26))
        self.relate('connect','plus-h','plus-v')
