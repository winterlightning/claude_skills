'Rolling Travel Suitcase.\nPlan and review: Retained rolling case, raised telescoping handle, front seam and two wheel marks.\nKeyshape: VRECT_L, exact SOLO48 envelope.\nConstruction reference: Lucide luggage: broad case, extending handle and two wheels.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0756a7ad-4a3f-4bc2-aeb6-bf531ca4d3a3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/suitcase rolling_0756a7ad-4a3f-4bc2-aeb6-bf531ca4d3a3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rolling-suitcase'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('rolling', 'suitcase')

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

        box('case',8,16,40,40,4)
        path('handle',(18,16),[(18,4),(30,4),(30,16)]);self.relate('connect','handle','case')
        self.add_line('pocket',(18,25),(30,25))
        for j,x in enumerate((14,34)):self.add_line(f'wheel-{j}',(x,40),(x,44));self.relate('connect',f'wheel-{j}','case')
