'Triple Wavy Water Surface.\nPlan: Three equal shallow waves with repeated crests and troughs and equal spacing. Bounds4,8..44,40.\nReference: Lucide wind curve vocabulary; no exact local water-wave match selected. Original three-wave count retained.\nKeyshape: HRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ec59703e-9d3e-4c04-b69e-ed8714a9e950'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/surface_ec59703e-9d3e-4c04-b69e-ed8714a9e950.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-water-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('three', 'water', 'waves')

    def build(self):
        def path(name, start, steps, closed=False):
            members = []
            point = start
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

        def circle(name, x, y, radius):
            path(name, (x-radius,y), [((x+radius,y),radius,radius,True),
                 ((x-radius,y),radius,radius,True)], True)

        def box(name, left, top, right, bottom, radius):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        for j,y in enumerate((10,24,38)):path(f'wave-{j}',(4,y),[((14,y),5,2,True),((24,y),5,2,False),((34,y),5,2,True),((44,y),5,2,False)])

SOURCE_REFERENCES = [('29f990c2-3ab5-475e-bcfa-6c296ca4b942', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/surface_29f990c2-3ab5-475e-bcfa-6c296ca4b942.svg')]
