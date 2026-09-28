'Simple Turtle Profile.\nPlan and review: Retained domed turtle shell, raised right head/neck, two feet and tiny left tail. Widened feet to preserve their openings.\nKeyshape: HRECT_L, exact SOLO48 envelope.\nConstruction reference: Lucide turtle: domed shell, right head and repeated feet; omit internal shell facets absent from source.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d3b1045-b9ab-4cb4-8258-5e06699c9040'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/terrapin_4d3b1045-b9ab-4cb4-8258-5e06699c9040.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'right-facing-terrapin'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('right', 'facing', 'terrapin')

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

        path('shell',(6,28),[((34,28),14,20,True),(6,28)],True)
        path('neck',(34,28),[(36,18),((44,18),4,4,True),((34,28),10,10,True)]);self.relate('connect','neck','shell')
        for j,x in enumerate((12,28)):
         path(f'foot-{j}',(x-4,28),[(x-4,36),((x+4,36),4,4,False),(x+4,28)]);self.relate('connect',f'foot-{j}','shell')
        self.add_line('tail',(4,28),(6,28));self.relate('connect','tail','shell')
