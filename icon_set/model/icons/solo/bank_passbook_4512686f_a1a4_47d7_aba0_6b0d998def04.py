from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4512686f-a1a4-47d7-aba0-6b0d998def04'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/bankbook_4512686f-a1a4-47d7-aba0-6b0d998def04.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bank-passbook'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('bank', 'passbook')

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
        # Plan: SQUARE extremes 6,6 to 42,42; rounded cover owns two full-width upper rules and a centered lower label.
        self.add_line('top',(10,6),(38,6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.add_arc('br',(42,38),(38,42),radius_x=4)
        self.add_line('bottom',(38,42),(10,42))
        self.add_arc('bl',(10,42),(6,38),radius_x=4)
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        ys=[10,14,22,38]
        for i in range(3):
            self.add_line(f'right-{i}',(42,ys[i]),(42,ys[i+1]))
            self.add_line(f'left-{i}',(6,ys[i+1]),(6,ys[i]))
        self.add_contour('cover','top','tr','right-0','right-1','right-2','br','bottom','bl','left-2','left-1','left-0','tl',closed=True)
        for i,y in enumerate((14,22)):
            self.add_line(f'band-{i}',(6,y),(42,y))
            self.relate('connect','cover',f'band-{i}')
        self.add_line('label',(16,31),(32,31))
