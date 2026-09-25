"""Square Analog Wristwatch.

Symbol plan: Rounded square analog watch with short tapered straps and right crown. Lucide watch informs strap attachment and two hand angles. Face and straps share x=23 axis; crown intentionally adds right weight. Omit extra crown outline.
Keyshape VRECT_L; exact visible bounds (6, 2, 42, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e5a00966-2751-5a20-bbf0-40f2ea40a18a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/devices/device wearable smart watch_e5a00966-2751-5a20-bbf0-40f2ea40a18a.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'rounded-square-analog-watch-with-side-crown'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    categories = ('primitives', 'devices')
    aliases = ()
    keywords = ('square', 'analog', 'wristwatch')

    def build(self):
        self.run('face-top',(12,12),(16,12),(30,12),(34,12))
        self.add_arc('face-tr',(34,12),(38,16),radius_x=4)
        self.run('face-right',(38,16),(38,24),(38,32))
        self.add_arc('face-br',(38,32),(34,36),radius_x=4)
        self.run('face-bottom',(34,36),(30,36),(16,36),(12,36))
        self.add_arc('face-bl',(12,36),(8,32),radius_x=4)
        self.add_line('face-left',(8,32),(8,16));self.add_arc('face-tl',(8,16),(12,12),radius_x=4)
        self.add_contour('face','face-top-1','face-top-2','face-top-3','face-tr','face-right-1','face-right-2','face-br','face-bottom-1','face-bottom-2','face-bottom-3','face-bl','face-left','face-tl',closed=True)
        for i in range(2):
            def q(x,y):return (x,y if i==0 else 48-y)
            self.add_polyline(f'strap-{i}',q(16,12),q(18,4),q(28,4),q(30,12));self.relate('connect',f'strap-{i}','face')
        self.add_polyline('hands',(23,21),(23,27),(29,22))
        self.add_line('crown',(38,24),(40,24));self.relate('connect','crown','face')

    def run(self,name,*points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(f'{name}-{i}',a,b)
