"""Handheld Semi-automatic Pistol Icon.

Symbol plan: Rectangular slide with recessed ejection port, slanted grip and trigger guard. Visible (2,6)-(46,42). Omit tiny sights and trigger.
Construction references: No useful direct Lucide subject match; geometric contour construction.
Original reference: SOURCE_PATH below; preserved subject, re-authored geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '45745e2c-a288-487b-ae80-5a5fdf0d1785'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/gun_45745e2c-a288-487b-ae80-5a5fdf0d1785.svg'
AUTHOR = 'gpt-6'


class PistolWithEjectionPort(Solo48):
    icon_id = 'pistol-with-ejection-port'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    aliases = ()
    keywords = ('pistol', 'with', 'ejection', 'port')

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
            path(name, (x-r,y), [((x+r,y),r,r,True), ((x-r,y),r,r,True)], True)

        path('pistol',(4,8),[(18,8),(30,8),(44,8),(44,24),(36,24),(24,24),(22,32),(20,40),(8,40),(12,24),(4,24),(4,8)],True)
        path('port',(18,8),[(18,16),(30,16),(30,8)])
        self.relate('connect','port','pistol')
        path('guard',(36,24),[((28,32),8,8,True),(22,32)])
        self.relate('connect','guard','pistol')
