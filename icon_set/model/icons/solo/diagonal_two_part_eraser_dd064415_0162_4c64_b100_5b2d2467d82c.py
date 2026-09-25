'Diagonal Two-Part Eraser\nPlan: Rounded diagonal eraser with exact four extrema and transverse seam at shared boundary nodes.\nReference: Lucide eraser: rounded diagonal body and transverse seam.\nReduction: Retain the defining silhouette and visible parts.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dd064415-0162-4c64-b100-5b2d2467d82c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/rubber_dd064415-0162-4c64-b100-5b2d2467d82c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-two-part-eraser'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('diagonal', 'two', 'part', 'eraser')

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

        self.add_bezier('top',(26,8),((28,6),(28,6),(30,6)),((32,6),(33,7),(34,8)))
        self.add_line('upper-right',(34,8),(40,14))
        self.add_bezier('right',(40,14),((42,16),(42,16),(42,18)),((42,20),(41,21),(40,22)))
        self.add_polyline('lower-right',(40,22),(30,32),(22,40))
        self.add_bezier('bottom',(22,40),((20,42),(20,42),(18,42)),((16,42),(15,41),(14,40)))
        self.add_line('lower-left',(14,40),(8,34))
        self.add_bezier('left',(8,34),((6,32),(6,32),(6,30)),((6,28),(7,27),(8,26)))
        self.add_polyline('upper-left',(8,26),(16,18),(26,8))
        self.relate('connect','top','upper-right');self.relate('connect','upper-right','right');self.relate('connect','right','lower-right');self.relate('connect','lower-right','bottom');self.relate('connect','bottom','lower-left');self.relate('connect','lower-left','left');self.relate('connect','left','upper-left');self.relate('connect','upper-left','top')
        self.add_line('seam',(16,18),(30,32));self.relate('connect','seam','upper-left');self.relate('connect','seam','lower-right')
