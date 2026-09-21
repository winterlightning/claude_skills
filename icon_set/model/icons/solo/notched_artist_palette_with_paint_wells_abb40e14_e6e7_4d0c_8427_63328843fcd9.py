'Notched Artist Palette with Paint Wells\nPlan: Palette with lower-left thumb notch and two separated upper paint wells.\nReference: Lucide palette: separated circular wells and a flowing silhouette.\nReduction: Reduce four paint wells to two; retain deep notch and its side.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'abb40e14-e6e7-4d0c-8427-63328843fcd9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/color painting palette_abb40e14-e6e7-4d0c-8427-63328843fcd9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'notched-artist-palette-with-paint-wells'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('notched', 'artist', 'palette', 'with', 'paint', 'wells')

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

        self.add_bezier('outline',(24,6),((35,6),(42,14),(42,24)),((42,34),(35,42),(29,42)),((24,42),(20,31),(16,31)),((12,31),(15,38),(12,38)),((8,38),(6,29),(6,24)),((6,14),(13,6),(24,6)))
        self.add_contour('palette','outline',closed=True)
        circle('well-left',18,19,2);circle('well-right',31,24,2)
