"""A server bust beside a stemmed wine glass. SQUARE balances the head and glass. Human reference user.svg supplies circular head and open shoulders; Lucide wine supplies bowl-stem-base construction. Head (16,12), r6; shoulder top26 gives exact 4 ink gap. Bow tie, liquid and clothing seam omitted to protect spacing.
Source editorial brief is preserved in the gallery; source supplies identity and arrangement.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = 'c4436bf3-759b-41d0-b845-5ca2470d9b2a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/bartender_c4436bf3-759b-41d0-b845-5ca2470d9b2a.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'bartender-holding-a-wine-glass'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ['Bartender holding a wine glass']
    keywords = ['server', 'bartender', 'bow tie', 'wine', 'glass', 'person', 'hospitality']

    def build(self):
        self.add_arc("head-top",(10,12),(22,12),radius_x=6)
        self.add_arc("head-bottom",(22,12),(10,12),radius_x=6)
        self.add_contour("head","head-top","head-bottom",closed=True)
        self.add_bezier("torso",(16,26),((6,26),(6,30),(6,42)))
        self.add_bezier("shoulder-right",(16,26),((26,26),(26,30),(26,42)))
        self.relate("connect","torso","shoulder-right")
        self.mark_human_figure("server",head="head",torso="torso",torso_junction="start")
        self.add_line("bowl-upper-1",(34,20),(34,10))
        self.add_line("bowl-upper-2",(34,10),(42,10))
        self.add_line("bowl-upper-3",(42,10),(42,20))
        self.add_arc("bowl-right",(42,20),(38,24),radius_x=4)
        self.add_arc("bowl-left",(38,24),(34,20),radius_x=4)
        self.add_contour("bowl","bowl-upper-1","bowl-upper-2","bowl-upper-3","bowl-right","bowl-left",closed=True)
        self.add_line("stem",(38,24),(38,42))
        self.add_polyline("base",(34,42),(38,42),(42,42))
        self.relate("connect","stem","bowl")
        self.relate("connect","stem","base")
