"""A fuel filler neck with its detached angled T cap. Square envelope keeps the cap separated from the neck. No exact useful Lucide match; fuel was inspected for spare construction. Panel lines, lower opening and removable cap retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2dfe1f6-1d73-4927-b7fd-6ddce6acddf8'
SOURCE_PATH = 'pictographic-primitives/transportation/check fuel cap_c2dfe1f6-1d73-4927-b7fd-6ddce6acddf8.svg'
SOURCE_REFERENCES = (('c2dfe1f6-1d73-4927-b7fd-6ddce6acddf8', 'pictographic-primitives/transportation/check fuel cap_c2dfe1f6-1d73-4927-b7fd-6ddce6acddf8.svg'),)
AUTHOR = 'gpt-6'

class FuelFillerRemovedCap(Solo48):
    icon_id = 'fuel-filler-removed-cap'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('fuel cap', 'filler', 'petrol', 'gas', 'car', 'dashboard', 'warning', 'refuel')

    def build(self) -> None:
        self.add_line('neck-a',(6,6),(16,6))
        self.add_line('neck-b',(16,6),(22,20))
        self.add_line('neck-c',(22,20),(24,24))
        self.add_arc('neck-d',(24,24),(24,34),radius_x=5)
        self.add_line('neck-e',(24,34),(22,34))
        self.add_line('neck-f',(22,34),(14,34))
        self.add_line('neck-g',(14,34),(6,34))
        self.add_contour('neck','neck-a','neck-b','neck-c','neck-d','neck-e','neck-f','neck-g')
        self.add_line('panel',(6,20),(22,20))
        self.relate('connect','panel','neck')
        self.add_line('opening-a',(14,34),(14,38))
        self.add_arc('opening-b',(14,38),(22,38),radius_x=4,sweep=False)
        self.add_line('opening-c',(22,38),(22,34))
        self.add_contour('opening','opening-a','opening-b','opening-c')
        self.relate('connect','opening','neck')
        self.add_polyline('cap',(34,6),(38,10),(42,14))
        self.add_line('cap-stem',(38,10),(32,16))
        self.relate('connect','cap-stem','cap')
