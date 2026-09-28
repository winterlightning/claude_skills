"""Durga Face with Crown.

Plan: Front-facing circular lower jaw beneath a pointed three-lobed crown, with a central face mark. Reduce separate hair walls; preserve crown lobes and round human jaw. Shared human reference user.svg. Bounds (8,4)-(40,44).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '46bc9f00-cd07-432b-8f83-9015dc133b34'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__durga-face-with-crown/20260927T135945Z-thuan-mac-1/reference/durga puja face_46bc9f00-cd07-432b-8f83-9015dc133b34.svg'
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
        self.add_polyline('right',(40,16),(40,24),(40,32))
        self.add_arc('jaw',(40,32),(8,32),radius_x=16,radius_y=12)
        self.add_polyline('left',(8,32),(8,24))
        self.add_contour('portrait','crown-left','lobe-left',*[f'crown-top-{i}' for i in range(1,5)],'lobe-right','right-1','right-2','jaw','left-1',closed=True)
        self.contours=[c for c in self.contours if c.contour_id not in ['crown-top','right','left']]
        self.add_polyline('crown-band',(12,24),(24,24),(36,24));self.relate('connect','portrait','crown-band')
        self.add_dot('left-eye',(20,32))
        self.add_dot('right-eye',(28,32))
