"""Beach Umbrella Under Sunny Sky.

Plan: Beach parasol beside a low sun; retain shoreline, simplify canopy ribs.
Construction reference: Lucide umbrella: clean canopy construction; source supplies the sun and shoreline.
Keyshape HRECT_L: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '08b0693a-916b-46bb-84c3-e776a7ee8dfc'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/beach_08b0693a-916b-46bb-84c3-e776a7ee8dfc.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'beach-parasol-beside-a-low-sun'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/misc'
    aliases = ()
    keywords = ('beach', 'umbrella', 'under', 'sunny', 'sky')

    def build(self):

        self.circle('sun',10,14,6)
        self.arc('canopy',(24,24),(44,24),10)
        self.add_line('base',(44,24),(24,24));self.add_contour('parasol','canopy','base',closed=True)
        self.add_line('pole',(34,24),(30,40));self.relate('connect','parasol','pole')
        self.add_line('shore',(4,40),(44,40));self.relate('connect','shore','pole')

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
