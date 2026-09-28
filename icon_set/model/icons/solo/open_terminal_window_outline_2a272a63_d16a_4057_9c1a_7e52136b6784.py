from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a272a63-d16a-4057-9c1a-7e52136b6784'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_08/brute force authentication password attack bash_2a272a63-d16a-4057-9c1a-7e52136b6784.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-terminal-window-outline'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('open', 'terminal', 'window', 'outline')

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
        # Plan: HRECT_M extremes4,10 to44,38; one rounded partial window contour with broad lower-right opening.
        self.add_line('bottom',(22,38),(10,38))
        self.add_arc('bl',(10,38),(4,32),radius_x=6)
        self.add_line('left',(4,32),(4,16))
        self.add_arc('tl',(4,16),(10,10),radius_x=6)
        self.add_line('top',(10,10),(38,10))
        self.add_arc('tr',(38,10),(44,16),radius_x=6)
        self.add_line('right-end',(44,16),(44,22))
        self.add_contour('outline','bottom','bl','left','tl','top','tr','right-end')
