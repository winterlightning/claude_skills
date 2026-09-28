"""Pirate Hook Hand.

Symbol plan: Round open hook and centered flared cuff, extremes8,4,40,44. Cuff shoulders share a centered stem; retain hook asymmetry.
Construction references: No useful direct Lucide match; coherent geometric contours.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f2e2b13d-530d-5217-9ecf-310a203892b9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/piracy hook hand_f2e2b13d-530d-5217-9ecf-310a203892b9.svg'
AUTHOR = 'gpt-6'


class PirateHookWithFlaredCuff(Solo48):
    icon_id = 'pirate-hook-with-flared-cuff'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    categories = ("crime", "primitives")
    aliases = ()
    keywords = ('pirate', 'hook', 'with', 'flared', 'cuff')

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

        self.add_arc('hook-top',(14,14),(34,14),radius_x=10)
        self.add_arc('hook-turn',(34,14),(24,24),radius_x=10)
        self.add_line('stem',(24,24),(24,34))
        self.add_contour('hook','hook-top','hook-turn','stem')
        path('cuff',(24,34),[(32,34),(40,44),(8,44),(16,34),(24,34)],True)
        self.relate('connect','hook','cuff')
