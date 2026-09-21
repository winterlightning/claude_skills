"""Bakery Muffin Dessert.

Plan: Muffin: three broad domed lobes over a tapered cup; remove tiny scallops.
Construction reference: Lucide soup: coherent bowl outline; source supplies the three-lobed muffin silhouette.
Keyshape SQUARE: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a750edfa-3ec5-4f76-a638-5243c8eeba15'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_27/muffin_a750edfa-3ec5-4f76-a638-5243c8eeba15.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'muffin-with-three-lobed-domed-top'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/misc'
    aliases = ()
    keywords = ('bakery', 'muffin', 'dessert')

    def build(self):

        self.arc('left',(6,22),(14,14),8)
        self.arc('dome',(14,14),(34,14),10,8)
        self.arc('right',(34,14),(42,22),8)
        self.arc('right-bottom',(42,22),(34,30),8)
        self.add_line('base',(34,30),(14,30))
        self.arc('left-bottom',(14,30),(6,22),8)
        self.add_contour('top','left','dome','right','right-bottom','base','left-bottom',closed=True)
        self.path('cup',[(14,30),(18,42),(30,42),(34,30)])
        self.relate('connect','top','cup')

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
