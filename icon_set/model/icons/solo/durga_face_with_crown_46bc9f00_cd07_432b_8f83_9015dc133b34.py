"""Durga Face with Crown.

Plan: Front-facing circular lower jaw beneath a pointed three-lobed crown, with a central face mark. Reduce separate hair walls; preserve crown lobes and round human jaw. Shared human reference user.svg. Bounds (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '46bc9f00-cd07-432b-8f83-9015dc133b34'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/durga puja face_46bc9f00-cd07-432b-8f83-9015dc133b34.svg'
AUTHOR = 'gpt-6'

class DurgaFaceWithCrown(Solo48):
    icon_id = 'durga-face-with-crown'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('durga', 'face', 'with', 'crown')

    def build(self):
        self.add_line('crown-left',(8,24),(8,16))
        self.add_arc('lobe-left',(8,16),(16,8),radius_x=8)
        self.add_polyline('crown-top',(16,8),(18,10),(24,4),(30,10),(32,8))
        self.add_arc('lobe-right',(32,8),(40,16),radius_x=8)
        self.add_polyline('right',(40,16),(40,24),(36,24),(36,32))
        self.add_arc('jaw',(36,32),(12,32),radius_x=12)
        self.add_polyline('left',(12,32),(12,24),(8,24))
        self.add_contour('portrait','crown-left','lobe-left',*[f'crown-top-{i}' for i in range(1,5)],'lobe-right','right-1','right-2','right-3','jaw','left-1','left-2',closed=True)
        self.contours=[c for c in self.contours if c.contour_id not in ['crown-top','right','left']]
        self.add_polyline('crown-band',(12,24),(24,24),(36,24));self.relate('connect','portrait','crown-band')
        self.add_dot('face-mark',(24,32))
