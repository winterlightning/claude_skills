from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b129829-6342-40c9-9b99-99ad94ea619d'
SOURCE_PATH = 'pictographic-primitives/shipping/warehouse package_6b129829-6342-40c9-9b99-99ad94ea619d.svg'
AUTHOR = 'gpt-6-astra'


class WarehouseDistributionDiagram(Solo48):
    icon_id = 'warehouse-distribution-diagram'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/shipping"
    aliases = ()
    keywords = ('warehouse', 'distribution', 'parcel', 'network', 'shipping', 'logistics')

    def build(self) -> None:
        # Square centerlines (6,6)-(42,42); domed depot above two branch endpoints.
        self.add_arc("roof", (8,22), (40,22), radius_x=16)
        self.add_polyline("walls-door", (40,22), (32,22), (32,18), (24,18), (16,18), (16,22), (8,22))
        self.relate("connect", "roof", "walls-door")
        self.add_polyline("branch", (13,34), (24,28), (35,34))
        self.add_line("trunk", (24,18), (24,28))
        self.relate("connect", "branch", "trunk")
        for n,x in enumerate((6,28)):
            self.add_polyline(f"parcel-{n}", (x,34), (x+7,34), (x+14,34), (x+14,42), (x,42), (x,34))
            self.relate("connect", "branch", f"parcel-{n}")
        self.relate("connect", "walls-door", "trunk")
