'Hand Gripper Exerciser.\nPlan: Two equal rounded rope handles, mirrored suspension arcs and a small upper rope loop.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Reference is a schematic skipping rope, not a hand gripper. Both handles and upper loop retained.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7be3fb9b-2826-4b84-92ca-586f25b9c48c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/jumping rope 1_7be3fb9b-2826-4b84-92ca-586f25b9c48c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'skipping-rope-top-loop'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'Uncategorized'
    aliases = ()
    keywords = ('skipping', 'rope', 'top', 'loop')

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

        circle('loop',24,7,3)
        path('rope-left',(24,10),[((14,28),26,26,False)])
        path('rope-right',(24,10),[((34,28),26,26,True)])
        self.relate('connect','loop','rope-left');self.relate('connect','loop','rope-right');self.relate('connect','rope-left','rope-right')
        for j,left in enumerate((8,28)):
         box(f'handle-{j}',left,28,left+12,44,6)
         self.relate('connect',f'handle-{j}',f'rope-{("left","right")[j]}')
