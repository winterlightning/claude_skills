'Front Facing Car under Spray\nPlan: Front car under two rows of spray marks; mirrored front and tires.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: One spray row replaces two; headlights omitted to retain front silhouette and wash marks.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8878e02-6a89-4f38-91b2-1f4b7dd92fdd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/car repair wash 1_e8878e02-6a89-4f38-91b2-1f4b7dd92fdd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'front-facing-car-under-spray'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('front', 'facing', 'car', 'under', 'spray')

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

        self.add_polyline('body',(6,29),(12,20),(36,20),(42,29),(42,38),(6,38),(6,29))
        self.add_line('windshield',(6,29),(42,29));self.relate('connect','windshield','body')
        for i,x in enumerate([14,34]):self.add_line(f'tire-{i}',(x,38),(x,42));self.relate('connect',f'tire-{i}','body')
        for i,x in enumerate([12,24,36]):self.add_line(f'spray-{i}',(x,6),(x-1,11))
