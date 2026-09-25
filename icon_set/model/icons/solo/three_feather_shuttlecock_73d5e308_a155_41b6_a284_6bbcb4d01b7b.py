"""Badminton Shuttlecock.

Plan: Diagonal shuttlecock with a rounded cork and three feather rays; fan shares the cork junction.
Construction reference: No useful exact Lucide match; geometric arc construction.
Keyshape SQUARE: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '73d5e308-a155-41b6-a284-6bbcb4d01b7b'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/badminton_73d5e308-a155-41b6-a284-6bbcb4d01b7b.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'three-feather-shuttlecock'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('badminton', 'shuttlecock')

    def build(self):
        # Upright fan preserves three broad feathers with an attached cork cap.
        self.path('fan',[(6,6),(42,6),(30,36),(18,36)],True)
        for i,x in enumerate((18,30)):
            end_x=20 if i==0 else 28
            self.add_line(f'feather-{i}',(x,6),(end_x,18))
            self.relate('connect','fan',f'feather-{i}')
        self.arc('cork',(18,36),(30,36),6,sweep=False)
        self.relate('connect','fan','cork')

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
