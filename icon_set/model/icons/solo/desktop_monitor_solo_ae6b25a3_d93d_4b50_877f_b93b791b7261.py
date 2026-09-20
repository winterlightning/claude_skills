"""Desktop monitor.

Construction reference: monitor.
Empty screen: excludes the independent currency, arrow or media control.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = 'ae6b25a3-d93d-4b50-877f-b93b791b7261'
SOURCE_PATH = 'pictographic-primitives/other/tv control pause_ae6b25a3-d93d-4b50-877f-b93b791b7261.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'desktop-monitor-solo-ae6b25a3'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('desktop-monitor',)
    keywords = ('desktop', 'monitor')

    def build(self):
        # Screen and foot share x=24; bottom edge is split at the stem.
        box(self,'screen',4,8,44,32,4,nodes=((24,32),))
        self.add_line('stem',(24,32),(24,40))
        self.add_polyline('foot',(14,40),(24,40),(34,40))
        self.relate('connect','screen','stem')
        self.relate('connect','stem','foot')
