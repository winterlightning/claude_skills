'A dashboard has a broad curved instrument panel beneath a rounded windshield. Two circular gauges flank the center, while a three-spoke steering wheel overlaps the lower foreground.\nPlan: Rounded dashboard frame with two gauges and foreground steering wheel.\nConstruction reference: No useful direct Lucide match; rebuilt from inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1d59a930-4893-4b9f-8208-3db738cc0478'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/cockpit_1d59a930-4893-4b9f-8208-3db738cc0478.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dashboard-with-foreground-steering-wheel'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('dashboard', 'with', 'foreground', 'steering', 'wheel')

    # Repair: Rebalance smaller wheel and inboard gauges; preserve both gauges and all3 steering spokes.
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L':self.add_line(member,here,end)
                elif kind=='A':self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(member,here,(args[0],args[1],end))
                here=end;members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*points):self.add_polyline(name,*points,closed=points[0]==points[-1])
        def join(a,b):self.relate('connect',a,b)

        path('dash',(16,34),[('L',(10,34)),('A',(6,30),4,4,True),('L',(6,10)),('A',(10,6),4,4,True),('L',(38,6)),('A',(42,10),4,4,True),('L',(42,30)),('A',(38,34),4,4,True),('L',(32,34))])
        circle('wheel',24,34,8);join('wheel','dash')
        poly('spokes',(16,34),(24,34),(32,34));line('spoke-bottom',(24,34),(24,42));join('wheel','spokes');join('wheel','spoke-bottom');join('spokes','spoke-bottom')
        circle('gauge-left',17,17,2);circle('gauge-right',31,17,2)
