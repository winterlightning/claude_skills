'Finished Hourglass Timer Symbol.\nPlan and review: Retained curved hourglass waist and one short line in the upper chamber. Narrowed the interior line for clearance.\nKeyshape: VRECT_M, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Lucide hourglass: paired waist curves between level ends.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '63036b8e-19cf-4f8d-abbd-61834b8f8ed5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/hourglass end_63036b8e-19cf-4f8d-abbd-61834b8f8ed5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hourglass-with-short-interior-line'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('hourglass', 'with', 'short', 'interior', 'line')

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

        curve('left',(10,4),((10,18),(20,18),(20,24)),((20,30),(10,30),(10,44)))
        curve('right',(38,4),((38,18),(28,18),(28,24)),((28,30),(38,30),(38,44)))
        self.add_line('top',(10,4),(38,4));self.add_line('bottom',(10,44),(38,44))
        for a in ('left','right'):
         for b in ('top','bottom'):self.relate('connect',a,b)
        self.add_line('sand',(22,12),(26,12))
