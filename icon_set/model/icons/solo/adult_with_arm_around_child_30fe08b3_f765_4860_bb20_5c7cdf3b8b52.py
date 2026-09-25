'Adult and Child Together.\nPlan: Two stick figures with shared limb vocabulary. Adult head r4 at14,10; neck14,22 gives exact 4u ink gap. Child r3 at36,20; neck36,31 also exact 4u.\nConstruction reference: human_ref/full_body_ref.png: circular heads and round-ended limbs.\nReduction: Body outlines reduced to shared stick-figure vocabulary.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30fe08b3-f765-4860-bb20-5c7cdf3b8b52'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/family child hold hand_30fe08b3-f765-4860-bb20-5c7cdf3b8b52.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'adult-with-arm-around-child'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('adult', 'with', 'arm', 'around', 'child')

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

        circle('adult-head',14,10,4)
        self.add_line('adult-torso',(14,22),(14,34))
        self.add_polyline('adult-legs',(6,42),(14,34),(22,42));self.relate('connect','adult-torso','adult-legs')
        self.add_polyline('adult-arms',(6,26),(14,22),(24,31),(36,31));self.relate('connect','adult-arms','adult-torso')
        circle('child-head',36,20,3)
        self.add_line('child-torso',(36,31),(36,34));self.relate('connect','child-torso','adult-arms')
        self.add_polyline('child-legs',(32,42),(36,34),(40,42));self.relate('connect','child-torso','child-legs')
        self.add_line('child-arm',(36,31),(42,31));self.relate('connect','child-arm','child-torso');self.relate('connect','child-arm','adult-arms')
        self.mark_human_figure('adult',head='adult-head',torso='adult-torso',torso_junction='start')
        self.mark_human_figure('child',head='child-head',torso='child-torso',torso_junction='start')
