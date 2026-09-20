"""Desktop monitor.

Construction reference: monitor.
Empty screen: excludes the independent currency, arrow or media control.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = '0005e7b2-b6eb-47bb-9376-770c2522288d'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/monitor upload_0005e7b2-b6eb-47bb-9376-770c2522288d.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'desktop-monitor-solo-0005e7b2'
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
