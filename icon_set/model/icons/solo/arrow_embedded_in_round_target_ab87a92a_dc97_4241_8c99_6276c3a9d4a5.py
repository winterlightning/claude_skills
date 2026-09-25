'Arrow Embedded in Round Target\nPlan: Open target rings make space for diagonal embedded arrow; round rings centered low-left.\nReference: Lucide target: concentric circles; open source rings accommodate the arrow.\nReduction: Two rings replace three; retain shaft and angular fletching.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab87a92a-dc97-4241-8c99-6276c3a9d4a5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/calibre_ab87a92a-dc97-4241-8c99-6276c3a9d4a5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arrow-embedded-in-round-target'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('arrow', 'embedded', 'in', 'round', 'target')

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

        self.add_arc('outer',(24,6),(42,24),radius_x=18,large_arc=True,sweep=False)
        self.add_arc('inner',(15,24),(24,33),radius_x=9,sweep=False)
        self.add_line('shaft',(24,24),(42,6))
        self.add_polyline('fletching',(34,6),(34,14),(42,14));self.relate('connect','shaft','fletching')
