from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9d7e3a6-e7cd-53ad-8f0d-95595a117f13'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/toys fidget spinner_c9d7e3a6-e7cd-53ad-8f0d-95595a117f13.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/references/toys fidget spinner_c9d7e3a6-e7cd-53ad-8f0d-95595a117f13.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/10-three-armed-fidget-spinner-toy--c9d7e3a6-e7cd-53ad-8f0d-95595a117f13.md'
DESIGN_PLAN = 'Top lobe and paired lower lobes enclose a central bearing; reflected side contours.'
DESIGN_NOTES = ['Three peripheral bearings omitted; three lobes and center bearing retained.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'three-armed-fidget-spinner-batch-017-10'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('spinner', 'fidget', 'toy', 'bearing', 'three', 'rotating', 'lobes', 'play')

    def build(self):
        # Top lobe and paired lower lobes enclose a central bearing; reflected side contours.
        self.add_arc('top', (16, 12), (32, 12), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('lower-right', (40, 36), (24, 36), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('lower-left', (24, 36), (8, 36), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_line('right-side-part-0', (32, 12), (32, 18))
        self.add_line('right-side-part-1', (32, 18), (40, 26))
        self.add_line('right-side-part-2', (40, 26), (40, 36))
        self.add_line('left-side-part-0', (8, 36), (8, 26))
        self.add_line('left-side-part-1', (8, 26), (16, 18))
        self.add_line('left-side-part-2', (16, 18), (16, 12))
        self.add_contour('spinner', 'top', 'right-side-part-0', 'right-side-part-1', 'right-side-part-2', 'lower-right', 'lower-left', 'left-side-part-0', 'left-side-part-1', 'left-side-part-2', closed=True)
        self.add_arc('bearing-0', (22, 25), (24, 23), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('bearing-1', (24, 23), (26, 25), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('bearing-2', (26, 25), (24, 27), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('bearing-3', (24, 27), (22, 25), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_contour('bearing', 'bearing-0', 'bearing-1', 'bearing-2', 'bearing-3', closed=True)
