"""Three kitchen knives hanging on a magnetic wall rack.

SOLO48 HRECT_L: visible (2, 6)-(46, 42), centerline (4, 8)-(44, 40).

Symbol plan: a straight rack bar at y=20 spans the width, split wherever a
knife meets it. Three identical knives, 8 wide and 8 apart (x=4, 20, 36):
above the bar a handle with straight sides and a r4 rounded butt reaching
y=8; below it a blade with a straight vertical spine and a cutting edge that
leaves the bolster vertically and sweeps to the point at y=40 (a r29 arc
about (x-21, 20), the radius that is tangent at the top and passes the tip
exactly).
Revision: the rejected drawing gave stick handles and short D-shaped blades
that read as hooks; each knife now has a handle and a long pointed blade.
Construction reference: no useful Lucide match (`utensils` knife checked
for the spine-and-curved-edge blade).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3d46c4b2-e4b0-4c4b-9f88-76961d7a269e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__magnetic-knife-rack-three-knives/20260926T160211Z-thuan-mac-1/reference/kitchen knife set_3d46c4b2-e4b0-4c4b-9f88-76961d7a269e.svg'
AUTHOR = 'claude-opus-5-5'

BAR_Y, HANDLE_SIDE_TOP, BUTT_R, TIP_Y = 20, 12, 4, 40
KNIFE_XS, KNIFE_W, EDGE_R = (4, 20, 36), 8, 29


class Drawing(Solo48):
    icon_id = 'magnetic-knife-rack-three-knives'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('kitchen knife set', 'knife rack')
    keywords = ('knife', 'knives', 'kitchen', 'rack', 'magnetic', 'chef', 'cutlery', 'cooking')

    def build(self):
        xs = KNIFE_XS
        # bar pieces between knives
        stops = [xs[0]]
        for x in xs:
            stops += [x, x + KNIFE_W]
        stops = sorted(set(stops))
        for i in range(len(stops) - 1):
            self.add_line(f'bar-{i}', (stops[i], BAR_Y), (stops[i + 1], BAR_Y))
        for k, x in enumerate(xs):
            r = x + KNIFE_W
            self.add_line(f'handle-{k}-l', (x, BAR_Y), (x, HANDLE_SIDE_TOP))
            self.add_arc(f'handle-{k}-butt', (x, HANDLE_SIDE_TOP), (r, HANDLE_SIDE_TOP), radius_x=BUTT_R, sweep=True)
            self.add_line(f'handle-{k}-r', (r, HANDLE_SIDE_TOP), (r, BAR_Y))
            self.add_contour(f'handle-{k}', f'handle-{k}-l', f'handle-{k}-butt', f'handle-{k}-r')
            self.add_line(f'blade-{k}-spine', (x, BAR_Y), (x, TIP_Y))
            self.add_arc(f'blade-{k}-edge', (x, TIP_Y), (r, BAR_Y), radius_x=EDGE_R, sweep=False)
            self.add_contour(f'blade-{k}', f'blade-{k}-spine', f'blade-{k}-edge')
            seg = stops.index(x)
            self.relate('connect', f'handle-{k}', f'bar-{seg}')
            self.relate('connect', f'blade-{k}', f'bar-{seg}')
            self.relate('connect', f'handle-{k}', f'blade-{k}')
            for j in range(len(stops) - 1):
                if stops[j + 1] == x or stops[j] == r:
                    self.relate('connect', f'handle-{k}', f'bar-{j}')
                    self.relate('connect', f'blade-{k}', f'bar-{j}')
        for i in range(len(stops) - 2):
            self.relate('connect', f'bar-{i}', f'bar-{i + 1}')
