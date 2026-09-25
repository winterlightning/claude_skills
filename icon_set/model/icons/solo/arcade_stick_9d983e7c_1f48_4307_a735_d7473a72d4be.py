"""Arcade Stick Controller, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9d983e7c-1f48-4307-a735-d7473a72d4be'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-01/control gear_9d983e7c-1f48-4307-a735-d7473a72d4be.svg'
AUTHOR = 'gpt-6'

class ArcadeStick(Solo48):
    icon_id = 'arcade-stick'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('arcade', 'arcade stick', 'joystick', 'controller', 'retro', 'fight stick', 'gaming', 'console')

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
        self.add_line('button',(34,30),(34,24))
        self.relate('connect','button','base')
