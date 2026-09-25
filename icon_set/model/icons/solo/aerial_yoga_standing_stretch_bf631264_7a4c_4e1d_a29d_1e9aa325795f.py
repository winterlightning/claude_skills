'Aerial Yoga Standing Stretch Pose.\nPlan: Leaning figure with exact diagonal head-neck spacing: sqrt(5²+12²)-5=8 centerline. Raised rightward arms preserve stretching action.\nConstruction reference: human_ref/full_body_ref.png: circular detached head aligned to upper torso.\nReduction: Parallel arms merged into one clear raised arm stroke to preserve head clearance.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bf631264-7a4c-4e1d-a29d-1e9aa325795f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/aerial yoga basic pose_bf631264-7a4c-4e1d-a29d-1e9aa325795f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'aerial-yoga-standing-stretch'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('aerial', 'yoga', 'standing', 'stretch')

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

        circle('head',23,11,5)
        self.add_line('torso',(18,23),(13,35))
        self.add_polyline('legs',(6,42),(13,35),(26,42));self.relate('connect','torso','legs')
        self.add_polyline('arms',(18,23),(30,28),(42,6));self.relate('connect','torso','arms')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
