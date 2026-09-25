"""Hanging Party Bunting Flags.
Plan: Two strands each own two identical triangular pennants. Centerline extremes (6,6)-(42,42).
Reference: No useful local Lucide bunting match; shared widths, heights and repeated series.
Reduction: Three flags per strand reduced to two; opposing cord slopes retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f2d67049-8a96-4fa1-833b-0d4bada861a8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/party decoration 1_f2d67049-8a96-4fa1-833b-0d4bada861a8.svg'
AUTHOR = 'gpt-6'


class Batch25Icon(Solo48):
    icon_id = 'two-strands-party-bunting'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "events"
    categories = ("primitives", "events")
    aliases = ()
    keywords = ('hanging', 'party', 'bunting', 'flags')

    def build(self):
        # Each cord is a single slope; pennants share width=12 and drop=11.
        for row,(y,dy) in enumerate(((6,1),(32,-1))):
            nodes=[(6+12*i,y+dy*i) for i in range(4)]
            self.add_polyline(f'cord-{row}',*nodes)
            for i in (0,2):
                a,b=nodes[i],nodes[i+1]
                tip=(a[0]+6,a[1]+(11 if row==0 else 10))
                self.add_polyline(f'flag-{row}-{i}',a,tip,b)
                self.relate('connect',f'cord-{row}',f'flag-{row}-{i}')
