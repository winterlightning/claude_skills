"""Smartphone bottom bezel.

Construction reference: smartphone.
Blank screen; preserves structural bottom bezel.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = '08a24aa4-c28b-421f-94e2-f810a7a98af1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/mobile phone house_08a24aa4-c28b-421f-94e2-f810a7a98af1.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'smartphone-bottom-bezel-solo-08a24aa4'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('smartphone-bottom-bezel',)
    keywords = ('smartphone', 'bottom', 'bezel')

    def build(self):
        # 8-unit bezel band; split wall endpoints create genuine divider joins.
        box(self,'phone',10,4,38,44,4,nodes=((10,36),(38,36)))
        self.add_line('bezel',(10,36),(38,36))
        self.relate('connect','phone','bezel')
