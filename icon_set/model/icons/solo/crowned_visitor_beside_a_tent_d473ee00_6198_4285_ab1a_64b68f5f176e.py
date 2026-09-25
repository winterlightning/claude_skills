"""Amusement Park King and Tent.

Plan: Crowned visitor and companion tent; preserve the natural scene; omit neckline.
Construction reference: human_ref/user.svg: circular face and curved shoulders; tent is a companion object.
Keyshape HRECT_L: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd473ee00-6198-4285-ab1a-64b68f5f176e'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/amusement park_d473ee00-6198-4285-ab1a-64b68f5f176e.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'crowned-visitor-beside-a-tent'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('amusement', 'park', 'king', 'and', 'tent')

    def build(self):

        self.path('crown',[(26,8),(30,12),(34,8),(38,12),(42,8),(40,20),(28,20)],True)
        self.arc('face',(28,20),(40,20),6,sweep=False)
        self.relate('connect','crown','face')
        self.arc('shoulders',(24,40),(44,40),10,6)
        self.path('tent',[(4,26),(10,16),(16,26),(4,26),(6,38),(14,38),(16,26)])

    def circle(self, name, x, y, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r, radius_y=ry)
        self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r, radius_y=ry)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def path(self, name, points, closed=False):
        self.add_polyline(name, *points, closed=closed)

    def arc(self, name, a, b, r, ry=None, sweep=True):
        self.add_arc(name, a, b, radius_x=r, radius_y=r if ry is None else ry, sweep=sweep)

    def rect(self, name, x, y, w, h, r=4):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f'{name}-{i}'; ids.append(part)
            if i%2: self.arc(part,a,b,r)
            elif a != b: self.add_line(part,a,b)
            else: ids.pop()
        self.add_contour(name,*ids,closed=True)
