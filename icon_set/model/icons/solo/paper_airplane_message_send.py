"""Up-right paper airplane with a folded tail notch."""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Solo48

AUTHOR = 'astra-chatgpt'


class PaperAirplaneMessageSend(Solo48):
    """A swept paper dart whose centre fold separates the near wing."""

    icon_id = "paper-airplane-message-send"
    keyshape = Keyshape.HRECT_XL
    category = "objects/communication"
    aliases = ("paper-plane", "message-send", "send")
    keywords = (
        "send", "paper", "airplane", "plane", "message", "share",
        "submit", "mail", "dart",
    )

    def build(self) -> None:
        # The outline is authored directly to HRECT_XL's centreline extremes:
        # x=2/46 and y=5/43. The small inward turn at (24,36) is the tail
        # notch; motion lines and the far-wing crease are intentionally absent.
        self.add_polyline(
            "airplane-outline",
            (46, 5), (34, 43), (24, 36), (18, 43), (17, 31), (2, 25),
            closed=True,
        )
        self.add_line("centre-fold", (17, 31), (46, 5))
        self.relate("connect", "airplane-outline", "centre-fold")
