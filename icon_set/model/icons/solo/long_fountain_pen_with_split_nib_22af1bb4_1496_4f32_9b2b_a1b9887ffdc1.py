# Final repair: Widen nib and barrel shoulder opening without changing slit meaning.
'Long Fountain Pen with Split Nib\nPlan: Diagonal fountain pen; wide nib attaches to tapered barrel and a slit meets the tip.\nReference: Lucide pencil original and atomic-debug: diagonal barrel and tapered point.\nReduction: Retain nib slit and wide shoulders; barrel taper shortened to fit.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22af1bb4-1496-4f32-9b2b-a1b9887ffdc1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/content ink pen_22af1bb4-1496-4f32-9b2b-a1b9887ffdc1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'long-fountain-pen-with-split-nib'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('long', 'fountain', 'pen', 'with', 'split', 'nib')

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

        self.add_polyline('outline',(6,42),(10,24),(18,24),(34,6),(42,14),(24,30),(24,38),(6,42),closed=True)
        self.add_line('nib-seam',(18,24),(24,30));self.relate('connect','nib-seam','outline')
        self.add_line('slit',(6,42),(14,34));self.relate('connect','slit','outline')
