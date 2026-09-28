"""Exposure compensation, outlined: an outlined minus bar and an outlined plus on either
side of a diagonal slash.

Symbol plan: the outlined minus is a bar outline 12x8 in the upper-left corner, the
outlined plus is a cross outline (arms 8 wide, span 16) centred (34,34) in the
lower-right corner, and the slash runs on x+y=44 from (8,36) to (36,8), 8.5 clear of the
minus corner and 11 of the plus notch. The reference's rounded-square frame is dropped (inside
it no outlined plus fits with 8-unit clearances).
Lucide construction: 'plus'/'minus' as outlined shapes; 'slash'.
Keyshape SQUARE: centerline x 6..42, y 6..42.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7e0c4b3a-5601-40b2-8ea5-02186da2356f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__exposure-compensation-outlined/20260926T035939Z-thuan-mac/reference/light mode exposure_7e0c4b3a-5601-40b2-8ea5-02186da2356f.svg"
AUTHOR = "claude-opus-5-5"


class ExposureCompensationOutlined(Solo48):
    icon_id = "exposure-compensation-outlined"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography/settings"
    aliases = ("light-mode-exposure", "exposure-outlined")
    keywords = ("exposure", "compensation", "plus", "minus", "outlined", "camera", "ev", "photo")

    def build(self) -> None:
        self.add_polyline("minus", (6, 6), (18, 6), (18, 14), (6, 14), closed=True)
        c, a, h = 34, 4, 8
        self.add_polyline("plus", (c - a, c - h), (c + a, c - h), (c + a, c - a), (c + h, c - a),
                          (c + h, c + a), (c + a, c + a), (c + a, c + h), (c - a, c + h),
                          (c - a, c + a), (c - h, c + a), (c - h, c - a), (c - a, c - a), closed=True)
        self.add_line("slash", (8, 36), (36, 8))
