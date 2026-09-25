"""Durga Face with Nose Ring.

Plan: Disembodied almond eyes, small round forehead ornament, curved mouth and large right nose ring. Merge brows into eye outlines and remove the crowded nose dot. Shared human references inform minimal facial vocabulary. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '21d086a9-9520-4bd8-a1ad-5e4a483646a8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/navaratri_21d086a9-9520-4bd8-a1ad-5e4a483646a8.svg'
AUTHOR = 'gpt-6'

class DurgaFaceWithNoseRing(Solo48):
    icon_id = 'durga-face-with-nose-ring'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('durga', 'face', 'with', 'nose', 'ring')

    def build(self):
        self.add_arc('ornament-r',(24,6),(27,9),radius_x=3)
        self.add_arc('ornament-br',(27,9),(24,12),radius_x=3)
        self.add_arc('ornament-bl',(24,12),(21,9),radius_x=3)
        self.add_arc('ornament-l',(21,9),(24,6),radius_x=3)
        self.add_contour('ornament','ornament-r','ornament-br','ornament-bl','ornament-l',closed=True)
        for n,x,y in [('left-eye',12,24),('right-eye',34,22)]:
         self.add_arc(n+'-top',(x-6,y),(x+6,y),radius_x=6,radius_y=4)
         self.add_arc(n+'-bottom',(x+6,y),(x-6,y),radius_x=6,radius_y=4)
         self.add_contour(n,n+'-top',n+'-bottom',closed=True)
        self.add_arc('mouth',(18,38),(26,38),radius_x=4,sweep=False)
        self.add_line('mouth-ring',(26,38),(34,38))
        self.add_arc('ring-top',(34,38),(42,38),radius_x=4)
        self.add_arc('ring-bottom',(42,38),(34,38),radius_x=4)
        self.add_contour('ring','ring-top','ring-bottom',closed=True)
        self.relate('connect','mouth','mouth-ring');self.relate('connect','mouth-ring','ring')
