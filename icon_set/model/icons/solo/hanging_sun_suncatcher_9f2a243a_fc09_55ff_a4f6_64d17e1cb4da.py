"""Hanging Sun Suncatcher.

Plan: Hanging sun with bead, four attached rays and long lower ray. Circle and rays use shared axes. Bounds (8,4)-(40,44). Lucide sun informs radial construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f2a243a-fc09-55ff-a4f6-64d17e1cb4da'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/suncather_9f2a243a-fc09-55ff-a4f6-64d17e1cb4da.svg'
AUTHOR = 'gpt-6'

class HangingSunSuncatcher(Solo48):
    icon_id = 'hanging-sun-suncatcher'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/hobbies"
    aliases = ()
    keywords = ('hanging', 'sun', 'suncatcher')

    def build(self):
        self.add_line('cord',(24,4),(24,8))
        self.add_arc('bead-r',(24,8),(24,16),radius_x=4)
        self.add_arc('bead-l',(24,16),(24,8),radius_x=4)
        self.add_contour('bead','bead-r','bead-l',closed=True)
        self.add_line('link',(24,16),(24,20))
        points=[(24,20),(32,28),(24,36),(16,28),(24,20)]
        for i in range(4):self.add_arc(f'ring-{i}',points[i],points[i+1],radius_x=8)
        self.add_contour('sun',*[f'ring-{i}' for i in range(4)],closed=True)
        for name,a,b in [('ray-left',(16,28),(8,28)),('ray-right',(32,28),(40,28)),('ray-bottom',(24,36),(24,44))]:
         self.add_line(name,a,b);self.relate('connect','sun',name)
        self.relate('connect','cord','bead');self.relate('connect','bead','link');self.relate('connect','link','sun')
