"""Three berries cluster beneath a stem and single leaf. SQUARE 6..42 holds symmetric berry lobes and asymmetric leaf. Source supplies three berries and overlap; Lucide cherry supplies connected fruit lobes. Shared front-berry rim nodes, repeated mirrored rear berries; omit berry texture."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'caa9f497-47bb-4168-ab8e-e78de139cf75'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_13/cranberry_caa9f497-47bb-4168-ab8e-e78de139cf75.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'three-round-berries-on-stem'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ('Berries with Stem and Leaf',)
    keywords = ('berry', 'fruit', 'stem', 'leaf', 'cluster', 'plant', 'food')
    def build(self):
        def mirror(p): return (48-p[0],p[1])
        left = [(18,36),(11,38),(6,35),(6,30),(6,26),(10,24),(15,24),(19,24),(22,26),(24,30)]
        for name,points in (("left-berry",left),("right-berry",[mirror(p) for p in reversed(left)])):
            self.add_bezier(name,points[0],*(tuple(points[j:j+3]) for j in range(1,len(points),3)))
        self.add_arc("front-lower",(30,36),(18,36),radius_x=6)
        self.add_contour("cluster","left-berry","right-berry","front-lower",closed=True)
        self.add_arc("front-upper",(18,36),(30,36),radius_x=6)
        self.relate("connect","cluster","front-upper")
        self.add_line("stem-lower",(24,30),(24,16))
        self.add_bezier("stem-upper",(24,16),((25,11),(28,7),(31,6)))
        self.add_contour("stem","stem-lower","stem-upper")
        self.relate("connect","cluster","stem")
        self.relate("connect","stem","leaf")
        self.add_bezier("leaf",(24,16),((16,16),(10,14),(10,6)),((20,6),(24,8),(24,16)))
