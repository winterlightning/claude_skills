'Tennis player swinging racket.\nPlan: Forward-leaning tennis player with running legs and an upraised oval racket on the right.\nConstruction reference: Shared full_body_ref.png: detached circular head and flowing stick limbs.\nReduction: Fingers, racket strings and facial detail omitted; head-to-torso clearance exactly 8 centerline units.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47651662-b3cd-4b7c-a239-c37cd47aa6c6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/tennis forehand_47651662-b3cd-4b7c-a239-c37cd47aa6c6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tennis-forehand-player'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('tennis', 'forehand', 'player')

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

        circle('head',23,10,4)
        self.add_line('torso',(23,22),(19,30))
        self.add_polyline('back-arm',(23,22),(12,25),(8,30));self.relate('connect','back-arm','torso')
        self.add_polyline('racket-arm',(23,22),(29,30),(34,30));self.relate('connect','racket-arm','torso')
        self.add_polyline('legs',(6,42),(15,36),(19,30),(22,38),(24,42));self.relate('connect','legs','torso')
        ellipse('racket',38,18,4,6)
        self.add_line('shaft',(38,24),(34,30));self.relate('connect','racket','shaft');self.relate('connect','shaft','racket-arm')
        self.mark_human_figure('player',head='head',torso='torso',torso_junction='start')
