"""A six-point sheriff badge carries a central round seal. No useful exact Lucide match. Keep six points and seal; omit triangle crossing lines and terminal balls to prevent crowded wedges."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eac1fcf9-1f37-433c-b879-34eecf599a76'
SOURCE_PATH = 'pictographic-primitives/protection/police badge_eac1fcf9-1f37-433c-b879-34eecf599a76.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'sheriff-star-badge'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/protection"
    aliases = ()
    keywords = ('sheriff', 'badge', 'star', 'police', 'law', 'marshal', 'security', 'officer')

    def build(self):
        # VRECT_L centerline extremes: (8,4)-(40,44).

        # Six-point star silhouette; omit overlapping triangle construction lines.
        self.add_polyline('star',(24,4),(30,14),(40,14),(36,24),(40,34),(30,34),(24,44),(18,34),(8,34),(12,24),(8,14),(18,14),closed=True)
        self.add_arc('seal-top',(21,24),(27,24),radius_x=3)
        self.add_arc('seal-bottom',(27,24),(21,24),radius_x=3)
        self.add_contour('seal','seal-top','seal-bottom',closed=True)
