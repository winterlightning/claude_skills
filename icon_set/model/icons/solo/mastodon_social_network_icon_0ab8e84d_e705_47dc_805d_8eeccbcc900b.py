"""mastodon logo 3: standalone repair of supplied reference.

Plan: Rounded logo bubble containing m. Keyshape SQUARE.
Reduction: Shortened letter stems and enlarged tail gap; preserved two humps.
Construction references: local Lucide originals and atomic-debug: message-square.

All geometry is authored for SOLO48; earlier runs remain unchanged.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "0ab8e84d-e705-47dc-805d-8eeccbcc900b"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/mastodon logo 3_0ab8e84d-e705-47dc-805d-8eeccbcc900b.svg"
AUTHOR = "gpt-6"


class MastodonSocialNetworkIcon(Solo48):
    icon_id = 'mastodon-social-network-icon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("mastodon-m-logo",)
    keywords = ("mastodon", "social", "letter-m", "logo")

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
        self.add_line("m-left", (16, 23), (16, 19))
        self.add_arc("m-hump-left", (16, 19), (24, 19), radius_x=4, sweep=True)
        self.add_arc("m-hump-right", (24, 19), (32, 19), radius_x=4, sweep=True)
        self.add_line("m-right", (32, 19), (32, 23))
        self.add_contour("letter-m", "m-left", "m-hump-left", "m-hump-right", "m-right")
        self.add_line("m-middle", (24, 19), (24, 23))
        self.relate("connect", "m-middle", "letter-m")
