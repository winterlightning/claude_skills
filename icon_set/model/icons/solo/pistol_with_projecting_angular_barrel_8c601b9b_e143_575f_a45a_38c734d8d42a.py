"""Handheld Pistol Firearm.

Symbol plan: Right-facing housing, projecting barrel, angled grip and curved trigger guard. Visible (2,6)-(46,42). Omit housing scratch.
Construction references: No useful direct Lucide subject match; geometric contour construction.
Original reference: SOURCE_PATH below; preserved subject, re-authored geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c601b9b-e143-575f-a45a-38c734d8d42a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/weapon_8c601b9b-e143-575f-a45a-38c734d8d42a.svg'
AUTHOR = 'gpt-6'


class PistolWithProjectingAngularBarrel(Solo48):
    icon_id = 'pistol-with-projecting-angular-barrel'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    aliases = ()
    keywords = ('pistol', 'with', 'projecting', 'angular', 'barrel')

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

        path('pistol',(8,8),[(28,8),(28,16),(44,16),(44,24),(36,24),(24,24),(22,32),(20,40),(8,40),(12,24),(4,24),(4,12),((8,8),4,4,True)],True)
        path('guard',(36,24),[((28,32),8,8,True),(22,32)])
        self.relate('connect','guard','pistol')
