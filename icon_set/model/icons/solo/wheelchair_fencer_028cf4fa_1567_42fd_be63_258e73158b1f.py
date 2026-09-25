'Wheelchair Fencing Athlete.\nPlan: Seated wheelchair fencer facing right. Circular head on upper torso axis, exact head-body gap8. Extended arm and sword, large rear wheel.\nConstruction reference: human_ref/full_body_ref.png: circular detached head, coherent torso and round-ended limbs. Sword and wheelchair follow source.\nReduction: Simplify wheel spokes and sword guard to a short crossbar.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '028cf4fa-1567-42fd-be63-258e73158b1f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/fencing 1_028cf4fa-1567-42fd-be63-258e73158b1f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wheelchair-fencer'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitive', 'primitives')
    aliases = ()
    keywords = ('wheelchair', 'fencer')

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

        circle('head',18,10,4)
        self.add_line('torso',(18,22),(18,30));self.mark_human_figure('fencer',head='head',torso='torso',torso_junction='start')
        self.add_polyline('leg',(18,30),(28,30),(32,42));self.relate('connect','torso','leg')
        self.add_line('arm',(18,22),(34,22));self.relate('connect','torso','arm')
        self.add_line('guard',(34,18),(34,26));self.relate('connect','arm','guard')
        self.add_line('sword',(34,22),(42,18));self.relate('connect','sword','guard');self.relate('connect','sword','arm')
        path('wheel',(18,24),[((6,30),12,10,False),((18,42),12,12,False),((26,38),8,4,False)])
        self.relate('connect','wheel','torso');self.relate('connect','wheel','leg')
