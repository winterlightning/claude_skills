"""amazon-web-service-app-mesh: geometric reconstruction on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e445dc8e-d77f-47cd-abd6-2ae8c4e0029d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__amazon-web-service-app-mesh/20260926T064521Z-thuan-mac/reference/amazon web service app mesh_e445dc8e-d77f-47cd-abd6-2ae8c4e0029d.svg'
AUTHOR = 'claude-opus-5-5'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class AmazonWebServiceAppMesh(Solo48):
    icon_id = 'amazon-web-service-app-mesh'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('amazon', 'web', 'service', 'app', 'mesh', '_uncategorized_02')

    def build(self):
        # Revision per review: the three outer node circles are bigger (r4, were r3); the r5 hub
        # moves to (24, 28) so every node keeps 8+ from it. Links: a vertical bar from the top
        # node to the hub top, and two straight links from the hub's 3-4-5 points (20, 31) and
        # (28, 31) to the lower nodes' inner cardinal points (14, 38) and (34, 38).
        import math

        def circle(name, cx, cy, r, splits):
            pts = sorted(splits, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
            names = []
            for i, a in enumerate(pts):
                b = pts[(i + 1) % len(pts)]
                a1 = math.atan2(a[1] - cy, a[0] - cx)
                a2 = math.atan2(b[1] - cy, b[0] - cx)
                span = (a2 - a1) % (2 * math.pi)
                n = f"{name}-{i + 1}"
                self.add_arc(n, a, b, radius_x=r, large_arc=span > math.pi, sweep=True)
                names.append(n)
            self.add_contour(name, *names, closed=True)

        def cardinal(cx, cy, r):
            return [(cx - r, cy), (cx, cy - r), (cx + r, cy), (cx, cy + r)]

        circle('hub', 24, 28, 5, [(24, 23), (28, 31), (20, 31)])
        circle('top', 24, 10, 4, cardinal(24, 10, 4))
        circle('left', 10, 38, 4, cardinal(10, 38, 4))
        circle('right', 38, 38, 4, cardinal(38, 38, 4))
        self.add_line('top-link', (24, 14), (24, 23))
        self.add_line('left-link', (20, 31), (14, 38))
        self.add_line('right-link', (28, 31), (34, 38))
        for name in ['top', 'left', 'right']:
            self.relate('connect', name + '-link', name)
            self.relate('connect', name + '-link', 'hub')
