'Worker at Conveyor Belt.\nPlan: Worker and package beside conveyor with two internal roller divisions. Head14,10 r4; torso starts14,22 exact8 gap. Bounds6..42.\nConstruction reference: human_ref/full_body_ref.png circular detached head and upright torso; source conveyor/package scene.\nReduction: Omit arm and tape; replace tiny roller circles with two internal belt divisions.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a73f189d-afeb-4835-99c1-01f3a49dee0f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/factory manufacturing line worker_a73f189d-afeb-4835-99c1-01f3a49dee0f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'worker-beside-box-on-conveyor'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('worker', 'beside', 'box', 'on', 'conveyor')

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

        circle('head',14,10,4)
        self.add_line('torso',(14,22),(14,30));self.mark_human_figure('worker',head='head',torso='torso',torso_junction='start')
        self.add_line('arm',(6,22),(19,22));self.relate('connect','arm','torso')
        box('belt',6,30,42,42,6);self.relate('connect','torso','belt')
        self.add_polyline('package',(28,30),(28,14),(42,14),(42,30));self.relate('connect','package','belt')
        for x in (18,30):self.add_line(f'roller-{x}',(x,30),(x,42));self.relate('connect',f'roller-{x}','belt')
