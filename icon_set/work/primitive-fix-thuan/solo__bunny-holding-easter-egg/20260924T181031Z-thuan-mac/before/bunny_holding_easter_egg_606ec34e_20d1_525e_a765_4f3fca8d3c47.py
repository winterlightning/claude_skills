"""Bunny Holding Easter Egg.

Plan: Front-facing bunny with two long ears holds an upright egg. Reduce whiskers and face details; ears become single broad strokes. Lucide rabbit informed long ears. Bounds (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '606ec34e-20d1-525e-a765-4f3fca8d3c47'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/easter egg bunny_606ec34e-20d1-525e-a765-4f3fca8d3c47.svg'
AUTHOR = 'gpt-6'

class BunnyHoldingEasterEgg(Solo48):
    icon_id = 'bunny-holding-easter-egg'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/holidays'
    aliases = ()
    keywords = ('bunny', 'holding', 'easter', 'egg')

    def build(self):
        pts=[(8,18),(20,18),(24,26),(14,36),(4,26),(8,18)]
        for i in range(5):self.add_arc(f'face-{i}',pts[i],pts[i+1],radius_x=10)
        self.add_contour('face',*[f'face-{i}' for i in range(5)],closed=True)
        for name,a,b in [('ear-left',(8,18),(8,8)),('ear-right',(20,18),(20,8)),('body',(14,36),(14,40))]:
         self.add_line(name,a,b);self.relate('connect','face',name)
        self.add_arc('egg-top',(32,32),(44,32),radius_x=6,radius_y=8)
        self.add_arc('egg-bottom',(44,32),(32,32),radius_x=6,radius_y=8)
        self.add_contour('egg','egg-top','egg-bottom',closed=True)
        self.add_line('paw',(24,26),(32,32));self.relate('connect','face','paw');self.relate('connect','egg','paw')
