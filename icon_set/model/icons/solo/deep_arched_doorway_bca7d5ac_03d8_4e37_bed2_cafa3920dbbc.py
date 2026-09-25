'Deep Arched Doorway\nPlan: Concentric arched doorway with connected diagonal lower jambs for depth.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Retain the defining silhouette and visible parts.\nKeyshape: VRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bca7d5ac-03d8-4e37-bed2-cafa3920dbbc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/antechamber_bca7d5ac-03d8-4e37-bed2-cafa3920dbbc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'deep-arched-doorway'
    keyshape = Keyshape.VRECT_L
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('deep', 'arched', 'doorway')

    def build(self):

        def path(name, start, steps, closed=False):
            members, point = [], start
            for index, step in enumerate(steps):
                member = f"{name}-{index}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[((x+rx,y),rx,ry,True),((x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r):
            ellipse(name,x,y,r,r)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)

        path('outer',(8,44),[(8,20),((40,20),16,16,True),(40,44),(8,44)],True)
        path('inner',(17,35),[(17,23),((31,23),7,10,True),(31,35),(17,35)],True)
        for k,(a,b) in enumerate([((8,44),(17,35)),((40,44),(31,35))]):
            self.add_line(f'depth-{k}',a,b);self.relate('connect',f'depth-{k}','outer');self.relate('connect',f'depth-{k}','inner')
