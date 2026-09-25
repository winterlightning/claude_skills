'Two People Side by Side.\nPlan: Two adjacent round-headed busts with shoulders meeting at the center.\nConstruction reference: human_ref/user.svg: matched circular heads and broad rounded shoulder arcs.\nReduction: Small interior arm strokes omitted; shared base and pair retained.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f9137ec-7d79-4d4a-9424-e048e82da8b3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/half brother_7f9137ec-7d79-4d4a-9424-e048e82da8b3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-adjacent-busts'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('two', 'adjacent', 'busts')

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

        for x in (14,34):circle(f'head-{x}',x,12,4)
        path('left-body',(4,40),[(4,34),((14,24),10,10,True),((24,34),10,10,True),(24,40)])
        path('right-body',(24,34),[((34,24),10,10,True),((44,34),10,10,True),(44,40)])
        self.relate('connect','left-body','right-body')
        self.add_polyline('base',(4,40),(24,40),(44,40))
        self.relate('connect','base','left-body');self.relate('connect','base','right-body')

SOURCE_REFERENCES = [('00cf88e9-707b-4bf7-9389-687cb8999fcf', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/friend_00cf88e9-707b-4bf7-9389-687cb8999fcf.svg')]
