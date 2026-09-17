"""Finger Tapping Smartwatch Screen.

Symbol plan: A tapping hand occludes a watch face on a horizontal wrist. Shared human-reference user.svg/full_body_ref.png informs simple anatomy; Lucide hand/watch informs rounded finger and watch. No detached head or torso. Omit background thumb crease and foreground thumb projection, which cannot preserve clearance beside the wrist; keep the extended index and curved palm.
Keyshape SQUARE; exact visible bounds (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5b432e2-8ae4-5f6e-900c-3683b1b01307'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/devices/wearable smart watch touch_c5b432e2-8ae4-5f6e-900c-3683b1b01307.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'finger-tapping-watch-on-horizontal-wrist'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/devices'
    aliases = ()
    keywords = ('finger', 'tapping', 'smartwatch', 'screen')

    def build(self):
        self.add_line('watch-bottom-left',(16,26),(12,26));self.add_arc('watch-bl',(12,26),(8,22),radius_x=4)
        self.add_line('watch-left',(8,22),(8,10));self.add_arc('watch-tl',(8,10),(12,6),radius_x=4)
        self.add_line('watch-top',(12,6),(28,6));self.add_arc('watch-tr',(28,6),(32,10),radius_x=4)
        self.add_line('watch-right',(32,10),(32,22));self.add_arc('watch-br',(32,22),(28,26),radius_x=4)
        self.add_line('watch-bottom-right',(28,26),(24,26))
        self.add_contour('watch','watch-bottom-left','watch-bl','watch-left','watch-tl','watch-top','watch-tr','watch-right','watch-br','watch-bottom-right')
        self.add_polyline('wrist-upper',(6,10),(8,10));self.add_polyline('wrist-lower',(6,22),(8,22))
        for part in ['wrist-upper','wrist-lower']:self.relate('connect',part,'watch')
        self.add_line('fist-top',(32,10),(38,10));self.add_arc('fist-tr',(38,10),(42,14),radius_x=4)
        self.add_line('fist-right',(42,14),(42,18));self.add_arc('fist-br',(42,18),(38,22),radius_x=4)
        self.add_line('fist-bottom',(38,22),(32,22));self.add_contour('fist','fist-top','fist-tr','fist-right','fist-br','fist-bottom');self.relate('connect','fist','watch')
        self.run('finger-left',(16,42),(16,26),(16,22))
        self.add_arc('finger-tip',(16,22),(24,22),radius_x=4)
        self.run('finger-right',(24,22),(24,26),(24,34),(32,34))
        self.add_arc('palm',(32,34),(40,42),radius_x=8)
        self.add_contour('hand','finger-left-1','finger-left-2','finger-tip','finger-right-1','finger-right-2','finger-right-3','palm')
        self.relate('connect','hand','watch')

    def run(self,name,*points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(f"{name}-{i}",a,b)
