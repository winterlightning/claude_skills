"""Adjustable-brightness bulb reconstructed from the supplied reference."""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48


SOURCE_ICON_ID = "afa0c105-3fb7-4c77-b44d-80888cf292ec"
SOURCE_PATH = 'pictographic-primitives/_uncategorized_01/adjustable lamp 1_afa0c105-3fb7-4c77-b44d-80888cf292ec.svg'
AUTHOR = 'gpt-6'


class AdjustableBrightnessLightBulb(Solo48):
    icon_id = "adjustable-brightness-light-bulb"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/lighting"
    aliases = ("dimmable-light-bulb", "adjustable-lamp")
    keywords = ("bulb", "brightness", "dimmer", "lamp", "light", "control")

    def build(self) -> None:
        # Plan: the root owns three siblings: a broad three-arc adjustment
        # stroke, a vertically symmetric bulb, and one circular indicator.
        # The arc sections share tangent directions at their exact endpoints;
        # the bulb derives mirrored shoulders and necks from axis_x.
        axis_x = 21

        self.add_arc(
            "adjustment-lower-left",
            (10, 36),
            (6, 24),
            radius_x=4,
            radius_y=12,
        )
        self.add_arc(
            "adjustment-upper-left",
            (6, 24),
            (24, 6),
            radius_x=18,
        )
        self.add_arc(
            "adjustment-upper-right",
            (24, 6),
            (38, 12),
            radius_x=14,
            radius_y=6,
        )
        self.add_contour(
            "adjustment-arc",
            "adjustment-lower-left",
            "adjustment-upper-left",
            "adjustment-upper-right",
        )

        head_rx, head_ry, head_y = 6, 6, 23
        shoulder_radius = 5
        shoulder_offset, shoulder_step = 2, 4
        neck_half_width = 3
        seam_y = 31
        base_depth = 8

        self.add_arc(
            "bulb-head",
            (axis_x - head_rx, head_y),
            (axis_x + head_rx, head_y),
            radius_x=head_rx,
            radius_y=head_ry,
        )
        self.add_arc(
            "bulb-right-shoulder",
            (axis_x + head_rx, head_y),
            (axis_x + head_rx - shoulder_offset, head_y + shoulder_step),
            radius_x=shoulder_radius,
        )
        self.add_arc(
            "bulb-right-neck",
            (axis_x + head_rx - shoulder_offset, head_y + shoulder_step),
            (axis_x + neck_half_width, seam_y),
            radius_x=shoulder_radius,
            sweep=False,
        )
        self.add_arc(
            "bulb-base-right",
            (axis_x + neck_half_width, seam_y),
            (axis_x, seam_y + base_depth),
            radius_x=neck_half_width,
            radius_y=base_depth,
        )
        self.add_arc(
            "bulb-base-left",
            (axis_x, seam_y + base_depth),
            (axis_x - neck_half_width, seam_y),
            radius_x=neck_half_width,
            radius_y=base_depth,
        )
        self.add_arc(
            "bulb-left-neck",
            (axis_x - neck_half_width, seam_y),
            (axis_x - head_rx + shoulder_offset, head_y + shoulder_step),
            radius_x=shoulder_radius,
            sweep=False,
        )
        self.add_arc(
            "bulb-left-shoulder",
            (axis_x - head_rx + shoulder_offset, head_y + shoulder_step),
            (axis_x - head_rx, head_y),
            radius_x=shoulder_radius,
        )
        self.add_contour(
            "bulb-outline",
            "bulb-head",
            "bulb-right-shoulder",
            "bulb-right-neck",
            "bulb-base-right",
            "bulb-base-left",
            "bulb-left-neck",
            "bulb-left-shoulder",
            closed=True,
        )
        self.add_line("bulb-contact", (axis_x, seam_y + base_depth), (axis_x, 42))
        self.relate("connect", "bulb-base-right", "bulb-contact")
        self.relate("connect", "bulb-base-left", "bulb-contact")

        indicator_center = (39, 30)
        indicator_radius = 3
        self.add_arc(
            "indicator-top",
            (indicator_center[0] - indicator_radius, indicator_center[1]),
            (indicator_center[0] + indicator_radius, indicator_center[1]),
            radius_x=indicator_radius,
        )
        self.add_arc(
            "indicator-bottom",
            (indicator_center[0] + indicator_radius, indicator_center[1]),
            (indicator_center[0] - indicator_radius, indicator_center[1]),
            radius_x=indicator_radius,
        )
        self.add_contour(
            "brightness-indicator",
            "indicator-top",
            "indicator-bottom",
            closed=True,
        )
