"""Bed with Pillow.

Plan: Single bed with tall rounded headboard and raised pillow.
Construction reference: Lucide bed: long rails, upright posts and rounded pillow.
Keyshape HRECT_L: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b900fc3a-b5fd-44b4-bfd4-79d61a306e3f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/bedroom_b900fc3a-b5fd-44b4-bfd4-79d61a306e3f.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'single-bed-with-tall-rounded-headboard'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bed', 'with', 'pillow')

    def build(self):
        self.add_line('headboard',(4,8),(4,40))
        self.path('frame',[(4,30),(44,30),(44,40)])
        self.relate('connect','headboard','frame')
        self.arc('pillow',(14,30),(34,30),10)
        self.relate('connect','frame','pillow')
        self.add_line('rail',(4,38),(44,38))
        self.relate('connect','headboard','rail');self.relate('connect','frame','rail')

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
