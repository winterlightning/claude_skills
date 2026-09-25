"""mastodon logo 2: standalone repair of supplied reference.

Plan: Rounded logo bubble with bottom tail. Keyshape SQUARE.
Reduction: Interior rings reduced to three equal dots; tail opening enlarged.
Construction references: local Lucide originals and atomic-debug: message-square.

All geometry is authored for SOLO48; earlier runs remain unchanged.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "5728b0bd-4ca7-4880-8dd9-2620444de10e"
SOURCE_PATH = "pictographic-primitives/_uncategorized_26/mastodon logo 2_5728b0bd-4ca7-4880-8dd9-2620444de10e.svg"
AUTHOR = "gpt-6"


class MastodonSocialNetworkLogo(Solo48):
    icon_id = 'mastodon-social-network-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("mastodon-chat-logo",)
    keywords = ("mastodon", "social", "bubble", "three-dots")

    def build(self) -> None:
        self.add_line("top", (16, 6), (32, 6))
        self.add_arc("upper-right", (32, 6), (42, 16), radius_x=10, sweep=True)
        self.add_line("right", (42, 16), (42, 25))
        self.add_arc("lower-right", (42, 25), (35, 32), radius_x=7, sweep=True)
        self.add_line("underbody", (35, 32), (18, 32))
        self.add_line("tail-descend", (18, 32), (23, 42))
        self.add_line("tail-return", (23, 42), (16, 40))
        self.add_arc("lower-left", (16, 40), (6, 30), radius_x=10, sweep=True)
        self.add_line("left", (6, 30), (6, 16))
        self.add_arc("upper-left", (6, 16), (16, 6), radius_x=10, sweep=True)
        self.add_contour("outline", "top", "upper-right", "right", "lower-right",
                         "underbody", "tail-descend", "tail-return", "lower-left",
                         "left", "upper-left", closed=True)
        for index, x in enumerate((15, 24, 33)):
            self.add_dot(f"message-mark-{index}", (x, 20))
