'Tuxedo Suit with Bow Tie.\nPlan: Formal jacket with two lapels and a two-wing bow tie.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9451716-545e-4b2d-baaa-edadd03ed515'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/tuxedo_f9451716-545e-4b2d-baaa-edadd03ed515.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tuxedo-bow-tie'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('tuxedo', 'bow', 'tie')

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

        path('jacket',(12,20),[(8,24),(10,44),(24,44),(38,44),(40,24),(36,20)])
        self.add_polyline('lapels',(12,20),(24,36),(36,20));self.relate('connect','lapels','jacket')
        self.add_line('seam',(24,36),(24,44));self.relate('connect','seam','lapels');self.relate('connect','seam','jacket')
        path('bow-left',(12,20),[(12,4),(24,12),(12,20)],True);path('bow-right',(36,20),[(36,4),(24,12),(36,20)],True)
        for bow in ('bow-left','bow-right'):
         self.relate('connect',bow,'jacket');self.relate('connect',bow,'lapels')
        self.relate('connect','bow-left','bow-right')
