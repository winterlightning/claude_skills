"""Stacked Cup Pyramid.

Plan: Three inverted cups in two tiers replace six tiny cups. Shared contacts form one pyramid outline and interior seams. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0ba24c61-a3ec-41f8-986f-d11b520339e6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/sport stacking_0ba24c61-a3ec-41f8-986f-d11b520339e6.svg'
AUTHOR = 'gpt-6'

class StackedCupPyramid(Solo48):
    icon_id = 'stacked-cup-pyramid'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hobbies'
    aliases = ()
    keywords = ('stacked', 'cup', 'pyramid')

    def build(self):
        self.add_polyline('pyramid',(16,6),(32,6),(36,24),(42,42),(24,42),(6,42),(12,24),closed=True)
        self.add_polyline('tier',(12,24),(24,24),(36,24))
        self.add_line('division',(24,24),(24,42))
        self.relate('connect','pyramid','tier');self.relate('connect','pyramid','division');self.relate('connect','tier','division')
