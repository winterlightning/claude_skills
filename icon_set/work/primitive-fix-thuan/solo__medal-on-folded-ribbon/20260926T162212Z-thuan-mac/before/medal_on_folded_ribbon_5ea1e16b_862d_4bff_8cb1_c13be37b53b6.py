"""A ringed medal hangs from a broad folded neck ribbon; reduce thin folds.

Live keyshape centerlines: VRECT_L (8,4)-(40,44); SQUARE (6,6)-(42,42);
HRECT_L (4,8)-(44,40). Shared dimensions preserve paired proportions.
Lucide medal: geometric construction; supplied reference: subject identity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='5ea1e16b-862d-4bff-8cb1-c13be37b53b6'
SOURCE_PATH='pictographic-primitives/rewards/medal shine_5ea1e16b-862d-4bff-8cb1-c13be37b53b6.svg'
AUTHOR='gpt-6'

class MedalOnFoldedRibbon(Solo48):
    icon_id='medal-on-folded-ribbon'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'rewards'
    categories = ('rewards', 'primitives')
    aliases=()
    keywords=('award', 'reward', 'medal-on-folded-ribbon')
    def build(self) -> None:
        self.add_arc('disc-top',(19,19),(29,19),radius_x=13)
        self.add_arc('disc-upper-right',(29,19),(36,26),radius_x=13)
        self.add_arc('disc-right',(36,26),(37,31),radius_x=13)
        self.add_arc('disc-bottom',(37,31),(11,31),radius_x=13)
        self.add_arc('disc-left',(11,31),(12,26),radius_x=13)
        self.add_arc('disc-upper-left',(12,26),(19,19),radius_x=13)
        self.add_contour('medal','disc-top','disc-upper-right','disc-right','disc-bottom','disc-left','disc-upper-left',closed=True)
        self.add_polyline('ribbon',(12,26),(8,12),(14,4),(34,4),(40,12),(36,26))
        self.add_line('fold-left',(14,4),(19,19))
        self.add_line('fold-right',(34,4),(29,19))
        for fold in ['fold-left','fold-right']:
            self.relate('connect',fold,'medal')
            self.relate('connect',fold,'ribbon')
        self.add_arc('ring-right',(24,27),(24,35),radius_x=4)
        self.add_arc('ring-left',(24,35),(24,27),radius_x=4)
        self.add_contour('ring','ring-right','ring-left',closed=True)
        self.relate('connect','medal','ribbon')
