'Round Handle Teapot.\nPlan and review: Retained overhead arched handle, domed lid, left spout and broad pot body. Widened spout and omitted small lid knob.\nKeyshape: HRECT_L, exact SOLO48 envelope.\nConstruction reference: Source render; no useful exact local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ae266a8-760d-4964-b040-37cfadf281d9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/tea pot 2_5ae266a8-760d-4964-b040-37cfadf281d9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'overhead-handle-teapot'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ()
    keywords = ('overhead', 'handle', 'teapot')

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

        path('handle',(16,24),[((40,24),12,16,True)])
        curve('lid',(16,24),((22,18),(36,18),(40,24)))
        path('pot',(16,24),[(14,26),(4,16),(4,28),(10,36),((16,40),6,4,False),(38,40),((44,34),6,6,False),(40,24)])
        for a,b in [('handle','lid'),('pot','lid'),('pot','handle')]:self.relate('connect',a,b)
