'Ear with Deep Inner Fold and Rounded Lobe\nPlan: Outer ear dome flows into right sweep and rounded lobe; inner fold is a coherent inward curl.\nReference: Lucide ear: open outer lobe and coherent inner fold.\nReduction: Retain the defining silhouette and visible parts.\nKeyshape: VRECT_M; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5fe7f155-57d9-4703-a38c-886ec75e5bc6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/mastoid_5fe7f155-57d9-4703-a38c-886ec75e5bc6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ear-with-deep-inner-fold-and-rounded-lobe'
    keyshape = Keyshape.VRECT_M
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('ear', 'with', 'deep', 'inner', 'fold', 'and', 'rounded', 'lobe')

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

        self.add_arc('outer-top',(10,18),(38,18),radius_x=14)
        self.add_bezier('outer-lower',(38,18),((38,29),(28,28),(28,36)),((28,41),(25,44),(20,44)),((14,44),(10,41),(10,36)))
        self.add_contour('outer','outer-top','outer-lower')
        self.add_bezier('fold',(20,30),((22,30),(23,24),(19,23)),((16,22),(18,14),(24,14)),((28,14),(29,18),(28,21)))
