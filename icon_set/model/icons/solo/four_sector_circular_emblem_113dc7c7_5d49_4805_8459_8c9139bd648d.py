'Radiation Warning Symbol.\nPlan and review: The visible source is a four-sector circular emblem, not a radiation trefoil. Preserved both circles and all four spokes; no invented radiation meaning.\nKeyshape: CIRCLE, exact SOLO48 envelope.\nConstruction reference: Lucide life-buoy: concentric circles with radial connectors; preserve four sectors visible in source.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '113dc7c7-5d49-4805-8459-8c9139bd648d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/air nuclear hazard_113dc7c7-5d49-4805-8459-8c9139bd648d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'four-sector-circular-emblem'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('four', 'sector', 'circular', 'emblem')

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

        circle('outer',24,24,20);circle('inner',24,24,8)
        for j,(a,b) in enumerate((((12,8),(19,18)),((36,8),(29,18)),((12,40),(19,30)),((36,40),(29,30)))):
         self.add_line(f'spoke-{j}',a,b);self.relate('connect',f'spoke-{j}','outer');self.relate('connect',f'spoke-{j}','inner')
