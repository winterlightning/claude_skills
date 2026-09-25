'Side View Utility Pickup Truck.\nPlan and review: Retained right-facing raised cab, low body and two equal wheels. Opened underside and angled lower corners into wheel joins to avoid crossing wheel interiors.\nKeyshape: HRECT_L, exact SOLO48 envelope.\nConstruction reference: Lucide truck: shared cab/deck structure and repeated round wheels.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd02de897-e58a-41e5-bf4c-96ad0e8cd1f5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pickup truck_d02de897-e58a-41e5-bf4c-96ad0e8cd1f5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'side-view-utility-pickup-truck'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('side', 'view', 'utility', 'pickup', 'truck')

    def build(self):

        def path(name, start, steps, closed=False):
            members=[]; point=start
            for index, step in enumerate(steps):
                member=f"{name}-{index}"
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep); point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def curve(name,start,*segments):
            self.add_bezier(name,start,*segments)

        path('body',(8,36),[(4,30),(4,22),(44,22),(44,30),(40,36)])
        self.add_line('underside',(16,36),(32,36))
        path('cab',(22,22),[(22,8),(32,8),(42,22)]);self.relate('connect','cab','body')
        for j,x in enumerate((12,36)):
         circle(f'wheel-{j}',x,36,4)
         for s in ('body','underside'):self.relate('connect',s,f'wheel-{j}')
