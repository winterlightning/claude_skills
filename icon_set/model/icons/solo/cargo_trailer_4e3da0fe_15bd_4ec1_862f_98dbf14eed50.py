'Simple Cargo Trailer.\nPlan and review: Retained blank cargo trailer, rounded roof and two equal wheels. Opened underside at wheel joins. No hitch or cab invented.\nKeyshape: HRECT_L, exact SOLO48 envelope.\nConstruction reference: Lucide truck: equal wheels and blank cargo body; no cab/hitch invented.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4e3da0fe-15bd-4ec1-862f-98dbf14eed50'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/transporter 7_4e3da0fe-15bd-4ec1-862f-98dbf14eed50.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cargo-trailer'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('cargo', 'trailer')

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

        path('body',(8,36),[(4,30),(4,18),((14,8),10,10,True),(34,8),((44,18),10,10,True),(44,30),(40,36)])
        self.add_line('underside',(16,36),(32,36))
        for j,x in enumerate((12,36)):
         circle(f'wheel-{j}',x,36,4)
         for s in ('body','underside'):self.relate('connect',s,f'wheel-{j}')
