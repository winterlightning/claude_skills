'Head Wearing Medical Face Mask.\nPlan: Left-facing head wearing a broad face mask with one strap leading toward the ear.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Ear outline and second strap stroke omitted; mask remains the defining feature.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4977c27d-8c14-4509-a7d1-6da59ee108a0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/head side mask_4977c27d-8c14-4509-a7d1-6da59ee108a0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'masked-head-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('masked', 'head', 'profile')

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

        path('head',(18,44),[(18,36),(10,32),(8,24),(14,18),((40,18),13,14,True),(40,32),((32,40),8,8,True),(32,44)])
        self.add_polyline('mask',(8,24),(24,24),(24,32),(24,36),(18,36));self.relate('connect','mask','head')
        self.add_line('strap',(24,24),(31,19));self.relate('connect','strap','mask')
