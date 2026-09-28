"""Baggage Weight Scale.

Plan: Suitcase on a platform beside a dial scale; retain handle and dial, omit tag and suitcase bands.
Construction reference: No useful exact Lucide match; geometric arc construction.
Keyshape SQUARE: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac7ab444-ea22-41ad-ac0e-d5661e17d156'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/baggage weight 1_ac7ab444-ea22-41ad-ac0e-d5661e17d156.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'tagged-suitcase-on-a-dial-scale'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('baggage', 'weight', 'scale')

    def build(self):

        self.rect('case',6,22,20,12,3)
        self.path('handle',[(10,22),(10,14),(22,14),(22,22)])
        self.relate('connect','case','handle')
        self.circle('dial',36,12,6)
        self.add_line('post',(36,18),(36,42));self.relate('connect','dial','post')
        self.add_line('platform',(6,42),(42,42));self.relate('connect','post','platform')

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
