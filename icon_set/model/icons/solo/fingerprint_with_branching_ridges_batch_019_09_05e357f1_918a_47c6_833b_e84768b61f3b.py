from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '05e357f1-918a-47c6-833b-e84768b61f3b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/fingerprint_05e357f1-918a-47c6-833b-e84768b61f3b.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/references/fingerprint_05e357f1-918a-47c6-833b-e84768b61f3b.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/09-biometric-fingerprint-identity-scanner--05e357f1-918a-47c6-833b-e84768b61f3b.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Fingerprint reduced to three widely separated nested ridge runs.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'fingerprint-with-branching-ridges-batch-019-09'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('fingerprint', 'biometric', 'scan', 'finger', 'identity', 'ridges', 'security', 'touch')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('outer', (8, 24), (40, 24), radius_x=16, radius_y=20, sweep=True, large_arc=False)
        self.add_arc('inner', (17, 24), (31, 24), radius_x=7, radius_y=10, sweep=True, large_arc=False)
        self.add_polyline('left-ridge', (17, 24), (17, 34), (10, 40), closed=False)
        self.add_polyline('right-ridge', (31, 24), (31, 34), (38, 40), closed=False)
        self.add_line('center-ridge', (24, 42), (24, 44))
        self.relate("connect", 'inner', 'left-ridge')
        self.relate("connect", 'inner', 'right-ridge')
