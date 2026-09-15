"""pot: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dcc7af24-9bec-4d53-bd95-0a77208b26b9'
SOURCE_PATH = 'pictographic-primitives/furnitures/pot_dcc7af24-9bec-4d53-bd95-0a77208b26b9.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Pot(Solo48):
    icon_id = 'pot'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('pot', 'furnitures')

    def build(self):
        # Plan: SQUARE; smooth elliptical lid and handle; preserve the left spout and directional kettle body.
        # Reference: Geometric lid and coherent handle curves.
        self.add_arc('base-left',(10,42),(6,38),radius_x=4)
        self.add_bezier('body-left',(6,38),((6,33),(7,28),(8,23)))
        self.add_polyline('rim',(8,23),(6,19),(31,19))
        self.add_bezier('body-right',(31,19),((32,24),(34,28),(34,33)))
        self.add_line('body-right-base',(34,33),(34,38))
        self.add_arc('base-corner',(34,38),(30,42),radius_x=4)
        self.add_line('base',(30,42),(10,42))
        self.add_contour('body','base-left','body-left','rim-1','rim-2','body-right','body-right-base','base-corner','base',closed=True)
        self.contours=self.contours[1:]
        self.add_arc('lid-left',(10,19),(20,8),radius_x=10,radius_y=11)
        self.add_arc('lid-right',(20,8),(30,19),radius_x=10,radius_y=11)
        self.add_contour('lid','lid-left','lid-right')
        self.add_line('knob',(20,6),(20,8))
        self.add_bezier('handle',(31,19),((37,16),(42,20),(42,25)),((42,30),(38,33),(34,33)))
        self.relate('connect','handle','body')
        self.relate('connect','lid','body')
        self.relate('connect','knob','lid')
