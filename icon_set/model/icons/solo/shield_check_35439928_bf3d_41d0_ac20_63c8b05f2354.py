"""Shield check (apps), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35439928-bf3d-41d0-ac20-63c8b05f2354'
SOURCE_PATH = 'pictographic-primitives/apps/shield check_35439928-bf3d-41d0-ac20-63c8b05f2354.svg'
AUTHOR = 'gpt-6'

class ShieldCheck(Solo48):
    icon_id = 'shield-check'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('shield', 'check', 'apps')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (31, 19), (21, 29))
        self.add_line('e1', (21, 29), (17, 25))
        self.add_line('e2', (40, 11), (40, 24))
        self.add_line('e3', (8, 25), (8, 10))
        self.add_bezier('e4', (8, 10), *(((11.486, 8.864), (15.006, 8.209), (18.349, 6.627)), ((19.158, 6.245), (23.309, 4), (23.882, 4)), ((23.883, 4), (23.884, 4), (23.885, 4)), ((23.952, 4), (24.018, 4), (24.084, 4)), ((24.876, 4), (27.756, 5.691), (28.665, 6.109)), ((32.421, 7.855), (36.118, 9.6), (40, 11))))
        self.add_bezier('e5', (40, 24), *(((40, 24.391), (39.992, 24.791), (39.992, 25.182)), ((39.992, 26.264), (39.705, 27.445), (39.436, 28.482)), ((37.945, 34.282), (33.667, 38.182), (29.095, 41.218)), ((28.025, 41.927), (25.137, 44), (24.042, 44)), ((24.041, 44), (24.04, 44), (24.039, 44)), ((23.964, 44), (23.881, 43.991), (23.806, 43.991)), ((23.124, 43.991), (19.604, 41.627), (18.838, 41.127)), ((14.509, 38.273), (10.594, 34.645), (8.825, 29.373)), ((8.413, 28.127), (8.008, 26.709), (8.008, 25.373)), ((8.008, 25.3), (8, 25.227), (8, 25.155)), ((8, 25.073), (8, 25.082), (8, 25))))
        self.add_contour('c0', *('e0', 'e1'), closed=False)
        self.add_contour('c1', *('e4', 'e2', 'e5', 'e3'), closed=True)
