"""A display camera: a wide rounded body with a broad raised top block and a large round lens.

Symbol plan: one closed outline - a rounded rectangle body (r4 corners) whose top edge
rises into a broad rounded block (r3 top corners), symmetric about x=24. The block opens
into the body (no divider line) so the lens can be large. The lens is one circle (r6)
on the axis, 9 above the base and clear of the block's inner corners.
Lucide construction: 'camera' - body outline with a raised top section and a circle lens.
Keyshape HRECT_L: centerline x 4..44 (walls), y 8..40 (block top, base).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "c8b17656-f666-5e6c-a3ff-976538f73f05"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__camera-with-top-handle/20260926T034135Z-thuan-mac/reference/camera display_c8b17656-f666-5e6c-a3ff-976538f73f05.svg"
AUTHOR = "claude-opus-5-5"


class CameraWithTopHandle(Solo48):
    icon_id = "camera-with-top-handle"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("display camera", "camera")
    keywords = ("camera", "photo", "photography", "lens", "picture", "snapshot")

    def build(self) -> None:
        ax = 24
        left, right, top, base, r = 4, 44, 16, 40, 4
        bw, btop, br = 12, 8, 3  # block half-width, top, corner radius
        lens_y, lens_r = 25, 6
        self.add_arc("corner-tl", (left, top + r), (left + r, top), radius_x=r)
        self.add_line("top-left", (left + r, top), (ax - bw, top))
        self.add_line("block-left", (ax - bw, top), (ax - bw, btop + br))
        self.add_arc("block-corner-l", (ax - bw, btop + br), (ax - bw + br, btop), radius_x=br)
        self.add_line("block-top", (ax - bw + br, btop), (ax + bw - br, btop))
        self.add_arc("block-corner-r", (ax + bw - br, btop), (ax + bw, btop + br), radius_x=br)
        self.add_line("block-right", (ax + bw, btop + br), (ax + bw, top))
        self.add_line("top-right", (ax + bw, top), (right - r, top))
        self.add_arc("corner-tr", (right - r, top), (right, top + r), radius_x=r)
        self.add_line("wall-right", (right, top + r), (right, base - r))
        self.add_arc("corner-br", (right, base - r), (right - r, base), radius_x=r)
        self.add_line("bottom", (right - r, base), (left + r, base))
        self.add_arc("corner-bl", (left + r, base), (left, base - r), radius_x=r)
        self.add_line("wall-left", (left, base - r), (left, top + r))
        self.add_contour("body", "corner-tl", "top-left", "block-left", "block-corner-l",
                         "block-top", "block-corner-r", "block-right", "top-right", "corner-tr",
                         "wall-right", "corner-br", "bottom", "corner-bl", "wall-left", closed=True)
        pts = [(ax - lens_r, lens_y), (ax, lens_y - lens_r), (ax + lens_r, lens_y), (ax, lens_y + lens_r)]
        names = ("lens-nw", "lens-ne", "lens-se", "lens-sw")
        for i, name in enumerate(names):
            self.add_arc(name, pts[i], pts[(i + 1) % 4], radius_x=lens_r)
        self.add_contour("lens", *names, closed=True)
