"""Diagonal kayak and matching teardrop paddle blades reconstructed from the original source and the inspected Lucide kayak original/atomic-debug. Shared bow/stern and shaft nodes preserve exact contacts. The cockpit variant uses a larger elliptical opening and shows the shaft outside the raised cockpit rim; the center portion is occluded by the seat. Deliberate diagonal orientation fits the complete subject on SQUARE without broken paddle tips.

Horizontal pointed kayak with a full double-ended paddle above it; keep the elongated cockpit in the cockpit variant. All four hull quarters share smooth tangents at the widest points. Source kayak and Lucide sailboat inspected; the horizontal layout preserves complete paddle blades without trapping wedges against the hull.

Reconstruct the pointed kayak with mirrored hull curves and two matching rounded paddle blades. Paddle moved alongside to preserve both blades and the cockpit counter at SOLO48. Source kayak inspected; Lucide sailboat informs a coherent hull, with deliberate equipment asymmetry.

Reconstruct the pointed kayak with mirrored hull curves and two matching rounded paddle blades. Paddle moved alongside to preserve both blades and the cockpit counter at SOLO48. Source kayak inspected; Lucide sailboat informs a coherent hull, with deliberate equipment asymmetry.

Kayak with Paddle, re-authored from its reference on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7a66c4e2-1e93-4712-9eb5-ab0c546777d9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__kayak-with-paddle/20260927T101636Z-thuan-mac-1/reference/kayak_7a66c4e2-1e93-4712-9eb5-ab0c546777d9.svg'
AUTHOR = 'gpt-6'

class KayakWithPaddle(Solo48):
    icon_id = 'kayak-with-paddle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('kayak', 'paddle', 'canoe', 'boat', 'water sports', 'rowing', 'river', 'outdoor')

    def ring(self, name, x, y, r):
        self.add_arc(name + '-a', (x - r, y), (x + r, y), radius_x=r)
        self.add_arc(name + '-b', (x + r, y), (x - r, y), radius_x=r)
        self.add_contour(name, name + '-a', name + '-b', closed=True)

    def branches(self, branches):
        parts = []
        for name, points in branches:
            members = []
            for i, (a, b) in enumerate(zip(points, points[1:])):
                key = f'{name}-{i}'
                self.add_line(key, a, b)
                members.append(key)
                parts.append((key, a, b))
            if len(members) > 1:
                self.add_contour(name, *members)
        for i, (name, a, b) in enumerate(parts):
            for other, c, d in parts[i + 1:]:
                if a in (c, d) or b in (c, d):
                    self.relate('connect', name, other)

    def build(self):
        # A pointed vertical kayak with a distinct diagonal two-bladed paddle.
        self.add_bezier('hull-nw',(24,6),((17,11),(10,17),(10,24)))
        self.add_bezier('hull-sw',(10,24),((10,31),(17,37),(24,42)))
        self.add_bezier('hull-se',(24,42),((31,37),(38,31),(38,24)))
        self.add_bezier('hull-ne',(38,24),((38,17),(31,11),(24,6)))
        self.add_contour('hull','hull-nw','hull-sw','hull-se','hull-ne',closed=True)
        self.add_line('shaft',(8,40),(40,8))
        self.add_line('blade-ne',(38,6),(42,10))
        self.add_line('blade-sw',(6,38),(10,42))
        self.relate('connect','shaft','blade-ne')
        self.relate('connect','shaft','blade-sw')
        self.relate('connect','shaft','hull')
