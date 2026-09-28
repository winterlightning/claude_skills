"""Browser header window.

Construction reference: panel-top.
Two control dots replace tiny header dashes; no interior graphic.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = 'dd2e4d0c-a37f-4f00-aaeb-0f1973cb4cc5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/ui webpage bank_dd2e4d0c-a37f-4f00-aaeb-0f1973cb4cc5.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'browser-header-window-solo-dd2e4d0c'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('browser-header-window',)
    keywords = ('browser', 'header', 'window')

    def build(self):
        # Header height 18 gives the controls 9-unit vertical breathing room.
        box(self,'window',6,6,42,42,4,nodes=((6,24),(42,24)))
        self.add_line('header',(6,24),(42,24))
        self.relate('connect','window','header')
        for i,x in enumerate((16,26)):
            self.add_dot(f'control-{i}',(x,15))
