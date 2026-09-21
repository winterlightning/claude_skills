"""Baseball Batting Helmet.

Plan: Batting helmet in profile with broad ear guard and a circular ear opening.
Construction reference: No useful exact Lucide match; geometric arc construction.
Keyshape HRECT_L: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e93a4ec7-1826-4d16-b85f-10f4fce227d7'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/baseball helmet_e93a4ec7-1826-4d16-b85f-10f4fce227d7.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'batting-helmet-with-ear-guard'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/misc'
    aliases = ()
    keywords = ('baseball', 'batting', 'helmet')

    def build(self):

        self.arc('dome',(4,24),(36,24),16)
        self.add_line('ledge',(36,24),(28,24))
        self.add_line('brim',(36,24),(44,24))
        self.arc('face-cut',(28,24),(28,32),4,sweep=False)
        self.arc('guard',(28,32),(12,32),8)
        self.arc('back',(12,32),(4,24),8)
        # Merge the temporary runs into one continuous contour.
        self.contours = [c for c in self.contours if not set(c.members).issubset({'face-cut', 'back', 'brim-1', 'dome', 'guard', 'brim-2'})]
        self.add_contour('helmet','dome','ledge','face-cut','guard','back',closed=True)
        self.relate('connect','helmet','brim')
        # Omit the ear opening; its pocket cannot retain legal clearance.

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
