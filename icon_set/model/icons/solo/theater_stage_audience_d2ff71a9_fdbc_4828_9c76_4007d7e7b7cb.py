"""Theater Stage with Audience.
Plan: Stage roof and mirrored pulled curtains above a repeated row of three audience backs. Centerline extremes (4,8)-(44,40). Audience backs follow the source rear silhouettes, not detached-head figures.
Reference: Lucide theater: mirrored curtains and repeated open audience arches; human_ref/user.svg inspected for human context.
Reduction: Curtain lower folds and audience side extensions omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd2ff71a9-fdbc-4828-9c76-4007d7e7b7cb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/show theater play_d2ff71a9-fdbc-4828-9c76-4007d7e7b7cb.svg'
AUTHOR = 'gpt-6'


class Batch25Icon(Solo48):
    icon_id = 'theater-stage-audience'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    aliases = ()
    keywords = ('theater', 'stage', 'with', 'audience')

    def build(self):

        self.add_polyline('frame',(4,26),(4,8),(16,8),(32,8),(44,8),(44,26))
        self.add_arc('curtain-left',(16,8),(4,26),radius_x=12,radius_y=18)
        self.add_arc('curtain-right',(32,8),(44,26),radius_x=12,radius_y=18,sweep=False)
        for c in ('curtain-left','curtain-right'): self.relate('connect','frame',c)
        for i,x in enumerate((8,24,40)):
            self.add_arc(f'audience-{i}',(x-4,40),(x+4,40),radius_x=4)
