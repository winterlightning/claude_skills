'Condiment Squeeze Bottle.\nPlan and review: Retained nozzle, neck collar line and broad tapered bottle body. Simplified collar thickness.\nKeyshape: VRECT_M, exact SOLO48 envelope selected for this subject.\nConstruction reference: No useful Lucide subject match; source render guides construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7269ba1-5723-4ac4-9255-c0b3b1134ec9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/ketchup_b7269ba1-5723-4ac4-9255-c0b3b1134ec9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'condiment-squeeze-bottle'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('condiment', 'squeeze', 'bottle')

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

        path('bottle',(20,4),[(28,4),(28,14),(38,32),(38,40),((34,44),4,4,True),(14,44),((10,40),4,4,True),(10,32),(20,14),(20,4)],True)
        self.add_line('collar',(20,14),(28,14));self.relate('connect','bottle','collar')
