'Simple Tree on Ground.\nPlan and review: Retained lobed canopy, trunk, two branches and ground baseline. Widened open canopy base and shortened branches for clearance.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Lucide sprout: central stem with true branch junction; source lobed canopy retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '535c2c0b-3059-4b5e-9695-580837811633'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/alder_535c2c0b-3059-4b5e-9695-580837811633.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tree-lobed-canopy-baseline'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('tree', 'lobed', 'canopy', 'baseline')

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

        curve('canopy',(15,30),((10,30),(6,28),(6,22)),((6,16),(10,14),(14,14)),((14,8),(18,6),(24,6)),((30,6),(34,8),(34,14)),((38,14),(42,16),(42,22)),((42,28),(38,30),(33,30)))
        self.add_polyline('trunk',(24,18),(24,24),(24,42));self.add_line('ground',(6,42),(42,42));self.relate('connect','trunk','ground')
        path('branches',(20,20),[(24,24),(28,20)]);self.relate('connect','trunk','branches')
