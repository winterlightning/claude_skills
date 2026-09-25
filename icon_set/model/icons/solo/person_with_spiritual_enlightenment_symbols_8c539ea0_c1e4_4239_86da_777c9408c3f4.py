"""A centered spiritual bust beneath three inward marks and a broad aura."""

from ...keyshapes import Keyshape
from ._base import Solo48


SOURCE_ICON_ID = "8c539ea0-c1e4-4239-86da-777c9408c3f4"
SOURCE_PATH = "pictographic-primitives/_uncategorized_04/asalha puja_8c539ea0-c1e4-4239-86da-777c9408c3f4.svg"
AUTHOR = "gpt-5"


class PersonWithSpiritualEnlightenmentSymbols(Solo48):
    icon_id = "person-with-spiritual-enlightenment-symbols"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("person-with-aura", "spiritual-enlightenment")
    keywords = ("person", "aura", "enlightenment", "spiritual", "meditation")
    human_construction = "bust"

    def build(self) -> None:
        # Plan: a radius-20 open aura surrounds three inward marks. The central
        # bust follows human_ref/user.svg: circular head and broad shoulders,
        # here joined at one exact neck point as a declared bust contact.
        self.add_arc(
            "aura",
            (8, 36),
            (40, 36),
            radius_x=20,
            large_arc=True,
        )

        self.add_polyline("mark-center", (21, 13), (24, 17), (27, 13))
        self.add_line("mark-left", (13, 22), (16, 20))
        self.add_line("mark-right", (35, 22), (32, 20))

        head_cx, head_cy, head_radius = 24, 29, 4
        self.add_arc(
            "head-top",
            (head_cx - head_radius, head_cy),
            (head_cx + head_radius, head_cy),
            radius_x=head_radius,
        )
        self.add_arc(
            "head-bottom",
            (head_cx + head_radius, head_cy),
            (head_cx - head_radius, head_cy),
            radius_x=head_radius,
        )
        self.add_contour("head", "head-top", "head-bottom", closed=True)

        neck = (24, 33)
        self.add_line("shoulder-right", neck, (32, 39))
        self.add_line("torso-right", (32, 39), (32, 42))
        self.add_line("torso-base", (32, 42), (16, 42))
        self.add_line("torso-left", (16, 42), (16, 39))
        self.add_line("shoulder-left", (16, 39), neck)
        self.add_contour(
            "body",
            "shoulder-right",
            "torso-right",
            "torso-base",
            "torso-left",
            "shoulder-left",
            closed=True,
        )
        self.relate("connect", "head", "body")
