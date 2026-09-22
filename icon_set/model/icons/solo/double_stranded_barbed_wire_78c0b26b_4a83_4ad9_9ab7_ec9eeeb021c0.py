"""Two parallel strands with paired diagonal barbs. HRECT_L gives a wide fence fragment. The two rows share y-step 20; each barb derives from its wire attachment. Lucide fence supplied repeated horizontal rails; small wrapping marks omitted.
Source editorial brief is preserved in the gallery; source supplies identity and arrangement.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '78c0b26b-4a83-4ad9-9ab7-ec9eeeb021c0'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/barbed wire fence_78c0b26b-4a83-4ad9-9ab7-ec9eeeb021c0.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'double-stranded-barbed-wire'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ['Double Stranded Barbed Wire']
    keywords = ['barbed wire', 'strands', 'barbs', 'fence', 'wire', 'parallel', 'security']

    def build(self):
        for row,y in enumerate((14,34)):
            nodes=(4,18,30,44)
            for j in range(3):
                self.add_line(f"wire-{row}-{j}",(nodes[j],y),(nodes[j+1],y))
            for j,x in enumerate((18,30)):
                name=f"barb-{row}-{j}"
                self.add_polyline(name,(x-6,y-6),(x,y),(x+6,y+6))
                self.relate("connect",name,f"wire-{row}-{j}")
                self.relate("connect",name,f"wire-{row}-{j+1}")
            self.relate("connect",f"wire-{row}-0",f"wire-{row}-1")
            self.relate("connect",f"wire-{row}-1",f"wire-{row}-2")
