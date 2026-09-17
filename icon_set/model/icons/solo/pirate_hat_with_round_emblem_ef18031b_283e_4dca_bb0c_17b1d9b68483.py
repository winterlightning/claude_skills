"""Classic Pirate Hat.

Symbol plan: Mirrored lobed hat outline about x=24, round central emblem. Visible (2,8)-(46,40). Omit four tiny emblem rays.
Construction references: No useful direct Lucide subject match; geometric contour construction.
Original reference: SOURCE_PATH below; preserved subject, re-authored geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef18031b-283e-4dca-bb0c-17b1d9b68483'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/piracy hat_ef18031b-283e-4dca-bb0c-17b1d9b68483.svg'
AUTHOR = 'gpt-6'


class PirateHatWithRoundEmblem(Solo48):
    icon_id = 'pirate-hat-with-round-emblem'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/crime"
    aliases = ()
    keywords = ('pirate', 'hat', 'with', 'round', 'emblem')

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

        path('hat',(4,26), [((14,18),10,8,True),((24,10),10,8,True),((34,18),10,8,True),((44,26),10,8,True),(36,38),(12,38),(4,26)],True)
        circle('emblem',24,24,3)
