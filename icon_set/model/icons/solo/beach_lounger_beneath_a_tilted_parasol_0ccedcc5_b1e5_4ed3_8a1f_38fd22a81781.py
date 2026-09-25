"""Beach Umbrella and Sunbed.

Plan: Lounger under parasol, a physical beach scene; simplify canopy to a semicircle.
Construction reference: Lucide umbrella: semicircular canopy; physical lounger and parasol remain one scene.
Keyshape SQUARE: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0ccedcc5-b1e5-4ed3-8a1f-38fd22a81781'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/beach palm sunbed_0ccedcc5-b1e5-4ed3-8a1f-38fd22a81781.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'beach-lounger-beneath-a-tilted-parasol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('beach', 'umbrella', 'and', 'sunbed')

    def build(self):

        self.arc('canopy',(6,22),(38,22),16)
        self.add_line('canopy-base',(38,22),(6,22));self.add_contour('parasol','canopy','canopy-base',closed=True)
        self.add_line('pole',(22,22),(22,34));self.relate('connect','parasol','pole')
        self.path('seat',[(6,34),(34,34),(42,26)])
        self.relate('connect','seat','pole')
        for i,x in enumerate((12,32)):
            self.add_line(f'leg-{i}',(x,34),(x-4,42));self.relate('connect','seat',f'leg-{i}')

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
