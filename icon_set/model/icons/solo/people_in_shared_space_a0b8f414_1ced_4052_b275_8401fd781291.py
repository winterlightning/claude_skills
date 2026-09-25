'People in Shared Space.\nPlan: Three equally proportioned minimal people under open shared-space arch. All head radii2 and torso strokes4 long; head outline to torso starts is8 centerline/4 ink. Bounds6..42.\nConstruction reference: human_ref/full_body_ref.png aligned circular heads and detached torso strokes; source triangular grouping and open arch.\nReduction: Omit limbs, shorten all bodies equally, and shorten arch sides while retaining all three people.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0b8f414-1ced-4052-b275-8401fd781291'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/share play spatial experience_a0b8f414-1ced-4052-b275-8401fd781291.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'people-in-shared-space'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('people', 'in', 'shared', 'space')

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

        path('arch',(6,20),[((24,6),18,14,True),((42,20),18,14,True)])
        for j,x,y,end in ((0,14,28,42),(1,24,17,31),(2,34,28,42)):
         circle(f'head-{j}',x,y,2)
         self.add_line(f'torso-{j}',(x,y+10),(x,end));self.mark_human_figure(f'person-{j}',head=f'head-{j}',torso=f'torso-{j}',torso_junction='start')
