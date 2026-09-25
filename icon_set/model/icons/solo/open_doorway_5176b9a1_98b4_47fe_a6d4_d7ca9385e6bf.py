'Open Entrance Doorway.\nPlan: Open doorway with angled open door and isolated knob. Bounds8,4..40,44.\nConstruction reference: Lucide door-open original/atomic-debug angled slab, jamb and knob.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5176b9a1-98b4-47fe-a6d4-d7ca9385e6bf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/left door open_5176b9a1-98b4-47fe-a6d4-d7ca9385e6bf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-doorway'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('open', 'doorway')

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

        def ellipse(name, x, y, rx, ry):
            path(name, (x-rx,y), [((x+rx,y),rx,ry,True), ((x-rx,y),rx,ry,True)], True)

        def circle(name, x, y, radius):
            ellipse(name,x,y,radius,radius)

        def box(name, left, top, right, bottom, radius=4):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        self.add_polyline('frame',(8,44),(8,4),(40,4),(40,44))
        self.add_polyline('door',(8,4),(28,16),(28,36),(8,44))
        self.relate('connect','frame','door')
        self.add_dot('knob',(20,26))
