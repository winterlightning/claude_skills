from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f8387852-af8b-4221-a8f7-998fc1b24294'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/band saw_f8387852-af8b-4221-a8f7-998fc1b24294.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'industrial-band-saw-machine'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('industrial', 'band', 'saw', 'machine')

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
        # Plan: SQUARE extremes 6,6 to 42,42; upright nested frame, base and lower-right gear remain in original relative arrangement.
        self.add_line('outer-left',(10,34),(10,12))
        self.add_arc('upper-left',(10,12),(16,6),radius_x=6)
        self.add_line('top',(16,6),(32,6))
        self.add_arc('upper-right',(32,6),(38,12),radius_x=6)
        self.add_line('outer-right',(38,12),(38,19))
        self.add_contour('frame','outer-left','upper-left','top','upper-right','outer-right')
        self.add_polyline('inner-frame',(18,34),(18,15),(30,15),(30,18))
        self.add_line('ledge',(18,25),(21,25))
        self.box('base',6,34,36,8)
        self.relate('connect','frame','base')
        self.relate('connect','inner-frame','base')
        self.relate('connect','inner-frame','ledge')
        cx,cy=30,25
        quarter=[(-3,-9),(3,-9),(3,-6),(6,-6),(6,-3),(9,-3)]
        points=[]
        for turn in range(4):
            for x,y in quarter:
                for _ in range(turn): x,y=-y,x
                points.append((cx+x,cy+y))
        self.add_polyline('gear',*points,closed=True)
        self.circle('hub',cx,cy,3)
