'Kidney-Shaped Paint Palette\nPlan: Kidney palette with inward notch and two circular paint wells; asymmetric source silhouette retained.\nReference: Lucide palette: a few separated circular wells inside an organic silhouette.\nReduction: Reduce four holes to two for legal spacing; preserve the lower-right notch.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd3ea8f6b-49cc-4787-9672-77eeeeac6b7b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/palate_d3ea8f6b-49cc-4787-9672-77eeeeac6b7b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'kidney-shaped-paint-palette'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('kidney', 'shaped', 'paint', 'palette')

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

        self.add_bezier('outline',(24,6),((34,6),(42,12),(42,22)),((42,28),(38,30),(34,30)),((30,30),(36,42),(26,42)),((14,42),(6,36),(6,25)),((6,14),(14,6),(24,6)))
        self.add_contour('palette','outline',closed=True)
        circle('well-upper',24,17,2);circle('well-left',17,29,2)
