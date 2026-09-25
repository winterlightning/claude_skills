from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5914bd56-799d-4aed-872f-a8f85da47371'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/logos/stitcher logo_5914bd56-799d-4aed-872f-a8f85da47371.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/references/stitcher logo_5914bd56-799d-4aed-872f-a8f85da47371.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/06-audio-equalizer-sound-bars--5914bd56-799d-4aed-872f-a8f85da47371.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Five bars retained as single strokes: five outlined bars cannot fit with 8-unit gaps.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'audio-equalizer-sound-bars-batch-018-06'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    keywords = ('audio', 'equalizer', 'bars', 'sound', 'levels', 'waveform', 'music', 'stitcher')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_line('bar-0', (4, 18), (4, 32))
        self.add_line('bar-1', (14, 12), (14, 36))
        self.add_line('bar-2', (24, 10), (24, 40))
        self.add_line('bar-3', (34, 8), (34, 38))
        self.add_line('bar-4', (44, 16), (44, 34))
