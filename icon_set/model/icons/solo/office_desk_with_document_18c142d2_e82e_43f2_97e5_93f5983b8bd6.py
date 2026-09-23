from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18c142d2-e82e-43f2-97e5-93f5983b8bd6'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_07/boss desk document_18c142d2-e82e-43f2-97e5-93f5983b8bd6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'office-desk-with-document'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('office', 'desk', 'with', 'document')

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
        # Plan: SQUARE extremes6,6 to42,42; desk slab, two legs and crossbar beneath a centered document.
        self.add_polyline('desktop',(6,22),(14,22),(34,22),(42,22),(42,30),(38,30),(10,30),(6,30),closed=True)
        self.add_polyline('document',(14,22),(14,6),(34,6),(34,22))
        self.relate('connect','desktop','document')
        self.add_line('text',(22,14),(26,14))
        for side,x in [('left',10),('right',38)]:
            self.add_polyline(side+'-leg',(x,30),(x,38),(x,42))
            self.relate('connect','desktop',side+'-leg')
        self.add_line('crossbar',(10,38),(38,38))
        for side in ('left','right'): self.relate('connect','crossbar',side+'-leg')
