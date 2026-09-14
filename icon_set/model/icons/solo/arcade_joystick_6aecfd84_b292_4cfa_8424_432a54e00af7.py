"""Arcade Joystick, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6aecfd84-b292-4cfa-8424-432a54e00af7'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-01/control gear_6aecfd84-b292-4cfa-8424-432a54e00af7.svg'
AUTHOR = 'gpt-6'

class ArcadeJoystick(Solo48):
    icon_id = 'arcade-joystick'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/gaming'
    aliases = ()
    keywords = ('arcade', 'joystick', 'arcade stick', 'controller', 'retro', 'fight stick', 'gaming', 'control')

    def build(self):
        # HRECT_L: centerline extremes (4, 8, 44, 40); current SOLO48 contract.
        def circle(name, x, y, r):
            self.add_arc(name+'-a',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(name+'-b',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(name,name+'-a',name+'-b',closed=True)
        def arc(name,a,b,r,ry=None,sweep=True):
            self.add_arc(name,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(name,*pts):
            for i,(a,b) in enumerate(zip(pts,pts[1:]),1):
                self.add_line(f'{name}-{i}',a,b)
        circle('ball',16,14,6)
        self.add_line('shaft',(16,20),(16,30))
        self.add_polyline('base',(16,30),(44,30),(44,40),(4,40),(4,30),(16,30),closed=True)
        self.relate('connect','shaft','ball')
        self.relate('connect','shaft','base')
        self.add_polyline('button',(30,30),(30,22),(38,22),(38,30))
        self.relate('connect','button','base')
