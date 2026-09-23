from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b317a6a6-fb5f-4063-b4ca-9345a6cec436'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_08/browser page text 2_b317a6a6-fb5f-4063-b4ca-9345a6cec436.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'web-browser-page-layout'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('web', 'browser', 'page', 'layout')

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
        # Plan: SQUARE extremes6,6 to42,42; browser frame owns header with3 controls, left navigation rail and2 stacked content cards.
        self.add_line('top',(10,6),(38,6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.add_line('right-upper',(42,10),(42,14))
        self.add_line('right-lower',(42,14),(42,38))
        self.add_arc('br',(42,38),(38,42),radius_x=4)
        self.add_line('bottom-right',(38,42),(18,42))
        self.add_line('bottom-left',(18,42),(10,42))
        self.add_arc('bl',(10,42),(6,38),radius_x=4)
        self.add_line('left-lower',(6,38),(6,14))
        self.add_line('left-upper',(6,14),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('window','top','tr','right-upper','right-lower','br','bottom-right','bottom-left','bl','left-lower','left-upper','tl',closed=True)
        self.add_polyline('header',(6,14),(18,14),(42,14))
        self.add_line('sidebar',(18,14),(18,42))
        self.relate('connect','header','sidebar')
        self.relate('connect','window','header')
        self.relate('connect','window','sidebar')
        for i,x in enumerate((12,20,28)): self.add_dot(f'control-{i}',(x,10))
        for i,y in enumerate((22,30,38)): self.add_line(f'nav-{i}',(10,y),(12,y))
        for i,y in enumerate((22,34)): self.box(f'content-{i}',26,y,8,6)
