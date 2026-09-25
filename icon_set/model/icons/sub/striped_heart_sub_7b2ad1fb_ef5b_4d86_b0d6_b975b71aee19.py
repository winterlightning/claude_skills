"""Striped Heart: An upright heart has two rounded lobes, a deep central notch, and a pointed bottom. Two horizontal dividers cross the interior, forming three broad stacked bands.

Construction: Symmetric heart with broad rounded lobes; horizontal stripes meet the sides as true dividers.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7b2ad1fb-ef5b-4d86-b0d6-b975b71aee19'
SOURCE_PATH = 'pictographic-primitives/state/lgbt heart_7b2ad1fb-ef5b-4d86-b0d6-b975b71aee19.svg'
AUTHOR = 'gpt-6'


class StripedHeartSub(Sub32):
    icon_id = 'striped-heart-sub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('striped', 'heart', 'upright', 'rounded', 'lobes', 'deep', 'central', 'notch')

    def build(self):
        self.add_arc("left-inner",(16,8),(9,2),radius_x=7,radius_y=6,sweep=False)
        self.add_arc("left-outer",(9,2),(2,10),radius_x=7,radius_y=8,sweep=False)
        self.add_line("left-side",(2,10),(16,30))
        self.add_line("right-side",(16,30),(30,10))
        self.add_arc("right-outer",(30,10),(23,2),radius_x=7,radius_y=8,sweep=False)
        self.add_arc("right-inner",(23,2),(16,8),radius_x=7,radius_y=6,sweep=False)
        self.add_contour("heart","left-inner","left-outer","left-side","right-side","right-outer","right-inner",closed=True)
        self.add_line("stripe-upper",(2,10),(30,10))
        self.add_line("stripe-lower",(9,20),(23,20))
        self.relate("connect","heart","stripe-upper")
        self.relate("connect","heart","stripe-lower")
