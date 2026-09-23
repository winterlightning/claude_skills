from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8a6f5388-93e2-4e87-bb21-8db3666f5c20'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/auto pilot car radius_8a6f5388-93e2-4e87-bb21-8db3666f5c20.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'autonomous-car-sensor-signal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('autonomous', 'car', 'sensor', 'signal')

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
        # Plan: SQUARE extremes 6,6 to 42,42; four mirrored pairs of concentric corner arcs enclose side-view car with equal wheels.
        for ix in (0,1):
            for iy in (0,1):
                def p(x,y): return (48-x if ix else x,48-y if iy else y)
                for label,r in [('outer',12),('inner',4)]:
                    self.add_arc(f'sensor-{ix}-{iy}-{label}',p(18-r,18),p(18,18-r),radius_x=r,sweep=(ix==iy))
        self.add_polyline('body',(15,29),(13,29),(13,25),(17,23),(20,18),(28,18),(31,23),(35,25),(35,29),(33,29))
        for x in (18,30): self.circle(f'wheel-{x}',x,29,3)
        self.add_line('chassis',(21,29),(27,29))
        for wheel in ('wheel-18','wheel-30'):
            self.relate('connect','body',wheel)
            self.relate('connect','chassis',wheel)
