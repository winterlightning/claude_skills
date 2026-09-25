'Curved Path Coverage Area.\nPlan and review: Retained outer curved area and shorter inner dividing arc on a shared baseline.\nKeyshape: HRECT_M, exact SOLO48 envelope selected for this subject.\nConstruction reference: No useful Lucide subject match; source render guides construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '12741330-14d5-47aa-8ea1-b1e93c08134f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/swath_12741330-14d5-47aa-8ea1-b1e93c08134f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-path-coverage-area'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('curved', 'path', 'coverage', 'area')

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

        path('outer',(4,38),[((44,10),40,28,True),(44,38),(4,38)],True)
        self.add_arc('inner',(20,38),(44,26),radius_x=24,radius_y=12,sweep=True)
        self.relate('connect','outer','inner')
