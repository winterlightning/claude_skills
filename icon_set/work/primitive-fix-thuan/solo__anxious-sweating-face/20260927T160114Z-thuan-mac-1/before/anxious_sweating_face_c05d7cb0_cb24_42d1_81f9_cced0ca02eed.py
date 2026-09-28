'Anxious Face with Sweat Drop.\nPlan: Worried eyes, downturned mouth and a round sweat bead with a short upper tip.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Brows and eyes combined. Droplet body made round with a short tip for a readable small sweat bead.\nKeyshape: CIRCLE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c05d7cb0-cb24-42d1-81f9-cced0ca02eed'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face anxious sweat_c05d7cb0-cb24-42d1-81f9-cced0ca02eed.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'anxious-sweating-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('anxious', 'sweating', 'face')

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

        circle('face',24,24,20)
        self.add_line('left-eye',(16,18),(19,16))
        self.add_line('right-eye',(28,15),(31,17))
        path('frown',(15,31),[((21,31),5,2,True)])
        path('sweat',(31,27),[((33,29),2,2,True),((31,31),2,2,True),((29,29),2,2,True),((31,27),2,2,True)],True)
        self.add_line('sweat-tip',(31,25),(31,27));self.relate('connect','sweat-tip','sweat')
