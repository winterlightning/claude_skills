"""A domed autonomous car with radio signals.
Plan: SQUARE allocates upper space to signals and lower space to car and wheels.
Reduction: Reduced two wave pairs to one; beacon reduced to stem; divided circular window reduced to a windshield bar.
Construction: Supplied reference owns dome and beacon; Lucide car-front supports sparse vehicle detail and paired wheels.
Layout: Mirrored dome, wheels, and radio strokes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '148a6d3d-6e93-44b0-ad9c-3c3c30856f29'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/auto pilot car signal 1_148a6d3d-6e93-44b0-ad9c-3c3c30856f29.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'autonomous-domed-car-with-signal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('autonomous', 'domed', 'car', 'with', 'signal')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def box(self, name, x, y, w, h, r=0):
        if not r:
            self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            return
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            part=f'{name}-{i}'; ids.append(part)
            if i%2: self.add_arc(part,pts[i],pts[(i+1)%8],radius_x=r)
            else: self.add_line(part,pts[i],pts[(i+1)%8])
        self.add_contour(name,*ids,closed=True)

    def build(self):
        # SQUARE extremes (6,6)-(42,42). Dome joins wheel tops, repeated
        # radio strokes flank the beacon. Omit doubled wave and window divider.
        self.add_arc('dome-left',(9,36),(24,19),radius_x=15,radius_y=17)
        self.add_arc('dome-right',(24,19),(39,36),radius_x=15,radius_y=17)
        self.add_contour('dome','dome-left','dome-right')
        for x in (9,39):
            pts=[(x,36),(x+3,39),(x,42),(x-3,39),(x,36)]
            for j in range(4):self.add_arc(f'wheel-{x}-{j}',pts[j],pts[j+1],radius_x=3)
            self.add_contour(f'wheel-{x}',*(f'wheel-{x}-{j}' for j in range(4)),closed=True)
            self.relate('connect','dome',f'wheel-{x}')
        self.add_line('window',(20,29),(28,29))
        self.add_line('base',(12,39),(36,39))
        for x in (9,39):self.relate('connect','base',f'wheel-{x}')
        self.add_line('beacon',(24,10),(24,19))
        self.relate('connect','beacon','dome')
        self.add_arc('radio-left',(14,6),(14,12),radius_x=3,sweep=False)
        self.add_arc('radio-right',(34,6),(34,12),radius_x=3,sweep=True)
