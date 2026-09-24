'Arched Facade with Upper Arcade\nPlan: Wide rounded facade with two upper arch openings and central lower entrance. Width budget is 8+8+8+8+8.\nReference: Lucide landmark: regular architectural rhythm.\nReduction: Two upper arches replace three to maintain spacing.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '19554f1f-19e3-4b9e-87c9-d610d1b7dcb6'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/cloister_19554f1f-19e3-4b9e-87c9-d610d1b7dcb6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arched-facade-with-upper-arcade'
    keyshape = Keyshape.HRECT_L
    category = "objects"
    keywords = ('arched', 'facade', 'with', 'upper', 'arcade')

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

        # Open doorway replaces the baseline through the opening; mirrored upper arches share the floor.
        path('facade',(20,40),[(8,40),((4,36),4,4,True),(4,28),(4,12),((8,8),4,4,True),(40,8),((44,12),4,4,True),(44,28),(44,36),((40,40),4,4,True),(28,40)])
        self.add_polyline('floor',(4,28),(12,28),(20,28),(28,28),(36,28),(44,28))
        self.relate('connect','floor','facade')
        for k,x in enumerate((16,32)):
            path(f'window-{k}',(x-4,28),[(x-4,20),((x+4,20),4,4,True),(x+4,28)])
            self.relate('connect',f'window-{k}','floor')
        path('door',(20,40),[((28,40),4,4,True)])
        self.relate('connect','door','facade')
