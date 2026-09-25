"""A robot has a domed head, a tapered box torso, curved arms ending in round hands, and two straight legs with flat feet. A small chevron marks its face, while a circle and short stroke mark its chest.

VRECT_XL visible bounds (6,2)-(42,46); domed head, box torso, curved arms and flat feet. Face chevron and second chest mark omitted for clarity. Lucide bot informed simple robotic body geometry; mirrored limbs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be97f138-9a4e-4f13-b4f3-9aaa3afe48ea'
SOURCE_PATH = 'pictographic-primitives/science/fiction robot_be97f138-9a4e-4f13-b4f3-9aaa3afe48ea.svg'
AUTHOR = 'gpt-6'

class DomedHumanoidRobot(Solo48):
    icon_id = 'domed-humanoid-robot'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('robot', 'android', 'humanoid', 'machine', 'fiction', 'technology')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('head-dome',(16,14),(32,14),radius_x=8,radius_y=10)
        self.add_polyline('torso',(16,14),(32,14),(32,30),(28,34),(20,34),(16,30),closed=True)
        self.relate('connect','head-dome','torso')
        for side in (-1,1):
            x=24+side*8
            self.add_arc(f'arm-{side}',(x,14),(24+side*16,30),radius_x=8,radius_y=16,sweep=side==1)
            self.relate('connect',f'arm-{side}','torso')
            self.add_polyline(f'leg-{side}',(24+side*4,34),(24+side*4,44),(24+side*10,44))
            self.relate('connect',f'leg-{side}','torso')
        self.add_dot('chest',(24,24))
