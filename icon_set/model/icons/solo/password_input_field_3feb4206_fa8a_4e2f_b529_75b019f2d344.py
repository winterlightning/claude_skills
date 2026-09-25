"""A rounded password field containing three masked characters."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "3feb4206-fa8a-4e2f-b529-75b019f2d344"
SOURCE_PATH = "pictographic-primitives/other/rectangle password_3feb4206-fa8a-4e2f-b529-75b019f2d344.svg"
AUTHOR = "gpt-6"


class PasswordInputField(Solo48):
    icon_id = "password-input-field"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("password box", "masked text field")
    keywords = ("password", "authentication", "dots", "entry")

    def build(self) -> None:
        # Rounded horizontal field, mirrored across both axes.
        radius = 4
        self.add_line("field-top", (8, 10), (40, 10))
        self.add_arc("field-ne", (40, 10), (44, 14), radius_x=radius)
        self.add_line("field-right", (44, 14), (44, 34))
        self.add_arc("field-se", (44, 34), (40, 38), radius_x=radius)
        self.add_line("field-bottom", (40, 38), (8, 38))
        self.add_arc("field-sw", (8, 38), (4, 34), radius_x=radius)
        self.add_line("field-left", (4, 34), (4, 14))
        self.add_arc("field-nw", (4, 14), (8, 10), radius_x=radius)
        self.add_contour("field", "field-top", "field-ne", "field-right",
                         "field-se", "field-bottom", "field-sw", "field-left",
                         "field-nw", closed=True)

        # The outlined source circles reduce to Lucide-like masked dots at 48.
        for index, x in enumerate((13, 24, 35), start=1):
            self.add_dot(f"password-dot-{index}", (x, 24))
