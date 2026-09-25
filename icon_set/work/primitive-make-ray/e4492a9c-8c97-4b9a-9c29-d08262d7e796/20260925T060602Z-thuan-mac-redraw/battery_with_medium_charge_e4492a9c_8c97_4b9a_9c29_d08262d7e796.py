"""Battery outline integrates a rounded terminal; interior rectangular charge block is centered vertically."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e4492a9c-8c97-4b9a-9c29-d08262d7e796'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__battery-with-medium-charge/20260925T060602Z-thuan-mac/reference/charging battery almost full_e4492a9c-8c97-4b9a-9c29-d08262d7e796.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'battery-with-medium-charge'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('charging battery almost full',)

    def build(self):
        # Symbol plan: Battery outline integrates a rounded terminal; interior rectangular charge block is centered vertically.
        # Construction reference: Lucide battery; original supplied subject controls meaning.

        def path(name, start, commands, closed=False):
            ids=[]; here=start
            for i,c in enumerate(commands):
                kind,end,*args=c
                if kind == 'L' and here==end: continue
                eid=f'{name}-{i}'
                if kind=='L': self.add_line(eid,here,end)
                elif kind=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(eid,here,(args[0],args[1],end))
                ids.append(eid);here=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path('outline',(8,10),[('L',(32,10)),('A',(36,14),4,4,True),('L',(36,18)),('L',(41,18)),('A',(44,21),3,3,True),('L',(44,27)),('A',(41,30),3,3,True),('L',(36,30)),('L',(36,34)),('A',(32,38),4,4,True),('L',(8,38)),('A',(4,34),4,4,True),('L',(4,14)),('A',(8,10),4,4,True)],True)
        poly('charge',(13,19),(24,19),(24,29),(13,29),closed=True)
