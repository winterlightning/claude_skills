from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f2e0c651-d48a-403a-b9be-ca4d6dfd34d6'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_07/bnter logo_f2e0c651-d48a-403a-b9be-ca4d6dfd34d6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-message-speech-bubble'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('rounded', 'message', 'speech', 'bubble')

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
        # Plan: HRECT_L extremes4,8 to44,40; rounded wide body and integrated lower-left speech tail.
        self.add_line('top',(8,8),(40,8))
        self.add_arc('tr',(40,8),(44,12),radius_x=4)
        self.add_line('right',(44,12),(44,28))
        self.add_arc('br',(44,28),(40,32),radius_x=4)
        points=[(40,32),(20,32),(10,40),(10,32),(8,32)]
        for i in range(4): self.add_line(f'lower-{i}',points[i],points[i+1])
        self.add_arc('bl',(8,32),(4,28),radius_x=4)
        self.add_line('left',(4,28),(4,12))
        self.add_arc('tl',(4,12),(8,8),radius_x=4)
        self.add_contour('outline','top','tr','right','br',*[f'lower-{i}' for i in range(4)],'bl','left','tl',closed=True)
