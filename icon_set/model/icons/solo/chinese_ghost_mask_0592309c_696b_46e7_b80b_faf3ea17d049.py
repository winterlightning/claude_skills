"""Chinese Ghost Mask.

Plan: Broad curved hat band above a pointed mask with brow and nose. Remove small cheek and chin flourishes. Lucide drama informed facial reduction. Bounds (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0592309c-696b-46e7-b80b-faf3ea17d049'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/hungry ghost festival_0592309c-696b-46e7-b80b-faf3ea17d049.svg'
AUTHOR = 'gpt-6'

class ChineseGhostMask(Solo48):
    icon_id = 'chinese-ghost-mask'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/holidays"
    aliases = ()
    keywords = ('chinese', 'ghost', 'mask')

    def build(self):
        self.add_arc('hat-top',(8,8),(40,8),radius_x=16,radius_y=4)
        self.add_line('hat-right',(40,8),(36,16))
        self.add_arc('hat-bottom',(36,16),(12,16),radius_x=12,radius_y=4,sweep=False)
        self.add_line('hat-left',(12,16),(8,8))
        self.add_contour('hat','hat-top','hat-right','hat-bottom','hat-left',closed=True)
        self.add_line('face-left',(12,16),(12,28))
        self.add_arc('jaw-left',(12,28),(24,44),radius_x=12,radius_y=16,sweep=False)
        self.add_arc('jaw-right',(24,44),(36,28),radius_x=12,radius_y=16,sweep=False)
        self.add_line('face-right',(36,28),(36,16))
        self.add_contour('face','face-left','jaw-left','jaw-right','face-right')
        self.relate('connect','hat','face')
        self.add_polyline('brow',(21,24),(24,24),(27,24));self.add_line('nose',(24,24),(24,32));self.relate('connect','brow','nose')
