'Three interwoven peaks in one continuous contour. HRECT_L fits the broad mark. Source supplies three interwoven peaks; central peak raised to open the crossing slopes and crossing; Lucide mountain supplies continuous angular silhouette. Shared extremal grid, rounded stroke joins; outer end loops use shared radius5 semicircles; small dangling entry stroke omitted.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f1e06b31-550b-4e11-afb7-adf754dc4bdb'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/amazon macie_f1e06b31-550b-4e11-afb7-adf754dc4bdb.svg'
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = 'interwoven-triple-mountain-mark'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ['Triple Peak Geometric Mountain']
    keywords = ['mountains', 'peaks', 'zigzag', 'geometric', 'mark', 'overlap', 'abstract']
    def build(self):
        points=[(4,35),(10,20),(24,36),(38,20),(44,35)]
        for j in range(4): self.add_line(f'peaks-{j+1}',points[j],points[j+1])
        self.add_arc('right-turn',(44,35),(34,35),radius_x=5)
        self.add_line('middle-peak-1',(34,35),(24,8))
        self.add_line('middle-peak-2',(24,8),(14,35))
        self.add_arc('left-turn',(14,35),(4,35),radius_x=5)
        self.add_contour('mark', 'peaks-1','peaks-2','peaks-3','peaks-4','right-turn','middle-peak-1','middle-peak-2','left-turn',closed=True)
