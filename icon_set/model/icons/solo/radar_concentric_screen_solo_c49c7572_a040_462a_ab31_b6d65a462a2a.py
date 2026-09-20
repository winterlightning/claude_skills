"""Radar concentric screen.

Construction reference: radar.
Reduced three rings to two to preserve clear radar bands at 48px.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = 'c49c7572-a040-462a-ab31-b6d65a462a2a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/radar_c49c7572-a040-462a-ab31-b6d65a462a2a.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'radar-concentric-screen-solo-c49c7572'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('radar-concentric-screen',)
    keywords = ('radar', 'concentric', 'screen')

    def build(self):
        # Concentric screen and range ring meet one northeast sweep at exact 3:4 nodes.
        path(self,'outer',(24,4),[('A',(36,8),20,20,True),('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(4,24),20,20,True),('A',(24,4),20,20,True)],True)
        path(self,'range',(24,14),[('A',(30,16),10,10,True),('A',(34,24),10,10,True),('A',(24,34),10,10,True),('A',(14,24),10,10,True),('A',(24,14),10,10,True)],True)
        self.add_polyline('sweep',(24,24),(30,16),(36,8))
        self.relate('connect','outer','sweep')
        self.relate('connect','range','sweep')
