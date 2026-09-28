"""A retro camera: a rounded body with a prism hump, a large round lens and a side strap line.

Symbol plan: the body is one closed rounded rectangle (r4 corners) whose top edge rises
into a trapezoid prism hump centred over the lens. The lens is one circle (r7) centred
under the hump, 8 from the body's top and bottom. A short line leaves the left wall at
lens-top height, the side detail of the reference. The reference's small shutter block
and inner lens ring cannot fit beside the hump / inside the lens at 48 and are dropped.
Lucide construction: 'camera' - rounded body with a raised top section and a circle lens.
Keyshape SQUARE: centerline x 6..42 (walls), y 6..42 (hump top, base).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6c55c909-3271-5e46-afc3-1df1e5139a05"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__camera-with-side-viewfinder/20260926T034135Z-thuan-mac/reference/camera retro_6c55c909-3271-5e46-afc3-1df1e5139a05.svg"
AUTHOR = "claude-opus-5-5"


class CameraWithSideViewfinder(Solo48):
    icon_id = "camera-with-side-viewfinder"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("retro camera", "photo camera")
    keywords = ("camera", "retro", "photo", "photography", "lens", "snapshot", "picture")

    def build(self) -> None:
        left, right, top, base, r = 6, 42, 12, 42, 4
        lens_x, lens_y, lens_r = 26, 26, 7
        side_y = 21
        # body with prism hump
        self.add_arc("corner-tl", (left, top + r), (left + r, top), radius_x=r)
        self.add_line("top-left", (left + r, top), (lens_x - 10, top))
        self.add_line("hump-left", (lens_x - 10, top), (lens_x - 6, 6))
        self.add_line("hump-top", (lens_x - 6, 6), (lens_x + 6, 6))
        self.add_line("hump-right", (lens_x + 6, 6), (lens_x + 10, top))
        self.add_line("top-right", (lens_x + 10, top), (right - r, top))
        self.add_arc("corner-tr", (right - r, top), (right, top + r), radius_x=r)
        self.add_line("wall-right", (right, top + r), (right, base - r))
        self.add_arc("corner-br", (right, base - r), (right - r, base), radius_x=r)
        self.add_line("bottom", (right - r, base), (left + r, base))
        self.add_arc("corner-bl", (left + r, base), (left, base - r), radius_x=r)
        self.add_line("wall-left-low", (left, base - r), (left, side_y))
        self.add_line("wall-left-high", (left, side_y), (left, top + r))
        self.add_contour("body", "corner-tl", "top-left", "hump-left", "hump-top", "hump-right",
                         "top-right", "corner-tr", "wall-right", "corner-br", "bottom",
                         "corner-bl", "wall-left-low", "wall-left-high", closed=True)
        # side line
        self.add_line("side-line", (left, side_y), (left + 5, side_y))
        self.relate("connect", "body", "side-line")
        # lens
        lx, ly, lr = lens_x, lens_y, lens_r
        pts = [(lx - lr, ly), (lx, ly - lr), (lx + lr, ly), (lx, ly + lr)]
        names = ("lens-nw", "lens-ne", "lens-se", "lens-sw")
        for i, name in enumerate(names):
            self.add_arc(name, pts[i], pts[(i + 1) % 4], radius_x=lr)
        self.add_contour("lens", *names, closed=True)
