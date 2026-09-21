"""Baby Face with Curl.

Plan: Blank round baby head and integrated curl; omit ear micro-lobes to protect round silhouette.
Construction reference: Lucide baby: integrated forehead curl and round open face outline.
Keyshape HRECT_L: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ec01feb-4215-413d-9fe1-82f8e7660a71'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/baby boy_4ec01feb-4215-413d-9fe1-82f8e7660a71.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'round-baby-head-with-one-curl'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/misc'
    aliases = ()
    keywords = ('baby', 'face', 'with', 'curl')

    def build(self):

        self.arc('face',(40,24),(8,24),16,sweep=True)
        self.arc('forehead',(8,24),(24,8),16)
        self.arc('curl',(24,8),(24,20),6)
        self.add_contour('head','face','forehead','curl')
        self.add_line('ear-left',(4,24),(8,24)); self.relate('connect','head','ear-left')
        self.add_line('ear-right',(40,24),(44,24)); self.relate('connect','head','ear-right')

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
