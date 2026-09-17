"""Airbrush Spray Gun.

Plan: Horizontal pointed nozzle, paint cup, trigger and angled grip. Upright cup replaces tilt; shared connection nodes retain physical tool. Bounds (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ad00d24-fd59-47d1-b4d4-68699424443b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/airbrush_8ad00d24-fd59-47d1-b4d4-68699424443b.svg'
AUTHOR = 'gpt-6'


class AirbrushSprayGun(Solo48):
    icon_id = 'airbrush-spray-gun'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hobbies'
    aliases = ()
    keywords = ('airbrush', 'spray', 'gun')

    def build(self):
        self.add_polyline('body',(4,28),(12,24),(24,24),(38,24))
        self.add_arc('rear',(38,24),(44,30),radius_x=6)
        self.add_polyline('grip',(44,30),(40,30),(44,40),(34,40),(30,32),(24,32),(12,32),(4,28))
        self.add_contour('airbrush','body-1','body-2','body-3','rear',*[f'grip-{i}' for i in range(1,8)],closed=True)
        self.contours=[c for c in self.contours if c.contour_id not in ['body','grip']]
        self.add_polyline('cup',(16,8),(32,8),(28,16),(24,16),(20,16),closed=True)
        self.add_line('cup-neck',(24,16),(24,24))
        self.relate('connect','cup','cup-neck')
        self.relate('connect','cup-neck','airbrush')
        self.add_arc('trigger',(24,32),(18,40),radius_x=6,radius_y=8)
        self.relate('connect','trigger','airbrush')
