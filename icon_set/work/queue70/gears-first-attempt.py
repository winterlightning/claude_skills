"""Two matched toothed gears meet diagonally. SQUARE bounds 6..42. Repeated tooth definition and circular hubs; source supplies diagonal pair, Lucide cog supplies radial repetition. Fine teeth omitted."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'b484255b-2a40-40d1-9943-7e27cfb9f399'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_12/cog double_b484255b-2a40-40d1-9943-7e27cfb9f399.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'diagonal-pair-of-meshing-gears'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Double Interlocking Gears',)
    keywords = ('gears', 'cogs', 'meshing', 'machine', 'teeth', 'mechanical', 'pair')
    def build(self):
        for n,(x,y) in enumerate(((16,32),(32,16))):
            points=[(-4,-10),(4,-10),(4,-7),(7,-7),(7,-4),(10,-4),(10,4),(7,4),(7,7),(4,7),(4,10),(-4,10),(-4,7),(-7,7),(-7,4),(-10,4),(-10,-4),(-7,-4),(-7,-7),(-4,-7)]
            self.add_polyline(f"gear-{n}",*((x+a,y+b) for a,b in points),closed=True)
            self.add_arc(f"hub-{n}-a",(x-2,y),(x+2,y),radius_x=2)
            self.add_arc(f"hub-{n}-b",(x+2,y),(x-2,y),radius_x=2)
            self.add_contour(f"hub-{n}",f"hub-{n}-a",f"hub-{n}-b",closed=True)
