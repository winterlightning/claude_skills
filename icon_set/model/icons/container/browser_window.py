"""Browser window: a landscape frame with a populated title bar.

Reconstructed from the reference render. The header carries the identity --
an open band, three indicator dashes on the left, and a divider separating it
from the body -- and the whole icon exists because that band is now drawable:
under the withdrawn slot rule the divider could not go below y 14 and the
dashes could not be placed at all.

Every gap in the header is exactly 8, the CONTAINER64 centerline minimum. That
is legal to sit on only because each of those measurements is
straight-to-straight, which the spacing engine evaluates exactly; the frame's
straight runs are therefore emitted as their own paths, away from the corner
arcs, so no gap is ever measured against a flattened curve.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Container64


class BrowserWindowContainer(Container64):
    icon_id = "browser-window"
    keyshape = Keyshape.HRECT_XL
    aliases = ("app-window", "web-browser-window", "window")
    keywords = ("browser", "window", "web", "page", "panel", "interface", "ui")

    def build(self) -> None:
        # HRECT_XL-64 is (0,4)-(64,60) visible, (2,6)-(62,58) centerline.
        #
        # Vertical rhythm, top down: top edge 6, dashes 14, divider 22. Two
        # gaps of 8, the minimum, and there is nothing to spend -- raising the
        # dashes runs them into the top edge and lowering them runs the
        # divider into the body.
        #
        # The frame is cut into five paths rather than two contours. Corners
        # keep their arcs, but every straight run the dashes are measured
        # against -- the top edge and the divider -- is its own path. A
        # straight-to-straight pair is measured exactly and may sit on the
        # minimum; a pair involving a flattened arc cannot be certified there
        # and comes back `review`. Each junction below is a genuine shared
        # endpoint and is declared as such.
        self.add_line("header-top", (6, 6), (58, 6))
        self.add_line("divider", (2, 22), (62, 22))

        self.add_arc("shoulder-nw-arc", (2, 10), (6, 6), radius_x=4)
        self.add_line("shoulder-nw-side", (2, 22), (2, 10))
        self.add_contour("shoulder-nw", "shoulder-nw-side", "shoulder-nw-arc")

        self.add_arc("shoulder-ne-arc", (58, 6), (62, 10), radius_x=4)
        self.add_line("shoulder-ne-side", (62, 10), (62, 22))
        self.add_contour("shoulder-ne", "shoulder-ne-arc", "shoulder-ne-side")

        self.add_line("body-right", (62, 22), (62, 54))
        self.add_arc("body-corner-se", (62, 54), (58, 58), radius_x=4)
        self.add_line("body-bottom", (58, 58), (6, 58))
        self.add_arc("body-corner-sw", (6, 58), (2, 54), radius_x=4)
        self.add_line("body-left", (2, 54), (2, 22))
        self.add_contour(
            "body",
            "body-right", "body-corner-se", "body-bottom", "body-corner-sw",
            "body-left",
        )

        for first, second in (
            ("header-top", "shoulder-nw"), ("header-top", "shoulder-ne"),
            ("divider", "shoulder-nw"), ("divider", "shoulder-ne"),
            ("divider", "body"), ("body", "shoulder-nw"), ("body", "shoulder-ne"),
        ):
            self.relate("connect", first, second)

        # Three indicator dashes, 2 units long so each paints as a stadium
        # rather than a disc. Neighbours are 8 apart, and each is 8 below the
        # top edge and 8 above the divider -- all three measured against
        # straight paths, so all three are exact.
        #
        # The reference sets them 8 from the left edge too, at x 10. That one
        # cannot be certified here: the frame's left side has to share a path
        # with the corner arc (splitting it would leave the side and the top
        # edge 5.66 apart around a corner they do not actually touch, which is
        # false crowding, not a real gap), and a gap measured against a
        # flattened arc cannot sit on the minimum. At x 12 the dashes clear
        # that curved path by 10 and everything else is unchanged; the
        # 2-unit shift is invisible at 64 pixels.
        self.add_line("light-1", (12, 14), (14, 14))
        self.add_line("light-2", (22, 14), (24, 14))
        self.add_line("light-3", (32, 14), (34, 14))
