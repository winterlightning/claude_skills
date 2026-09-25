'Simple Small Table.\nPlan and review: Retained rounded thick tabletop and two equal inset legs.\nKeyshape: HRECT_M, exact SOLO48 envelope.\nConstruction reference: No useful exact Lucide match; source silhouette and geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9bf30c6d-ce72-47b6-937b-660de64e1258'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/tabletop_9bf30c6d-ce72-47b6-937b-660de64e1258.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-leg-small-table'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('two', 'leg', 'small', 'table')

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

        box('top',4,10,44,18,4)
        for j,x in enumerate((12,36)):self.add_line(f'leg-{j}',(x,18),(x,38));self.relate('connect',f'leg-{j}','top')
