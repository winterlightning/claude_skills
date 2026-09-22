"""Two matched toothed gears mesh diagonally. SQUARE bounds 6..42. A half-turn generates the matching gear silhouette; the mesh is one continuous outer contour. Source supplies diagonal gear pair and Lucide cog supplies radial repetition. Fine teeth omitted and hub openings reduced to dots for certified clearance."""
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
        # Each gear owns the same tooth pattern. The facing quadrant is
        # replaced by the visible shared meshing silhouette.
        half = [(12,22),(20,22),(22,20),(22,12),(25,12),(25,9),(28,9),(28,6),(36,6),(36,9),(39,9),(39,12),(42,12),(42,20),(39,20),(39,23),(36,23)]
        left = half + [(48-x,48-y) for x,y in half]
        self.add_polyline("meshing-outline",*left,closed=True)
        for x,y in ((16,32),(32,16)):
            self.add_dot(f"hub-{x}",(x,y))
