"""Double-Edge Razor Blade.

Symbol plan: Double-edge razor blade with mirrored end notches and a central rounded slot. Orient horizontally and omit the tiny slot extensions and end ticks.
HRECT_L centerline extremes (4,8)-(44,40); exact envelope selected for the subject's proportions.
Construction reference: No useful exact Lucide blade match; reconstruct the source as one symmetric notched blade with a clear central opening.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '954cbc20-8d2e-44ae-b48a-f47084c00d57'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__double-edge-razor-blade/20260927T070927Z-thuan-mac-1/reference/razor tool_954cbc20-8d2e-44ae-b48a-f47084c00d57.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'double-edge-razor-blade'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('razor', 'blade', 'shaving', 'barber', 'grooming', 'cutting', 'tool', 'edge')

    def build(self) -> None:
        # Rotate the blade toward the source's diamond silhouette; preserve side nicks.
        self.add_polyline('blade',(24,6),(42,24),(38,28),(40,30),
                          (24,42),(6,24),(10,20),(8,18),closed=True)
        self.add_polyline('slot',(24,18),(30,24),(24,30),(18,24),closed=True)
