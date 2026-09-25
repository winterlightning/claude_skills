"""Fresh reference repair. Construction reference: Lucide bike (wheel construction only).
Keyshape HRECT_L; source identity is preserved separately from its icon name.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ba2c7c5d-7b19-4251-8651-f1619fdbdc5e'
SOURCE_PATH = 'pictographic-primitives/other/bike_ba2c7c5d-7b19-4251-8651-f1619fdbdc5e.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'simple-bicycle'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('bike',)

    def path(self,n,start,*steps,closed=False):
        here=start; ids=[]
        for i,step in enumerate(steps):
            kind,end,*v=step; name=f'{n}-{i}';ids.append(name)
            if kind=='L':self.add_line(name,here,end)
            elif kind=='A':self.add_arc(name,here,end,radius_x=v[0],radius_y=v[1],sweep=v[2])
            elif kind=='C':self.add_bezier(name,here,(v[0],v[1],end))
            here=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True),closed=True)

    def build(self):

        # The reference is an open simple frame, not a diamond: preserve the single sloping crossbar.
        for n,x in [('rear',12),('front',36)]:self.circle(n,x,32,8)
        self.add_polyline('rear-fork',(12,32),(12,24),(18,8))
        self.add_polyline('seat',(10,8),(14,8),(18,8))
        self.add_polyline('front-fork',(36,32),(36,24),(32,16),(30,8),(26,8))
        self.add_line('crossbar',(12,24),(32,16))
        for a,b in [('rear','rear-fork'),('front','front-fork'),('rear-fork','seat'),('rear-fork','crossbar'),('front-fork','crossbar')]:self.relate('connect',a,b)

    icon_id = 'bicycle-reference-25-solo'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sub icon', 'simple bicycle')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
