"""Five circular beads on a sagging string. HRECT_M fits a wide U shape, deepened for spacing. Beads share radius3 and mirror across x24; straight links meet cardinal bead nodes. No useful Lucide necklace match; reference supplies bead count and arrangement.
Source editorial brief is preserved in the gallery; source supplies identity and arrangement.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = 'ed4699f6-a912-4876-9b67-eba4703923e0'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/bead_ed4699f6-a912-4876-9b67-eba4703923e0.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'curved-string-of-beads'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ['Curved String of Beads']
    keywords = ['beads', 'string', 'necklace', 'circles', 'chain', 'jewelry', 'curve']

    def build(self):
        beads=((7,13),(11,29),(24,35),(37,29),(41,13))
        for j,(x,y) in enumerate(beads):
            points=((x+3,y),(x,y+3),(x-3,y),(x,y-3),(x+3,y))
            members=[]
            for k in range(4):
                name=f"bead-{j}-{k}"
                self.add_arc(name,points[k],points[k+1],radius_x=3)
                members.append(name)
            self.add_contour(f"bead-{j}",*members,closed=True)
        links=(((7,16),(11,26)),((14,29),(21,35)),((27,35),(34,29)),((37,26),(41,16)))
        for j,(a,b) in enumerate(links):
            self.add_line(f"string-{j}",a,b)
            self.relate("connect",f"string-{j}",f"bead-{j}")
            self.relate("connect",f"string-{j}",f"bead-{j+1}")
