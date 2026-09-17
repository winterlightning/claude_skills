from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e5e7f969-d092-4932-8d8d-f11924b8f98d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/logos/tiktok logo 1_e5e7f969-d092-4932-8d8d-f11924b8f98d.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/references/tiktok logo 1_e5e7f969-d092-4932-8d8d-f11924b8f98d.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/08-tiktok-social-media-logo--e5e7f969-d092-4932-8d8d-f11924b8f98d.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Outlined note keeps right-sweeping flag; color offset omitted.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'tiktok-musical-note-logo-batch-018-08'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('tiktok', 'logo', 'note', 'music', 'social', 'media', 'stem', 'flag')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('stem', (30, 33), (30, 4), (38, 4), (38, 12), (40, 16), (40, 24), (30, 20), closed=False)
        self.add_arc('bowl-bottom', (30, 33), (8, 33), radius_x=11, radius_y=11, sweep=True, large_arc=False)
        self.add_arc('bowl-upper', (8, 33), (19, 22), radius_x=11, radius_y=11, sweep=True, large_arc=False)
        self.add_line('bowl-tip', (19, 22), (19, 31))
        self.relate("connect", 'stem', 'bowl-bottom')
        self.relate("connect", 'bowl-bottom', 'bowl-upper')
        self.relate("connect", 'bowl-upper', 'bowl-tip')
