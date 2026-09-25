"""Christmas Wreath with Bow.

Plan: Wreath ring partly hidden by two large rounded bow loops. Reduce doubled ring to a single broad outline. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aec631c3-6d2a-4e18-b57f-a16014347cf7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/door wreath_aec631c3-6d2a-4e18-b57f-a16014347cf7.svg'
AUTHOR = 'gpt-6'

class ChristmasWreathWithBow(Solo48):
    icon_id = 'christmas-wreath-with-bow'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('christmas', 'wreath', 'with', 'bow')

    def build(self):
        self.add_line('bow-l-top',(24,16),(12,6))
        self.add_arc('bow-l-end',(12,6),(12,18),radius_x=6,sweep=False)
        self.add_line('bow-l-bottom',(12,18),(24,16))
        self.add_contour('bow-left','bow-l-top','bow-l-end','bow-l-bottom',closed=True)
        self.add_line('bow-r-top',(24,16),(36,6))
        self.add_arc('bow-r-end',(36,6),(36,18),radius_x=6)
        self.add_line('bow-r-bottom',(36,18),(24,16))
        self.add_contour('bow-right','bow-r-top','bow-r-end','bow-r-bottom',closed=True)
        self.add_arc('ring-tl',(12,18),(8,26),radius_x=4,radius_y=8,sweep=False)
        self.add_arc('ring-bl',(8,26),(24,42),radius_x=16,sweep=False)
        self.add_arc('ring-br',(24,42),(40,26),radius_x=16,sweep=False)
        self.add_arc('ring-tr',(40,26),(36,18),radius_x=4,radius_y=8,sweep=False)
        self.add_contour('wreath','ring-tl','ring-bl','ring-br','ring-tr')
        for a,b in [('bow-left','bow-right'),('bow-left','wreath'),('bow-right','wreath')]:self.relate('connect',a,b)
