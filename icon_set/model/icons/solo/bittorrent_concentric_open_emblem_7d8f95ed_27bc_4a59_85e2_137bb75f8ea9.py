"""BitTorrent Cryptocurrency Logo.
Plan: Outer radius20 and middle radius11 share center (24,24). The inner radius3 curve is offset to (29,23) for an open counter. Circular ink radius22.
Reference: Supplied original; no useful exact local Lucide match. Shared axes and simple geometric construction.
Reduction: Broad band outlines reduced to three concentric open strokes; lower-right opening retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d8f95ed-27bc-4a59-85e2-137bb75f8ea9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/finance/virtual coin crypto bittorrent_7d8f95ed-27bc-4a59-85e2-137bb75f8ea9.svg'
AUTHOR = 'gpt-6'

class Batch30Icon(Solo48):
    icon_id = 'bittorrent-concentric-open-emblem'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "finance"
    categories = ("primitives", "finance")
    aliases = ()
    keywords = ('bittorrent', 'cryptocurrency', 'logo')

    def build(self):

        self.add_arc('outer',(24,44),(44,24),radius_x=20,large_arc=True,sweep=True)
        self.add_arc('middle',(24,35),(24,13),radius_x=11,sweep=True)
        self.add_line('middle-tail',(24,35),(34,35));self.relate('connect','middle','middle-tail')
        self.add_arc('inner',(29,26),(32,23),radius_x=3,large_arc=True,sweep=True)
