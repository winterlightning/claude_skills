"""Make the pearl truly circular and recenter its adjoining collar curves; the pendant no longer reads as a flattened bead.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1abfa79e-18a0-4f01-b0ce-90b012a88a6a'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-06/necklace with pearl_1abfa79e-18a0-4f01-b0ce-90b012a88a6a.svg'
AUTHOR = 'gpt-6'

class CollarNecklaceWithPearl(Solo48):
    icon_id = 'collar-necklace-with-pearl-centerline-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('collar', 'necklace', 'with', 'pearl')

    def build(self) -> None:
        p_6_22 = (6, 22)
        p_42_22 = (42, 22)
        p_30_37 = (30, 36)
        p_18_37 = (18, 36)
        self.add_arc('outer-top', p_6_22, p_42_22, radius_x=18, radius_y=16, sweep=True, large_arc=False)
        self.add_arc('outer-r', p_42_22, p_30_37, radius_x=12, radius_y=14, sweep=True, large_arc=False)
        self.add_arc('outer-l', p_18_37, p_6_22, radius_x=12, radius_y=14, sweep=True, large_arc=False)
        self.add_arc('inner', p_6_22, p_42_22, radius_x=18, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('pearl-top', p_18_37, p_30_37, radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('pearl-bottom', p_30_37, p_18_37, radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('collar', 'outer-l', 'outer-top', 'outer-r', closed=False)
        self.add_contour('pearl', 'pearl-top', 'pearl-bottom', closed=True)
        self.relate('connect', 'inner', 'collar')
        self.relate('connect', 'pearl', 'collar')
    variant_of = 'collar-necklace-with-pearl'
    variant_label = 'Batch 01 centerline repair'
