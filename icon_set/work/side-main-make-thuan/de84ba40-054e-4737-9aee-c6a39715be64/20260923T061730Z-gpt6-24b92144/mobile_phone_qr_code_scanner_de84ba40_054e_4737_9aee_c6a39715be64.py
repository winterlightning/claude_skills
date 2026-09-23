"""A mobile phone displaying four QR-like corner marks."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "de84ba40-054e-4737-9aee-c6a39715be64"
SOURCE_PATH = "pictographic-primitives/other/mobile phone qr code_de84ba40-054e-4737-9aee-c6a39715be64.svg"
AUTHOR = "gpt-6"


class MobilePhoneQrCodeScanner(Solo48):
    icon_id = "mobile-phone-qr-code-scanner"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("qr phone", "mobile qr code")
    keywords = ("smartphone", "qr", "scan", "payment")

    def build(self) -> None:
        self.add_line("top", (12, 4), (36, 4))
        self.add_arc("ne", (36, 4), (40, 8), radius_x=4)
        self.add_line("right-screen", (40, 8), (40, 36))
        self.add_line("right-footer", (40, 36), (40, 40))
        self.add_arc("se", (40, 40), (36, 44), radius_x=4)
        self.add_line("bottom", (36, 44), (12, 44))
        self.add_arc("sw", (12, 44), (8, 40), radius_x=4)
        self.add_line("left-footer", (8, 40), (8, 36))
        self.add_line("left-screen", (8, 36), (8, 8))
        self.add_arc("nw", (8, 8), (12, 4), radius_x=4)
        self.add_contour("phone-frame", "top", "ne", "right-screen",
                         "right-footer", "se", "bottom", "sw",
                         "left-footer", "left-screen", "nw", closed=True)
        self.add_line("footer", (8, 36), (40, 36))
        self.relate("connect", "footer", "left-screen")
        self.relate("connect", "footer", "right-screen")

        # The reference alternates two square finder marks and two L marks.
        # Solid marks keep the same diagonal placement on this denser canvas.
        self.add_dot("finder-nw", (18, 16))
        self.add_polyline("finder-ne", (28, 15), (31, 15), (31, 18))
        self.add_polyline("finder-sw", (17, 25), (17, 28), (20, 28))
        self.add_dot("finder-se", (30, 27))
