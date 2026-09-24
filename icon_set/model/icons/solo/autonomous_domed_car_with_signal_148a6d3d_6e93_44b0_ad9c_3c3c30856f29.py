from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '148a6d3d-6e93-44b0-ad9c-3c3c30856f29'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/auto pilot car signal 1_148a6d3d-6e93-44b0-ad9c-3c3c30856f29.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'autonomous-domed-car-with-signal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
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
        # Plan: SQUARE extremes 6,6 to 42,42; dome, two wheels, divided round window, roof beacon and paired radio arcs.
        self.add_arc('dome',(6,38),(42,38),radius_x=18,radius_y=16)
        self.add_line('left-base',(6,38),(9,38))
        self.add_line('center-base',(15,38),(33,38))
        self.add_line('right-base',(39,38),(42,38))
        for side,x in [('left',12),('right',36)]:
            self.circle(side+'-wheel',x,39,3)
        self.circle('window',24,31,6)
        self.add_line('window-divider',(18,31),(30,31))
        self.relate('connect','window','window-divider')
        self.add_arc('beacon-top',(21,20),(27,20),radius_x=3)
        self.add_polyline('beacon-stem',(21,22),(21,20))
        self.add_line('beacon-right',(27,20),(27,22))
        self.relate('connect','beacon-top','beacon-stem')
        self.relate('connect','beacon-top','beacon-right')
        for side in (0,1):
            def p(x,y): return (48-x if side else x,y)
            self.add_arc(f'outer-{side}',p(15,6),p(15,18),radius_x=6,sweep=bool(side))
            self.add_arc(f'inner-{side}',p(20,8),p(20,16),radius_x=4,sweep=bool(side))
