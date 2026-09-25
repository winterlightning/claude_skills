"""laptop small squares: fresh SOLO48 repair.
Plan: Shared screen hinges and base; two identical small solid rounded squares.
Keyshape: SQUARE. The taller screen holds two vertically stacked solid marks.
Omissions: Outlined boxes replaced by solid marks with explicit user approval.
Construction reference: No useful additional Lucide match inspected; supplied laptop reference governs construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '71714a04-dd1b-4fab-90a6-dbd391dacaf5'
SOURCE_PATH = 'pictographic-primitives/other/laptop small squares_71714a04-dd1b-4fab-90a6-dbd391dacaf5.svg'
AUTHOR = 'gpt-6'
PARENT_SOURCE = 'icon_set/model/icons/solo/laptop_small_squares_71714a04_dd1b_4fab_90a6_dbd391dacaf5.py'

class Drawing(Solo48):
    icon_id = 'laptop-small-squares'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('laptop small squares',)

    def laptop(self):
        self.add_line('screen-left', (10, 34), (10, 10))
        self.add_arc('screen-tl', (10, 10), (14, 6), radius_x=4)
        self.add_line('screen-top', (14, 6), (34, 6))
        self.add_arc('screen-tr', (34, 6), (38, 10), radius_x=4)
        self.add_line('screen-right', (38, 10), (38, 34))
        self.add_line('hinge', (38, 34), (10, 34))
        self.add_contour('screen', 'screen-left', 'screen-tl', 'screen-top', 'screen-tr', 'screen-right', 'hinge', closed=True)
        self.add_polyline('base', (10, 34), (6, 42), (42, 42), (38, 34))
        self.relate('connect', 'screen', 'base')

    def build(self):
        self.laptop()
        tile = 1
        for i, y in enumerate((15, 24)):
            self.add_polyline('tile-' + str(i), (19, y), (19 + tile, y), (19 + tile, y + tile), (19, y + tile), closed=True)

# Explicit user approval bound to this drawing; raw checks remain available.
VISUAL_EXCEPTION = {'reason': 'User explicitly requested two small solid square marks, like the music note dots, and approved an exception. The filled-over centers and their within-mark spacing are intentional; distinct marks and screen remain separated.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': '78ba8b13ddd86f1bfd111c6dfa8b5a1ef9c2e75f871eae2fadf494313634ebd0', 'scope': ['tile-0', 'tile-1'], 'user_request': 'fix laptop please, you can make a square like circle in music (small solid) like that then put exception', 'application': 'Local drawing-specific visual exception. The built-in publication exception handler currently supports SUB32 only, so this SOLO48 approval is preserved as metadata without claiming an automatic pass.'}

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': '78ba8b13ddd86f1bfd111c6dfa8b5a1ef9c2e75f871eae2fadf494313634ebd0', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': '71714a04-dd1b-4fab-90a6-dbd391dacaf5'}
