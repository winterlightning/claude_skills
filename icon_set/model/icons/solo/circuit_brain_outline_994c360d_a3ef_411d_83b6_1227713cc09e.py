'Circuit Brain Outline\nPlan: Lobed brain above two descending circuit traces with round terminals; coherent mirrored brain crown.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Two terminals replace three; retain brain lobes and descending circuit traces.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '994c360d-a3ef-411d-83b6-1227713cc09e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/brain circuit_994c360d-a3ef-411d-83b6-1227713cc09e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circuit-brain-outline'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    keywords = ('circuit', 'brain', 'outline')

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

        self.add_bezier('brain',(12,34),((6,34),(6,30),(6,27)),((6,23),(9,23),(9,20)),((6,12),(13,9),(17,10)),((19,5),(24,6),(24,6)),((24,6),(29,5),(31,10)),((35,9),(42,12),(39,20)),((39,23),(42,23),(42,27)),((42,30),(42,34),(36,34)))
        circle('terminal-left',18,20,2);circle('terminal-right',30,20,2)
        self.add_line('trace-left',(18,22),(18,42));self.relate('connect','trace-left','terminal-left')
        self.add_line('trace-right',(30,22),(30,42));self.relate('connect','trace-right','terminal-right')
