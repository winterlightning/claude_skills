from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ebcea186-c719-4114-bdb5-259abc380960'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/net rope_ebcea186-c719-4114-bdb5-259abc380960.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/references/net rope_ebcea186-c719-4114-bdb5-259abc380960.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/03-volleyball-court-net--ebcea186-c719-4114-bdb5-259abc380960.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Net reduced to a regular four-column, two-row mesh; slight sag omitted.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'volleyball-net-batch-018-03'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "kids"
    categories = ("primitives", "kids")
    keywords = ('net', 'volleyball', 'sport', 'mesh', 'rope', 'posts', 'court', 'game')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('vertical-4', (4, 8), (4, 18), (4, 28), (4, 40), closed=False)
        self.add_polyline('vertical-14', (14, 8), (14, 18), (14, 28), (14, 28), closed=False)
        self.add_polyline('vertical-24', (24, 8), (24, 18), (24, 28), (24, 28), closed=False)
        self.add_polyline('vertical-34', (34, 8), (34, 18), (34, 28), (34, 28), closed=False)
        self.add_polyline('vertical-44', (44, 8), (44, 18), (44, 28), (44, 40), closed=False)
        self.add_polyline('net-8', (4, 8), (14, 8), (24, 8), (34, 8), (44, 8), closed=False)
        self.add_polyline('net-18', (4, 18), (14, 18), (24, 18), (34, 18), (44, 18), closed=False)
        self.add_polyline('net-28', (4, 28), (14, 28), (24, 28), (34, 28), (44, 28), closed=False)
        self.relate("connect", 'vertical-4', 'net-8')
        self.relate("connect", 'vertical-4', 'net-18')
        self.relate("connect", 'vertical-4', 'net-28')
        self.relate("connect", 'vertical-14', 'net-8')
        self.relate("connect", 'vertical-14', 'net-18')
        self.relate("connect", 'vertical-14', 'net-28')
        self.relate("connect", 'vertical-24', 'net-8')
        self.relate("connect", 'vertical-24', 'net-18')
        self.relate("connect", 'vertical-24', 'net-28')
        self.relate("connect", 'vertical-34', 'net-8')
        self.relate("connect", 'vertical-34', 'net-18')
        self.relate("connect", 'vertical-34', 'net-28')
        self.relate("connect", 'vertical-44', 'net-8')
        self.relate("connect", 'vertical-44', 'net-18')
        self.relate("connect", 'vertical-44', 'net-28')
