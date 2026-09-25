'Stepped Tower with Spire\nPlan: Stepped tower with central spire; shared eight-unit tower widths.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Omit facade marks, retain stepped masses and spire.\nKeyshape: VRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '594d48c3-e95a-4c24-ab70-9732672baf73'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/burj kalifa uae_594d48c3-e95a-4c24-ab70-9732672baf73.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'stepped-tower-with-spire'
    keyshape = Keyshape.VRECT_L
    category = "primitives-generate"
    keywords = ('stepped', 'tower', 'with', 'spire')

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

        self.add_polyline('silhouette',(8,44),(8,32),(16,32),(16,16),(24,16),(24,8),(32,8),(32,24),(40,24),(40,44),(8,44))
        self.add_line('spire',(28,4),(28,8));self.relate('connect','spire','silhouette')
        self.add_line('central',(24,16),(24,44));self.relate('connect','central','silhouette')
