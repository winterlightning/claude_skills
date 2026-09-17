"""Decorative String Lights.

Plan: Three teardrop lights hang from a sagging cord. Shared bulb geometry and pitch 16; remove socket rings and outward tilts. Bounds (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc09485d-3e5e-5c26-9e38-518f2297846d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/christmas lights_bc09485d-3e5e-5c26-9e38-518f2297846d.svg'
AUTHOR = 'gpt-6'

class DecorativeStringLights(Solo48):
    icon_id = 'decorative-string-lights'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/holidays"
    aliases = ()
    keywords = ('decorative', 'string', 'lights')

    def build(self):
        self.add_polyline('cord',(4,8),(8,10),(24,16),(40,10),(44,8))
        for i,x,y in [(0,8,20),(1,24,24),(2,40,20)]:
         self.add_line(f'socket-{i}',(x,y-(8 if i==1 else 10)),(x,y))
         self.add_arc(f'bulb-{i}-tr',(x,y),(x+4,y+4),radius_x=4)
         self.add_arc(f'bulb-{i}-br',(x+4,y+4),(x,y+16),radius_x=4,radius_y=12)
         self.add_arc(f'bulb-{i}-bl',(x,y+16),(x-4,y+4),radius_x=4,radius_y=12)
         self.add_arc(f'bulb-{i}-tl',(x-4,y+4),(x,y),radius_x=4)
         self.add_contour(f'bulb-{i}',*[f'bulb-{i}-{s}' for s in ['tr','br','bl','tl']],closed=True)
         self.relate('connect','cord',f'socket-{i}');self.relate('connect',f'socket-{i}',f'bulb-{i}')
