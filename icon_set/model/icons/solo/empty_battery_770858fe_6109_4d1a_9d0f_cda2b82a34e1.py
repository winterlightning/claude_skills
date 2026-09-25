from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '770858fe-6109-4d1a-9d0f-cda2b82a34e1'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/battery low_770858fe-6109-4d1a-9d0f-cda2b82a34e1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'empty-battery'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('empty', 'battery')

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
        # Plan: HRECT_M extremes 4,10 to 44,38; empty rounded battery body and attached right terminal with exact shared endpoints.
        self.add_line('top',(8,10),(32,10))
        self.add_arc('tr',(32,10),(36,14),radius_x=4)
        ys=[14,18,30,34]
        for i in range(3): self.add_line(f'right-{i}',(36,ys[i]),(36,ys[i+1]))
        self.add_arc('br',(36,34),(32,38),radius_x=4)
        self.add_line('bottom',(32,38),(8,38))
        self.add_arc('bl',(8,38),(4,34),radius_x=4)
        self.add_line('left',(4,34),(4,14))
        self.add_arc('tl',(4,14),(8,10),radius_x=4)
        self.add_contour('body','top','tr','right-0','right-1','right-2','br','bottom','bl','left','tl',closed=True)
        self.add_line('terminal-top',(36,18),(41,18))
        self.add_arc('terminal-tr',(41,18),(44,21),radius_x=3)
        self.add_line('terminal-right',(44,21),(44,27))
        self.add_arc('terminal-br',(44,27),(41,30),radius_x=3)
        self.add_line('terminal-bottom',(41,30),(36,30))
        self.add_contour('terminal','terminal-top','terminal-tr','terminal-right','terminal-br','terminal-bottom')
        self.relate('connect','body','terminal')
