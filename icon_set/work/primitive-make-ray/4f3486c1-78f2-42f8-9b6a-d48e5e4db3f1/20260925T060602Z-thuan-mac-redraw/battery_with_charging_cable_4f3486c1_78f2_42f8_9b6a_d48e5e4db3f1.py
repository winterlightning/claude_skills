"""Wide battery with rounded terminal and centered downward charging lead."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4f3486c1-78f2-42f8-9b6a-d48e5e4db3f1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__battery-with-charging-cable/20260925T060602Z-thuan-mac/reference/battery charge_4f3486c1-78f2-42f8-9b6a-d48e5e4db3f1.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'battery-with-charging-cable'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('battery charge',)

    def build(self):
        # Symbol plan: Wide battery with rounded terminal and centered downward charging lead.
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
        path('body',(8,8),[('L',(32,8)),('A',(36,12),4,4,True),('L',(36,16)),('L',(36,28)),('A',(32,32),4,4,True),('L',(20,32)),('L',(8,32)),('A',(4,28),4,4,True),('L',(4,12)),('A',(8,8),4,4,True)],True)
        path('terminal',(36,16),[('L',(41,16)),('A',(44,19),3,3,True),('L',(44,25)),('A',(41,28),3,3,True),('L',(36,28))]);join('terminal','body')
        line('cable',(20,32),(20,40));join('cable','body')
