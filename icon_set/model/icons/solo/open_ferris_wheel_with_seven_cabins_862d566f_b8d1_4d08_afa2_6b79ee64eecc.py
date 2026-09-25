# Final repair: Rebuild exact semicircular rim; draft until cabin identity can be retained.
'Open Ferris Wheel with Seven Cabins\nPlan: Circular ride rim above triangular support; seven cabin centers reduced to round marks.\nReference: Lucide ferris-wheel original and atomic-debug: rim, hub, triangular support.\nReduction: Initial sparse frame; cabin identity requires visual review.\nKeyshape: VRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '862d566f-b8d1-4d08-afa2-6b79ee64eecc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/amusement park ferris wheel_862d566f-b8d1-4d08-afa2-6b79ee64eecc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-ferris-wheel-with-seven-cabins'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    keywords = ('open', 'ferris', 'wheel', 'with', 'seven', 'cabins')

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

        path('rim',(8,20),[((40,20),16,16,True)])
        circle('hub',24,20,3)
        self.add_polyline('support',(12,44),(24,31),(36,44))
        self.add_line('base',(8,44),(40,44));self.relate('connect','base','support')
