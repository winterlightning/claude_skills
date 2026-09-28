"""Law Enforcement Handcuffs Symbol.

Symbol plan: Two equal cuff circles with one tall arched connector. Visible (2,6)-(46,42). Omit doubled rims and small lock housings.
Construction references: Lucide spline: a continuous connector terminating at circular parts.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '404190ff-389e-4a15-a7fe-4b448b432ffd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/handcuffs_404190ff-389e-4a15-a7fe-4b448b432ffd.svg'
AUTHOR = 'gpt-6'


class HandcuffsWithArchedConnector(Solo48):
    icon_id = 'handcuffs-with-arched-connector'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/crime"
    aliases = ()
    keywords = ('handcuffs', 'with', 'arched', 'connector')

    def build(self):
        def path(name, start, steps, closed=False):
            ids = []
            point = start
            for i, step in enumerate(steps):
                member = f"{name}-{i}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                ids.append(member)
            self.add_contour(name, *ids, closed=closed)

        def circle(name, x, y, r):
            path(name, (x,y-r), [((x+r,y),r,r,True), ((x,y+r),r,r,True), ((x-r,y),r,r,True), ((x,y-r),r,r,True)], True)

        axis=24
        for side in (-1,1):circle(f'cuff-{side}',axis+side*13,33,7)
        path('connector',(11,26),[(11,21),((24,8),13,13,True),((37,21),13,13,True),(37,26)])
        for side in (-1,1):self.relate('connect','connector',f'cuff-{side}')
