"""Festival Bunting and Exhibition Barrier.
Plan: Two pennants hang on one cord above two barrier posts joined by a sagging rope. Mirror on x=24. Centerline extremes (4,8)-(44,40).
Reference: No useful local Lucide bunting match; mirrored repeated pennants and elliptical rope.
Reduction: Three flags reduced to two; small finial loops omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a66aea78-cf32-4763-9086-c7716f4a28d1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/museum exhibition_a66aea78-cf32-4763-9086-c7716f4a28d1.svg'
AUTHOR = 'gpt-6'


class Batch25Icon(Solo48):
    icon_id = 'festival-bunting-rope-barrier'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/entertainment"
    aliases = ()
    keywords = ('festival', 'bunting', 'and', 'exhibition', 'barrier')

    def build(self):

        self.add_polyline('cord',(4,8),(20,8),(28,8),(44,8))
        for i,x in enumerate((4,28)):
            self.add_polyline(f'flag-{i}',(x,8),(x+8,20),(x+16,8))
            self.relate('connect','cord',f'flag-{i}')
        self.add_line('post-left',(8,30),(8,40))
        self.add_line('post-right',(40,30),(40,40))
        self.add_arc('rope',(8,30),(40,30),radius_x=16,radius_y=5,sweep=False)
        self.relate('connect','rope','post-left')
        self.relate('connect','rope','post-right')
