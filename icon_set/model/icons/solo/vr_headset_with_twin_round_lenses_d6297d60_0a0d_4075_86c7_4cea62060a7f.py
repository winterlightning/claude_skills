"""Virtual Reality Headset.

Symbol plan: VR viewer with two round lenses and integral nose notch. Lens circles use shared radius3 and symmetric centers. Lucide glasses informs lens pair and bridge. Remove top double strap to prioritize optical openings; shallow raised top retained by main shell.
Keyshape HRECT_L; exact visible bounds (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd6297d60-0a0d-4075-86c7-4cea62060a7f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/devices/wearable google cardboard_d6297d60-0a0d-4075-86c7-4cea62060a7f.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'vr-headset-with-twin-round-lenses'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    categories = ('primitives', 'devices')
    aliases = ()
    keywords = ('virtual', 'reality', 'headset')

    def build(self):
        self.add_line('top',(8,8),(40,8));self.add_arc('tr',(40,8),(44,12),radius_x=4)
        self.add_line('right',(44,12),(44,36));self.add_arc('br',(44,36),(40,40),radius_x=4)
        self.add_line('bottom-r',(40,40),(32,40));self.add_arc('notch-r',(32,40),(28,36),radius_x=4)
        self.add_arc('nose',(28,36),(20,36),radius_x=4,sweep=False)
        self.add_arc('notch-l',(20,36),(16,40),radius_x=4);self.add_line('bottom-l',(16,40),(8,40))
        self.add_arc('bl',(8,40),(4,36),radius_x=4);self.add_line('left',(4,36),(4,12));self.add_arc('tl',(4,12),(8,8),radius_x=4)
        self.add_contour('body','top','tr','right','br','bottom-r','notch-r','nose','notch-l','bottom-l','bl','left','tl',closed=True)
        for i,x in enumerate((16,32)):self.circle(f'lens-{i}',x,21,3)

    def circle(self,name,cx,cy,r):
        points=[(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
        names=[]
        for i,start in enumerate(points):
            part=f'{name}-{i}';self.add_arc(part,start,points[(i+1)%4],radius_x=r);names.append(part)
        self.add_contour(name,*names,closed=True)
