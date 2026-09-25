'Heart Engagement Ring.\nPlan: Heart jewel above an open circular ring band; four exact quarter arcs form the heart lobes.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e240258-45ce-4bd1-bbcb-cc2aef7950e7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/lgbt engagement ring_0e240258-45ce-4bd1-bbcb-cc2aef7950e7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'heart-set-engagement-ring'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('heart', 'set', 'engagement', 'ring')

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

        path('heart',(24,12),[((16,4),8,8,False),((8,12),8,8,False),(24,24),(40,12),((32,4),8,8,False),((24,12),8,8,False)],True)
        self.add_arc('band',(12,26),(36,26),radius_x=13,radius_y=13,large_arc=True,sweep=False)
