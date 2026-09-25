"""A cloud above two side-by-side database cylinders.

Plan: one asymmetric two-lobe cloud outline owns a repeated cylinder pair.
Cylinder width, cap radii and base height are shared. Lucide cloud informed
the lobe silhouette; Lucide database informed the oval cap and round base.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "b5835419-04ce-4820-b84f-80a2863f52ba"
SOURCE_PATH = "pictographic-primitives/_uncategorized_26/machine learning infrastructure_b5835419-04ce-4820-b84f-80a2863f52ba.svg"
AUTHOR = "gpt-6"


class CloudDatabaseStorage(Solo48):
    icon_id = "cloud-database-storage"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("cloud-storage-databases",)
    keywords = ("cloud", "database", "storage", "server")

    def build(self) -> None:
        self.add_line("cloud-left", (6, 18), (8, 16))
        self.add_arc("cloud-large-lobe", (8, 16), (28, 16), radius_x=10, radius_y=10, sweep=True)
        self.add_arc("cloud-small-lobe", (28, 16), (40, 16), radius_x=6, radius_y=6, sweep=True)
        self.add_line("cloud-right", (40, 16), (42, 18))
        self.add_contour("cloud", "cloud-left", "cloud-large-lobe", "cloud-small-lobe", "cloud-right")

        for index, cx in enumerate((14, 34)):
            left, right = cx - 6, cx + 6
            self.add_arc(f"cap-top-{index}", (left, 29), (right, 29), radius_x=6, radius_y=3, sweep=True)
            self.add_arc(f"cap-bottom-{index}", (right, 29), (left, 29), radius_x=6, radius_y=3, sweep=True)
            self.add_contour(f"cap-{index}", f"cap-top-{index}", f"cap-bottom-{index}", closed=True)
            self.add_line(f"wall-left-{index}", (left, 29), (left, 39))
            self.add_arc(f"base-{index}", (left, 39), (right, 39), radius_x=6, radius_y=3, sweep=False)
            self.add_line(f"wall-right-{index}", (right, 39), (right, 29))
            self.add_contour(f"body-{index}", f"wall-left-{index}", f"base-{index}", f"wall-right-{index}")
            self.relate("connect", f"cap-{index}", f"body-{index}")
