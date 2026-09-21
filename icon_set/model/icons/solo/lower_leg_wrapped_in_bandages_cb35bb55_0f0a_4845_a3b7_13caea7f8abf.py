"""Bandaged Leg and Foot.

Plan: Lower leg in a cast with broad ankle and left-facing toes; two wrap lines define bandages.
Construction reference: No useful exact Lucide match; geometric arc construction.
Keyshape VRECT_L: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cb35bb55-0f0a-4845-a3b7-13caea7f8abf'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/bandage leg_cb35bb55-0f0a-4845-a3b7-13caea7f8abf.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'lower-leg-wrapped-in-bandages'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/misc'
    aliases = ()
    keywords = ('bandaged', 'leg', 'and', 'foot')

    def build(self):

        self.path('leg',[(24,4),(40,4),(40,36)])
        self.arc('heel',(40,36),(32,44),8)
        self.add_line('sole',(32,44),(16,44))
        self.arc('toe',(16,44),(16,28),8)
        self.path('ankle',[(16,28),(24,28),(24,4)])
        # Merge the temporary runs into one continuous contour.
        self.contours = [c for c in self.contours if not set(c.members).issubset({'ankle-2', 'leg-2', 'ankle-1', 'leg-1', 'heel', 'sole', 'toe'})]
        self.add_contour('outline','leg-1','leg-2','heel','sole','toe','ankle-1','ankle-2',closed=True)
        self.add_line('wrap',(24,12),(40,20));self.relate('connect','outline','wrap')
        self.add_line('foot-wrap',(24,24),(40,32));self.relate('connect','outline','foot-wrap')

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
