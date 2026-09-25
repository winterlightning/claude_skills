"""Oval Party Celebration Balloon.
Plan: One inflated oval with a tapered tie point owns its bottom string attachment on the vertical axis. Extrema (10,4)-(38,44).
Reference: Lucide balloon: balloon contour meeting a single string.
Reduction: Small triangular knot omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '62e45ef0-9a2c-5eb6-b5cd-114f6ee097b4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/party balloon_62e45ef0-9a2c-5eb6-b5cd-114f6ee097b4.svg'
AUTHOR = 'gpt-6'


class Batch26Icon(Solo48):
    icon_id = 'oval-balloon-straight-string'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "events"
    categories = ("primitives", "events")
    aliases = ()
    keywords = ('oval', 'party', 'celebration', 'balloon')

    def build(self):

        self.add_bezier('balloon-right',(24,4),((32,4),(38,10),(38,18)),((38,26),(29,32),(24,34)))
        self.add_bezier('balloon-left',(24,34),((19,32),(10,26),(10,18)),((10,10),(16,4),(24,4)))
        self.add_contour('balloon','balloon-right','balloon-left',closed=True)
        self.add_line('string',(24,34),(24,44))
        self.relate('connect','balloon','string')
