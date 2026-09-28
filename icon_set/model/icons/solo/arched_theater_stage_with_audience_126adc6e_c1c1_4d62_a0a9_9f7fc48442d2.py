"""Arched Theater Stage with Audience.

Plan: Large stage arch above two audience busts; remove outer rectangular frame and reduce three spectators to two. Shared human reference: round heads, open curved shoulders, exact 8 centerline gap. Bounds (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '126adc6e-c1c1-4d62-a0a9-9f7fc48442d2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/ramlila_126adc6e-c1c1-4d62-a0a9-9f7fc48442d2.svg'
AUTHOR = 'gpt-6'

class ArchedTheaterStageWithAudience(Solo48):
    icon_id = 'arched-theater-stage-with-audience'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('arched', 'theater', 'stage', 'with', 'audience')

    def build(self):
        self.add_arc('stage',(8,16),(40,16),radius_x=16,radius_y=12)
        for i,x in enumerate([14,34]):
         self.add_arc(f'head-{i}-r',(x,24),(x,32),radius_x=4)
         self.add_arc(f'head-{i}-l',(x,32),(x,24),radius_x=4)
         self.add_contour(f'head-{i}',f'head-{i}-r',f'head-{i}-l',closed=True)
         self.add_arc(f'shoulder-{i}-l',(x-6,44),(x,40),radius_x=6,radius_y=4)
         self.add_arc(f'shoulder-{i}-r',(x,40),(x+6,44),radius_x=6,radius_y=4)
         self.add_contour(f'shoulders-{i}',f'shoulder-{i}-l',f'shoulder-{i}-r')
