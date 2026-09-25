"""Four equal arrows converge on an open center. SQUARE visible bounds (4,4)-(44,44) fit the four equal cardinal arrows. Lucide arrow-down informs the shaft and open head; a shared quarter-turn pattern preserves equal spacing. No arrows omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b70ed0a4-9193-4eb1-aa64-53f88bcf4fe3'
SOURCE_PATH = 'pictographic-primitives/symbol/four arrows pointing_b70ed0a4-9193-4eb1-aa64-53f88bcf4fe3.svg'
AUTHOR = 'gpt-6'


class ArrowsInwardFour(Solo48):
    icon_id = 'arrows-inward-four'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('arrows', 'inward', 'collapse', 'center', 'converge', 'compress', 'focus', 'minimize')

    def build(self) -> None:
        # Rotate one inward arrow around the shared center.
        def rotate(p, turns):
            x,y=p
            for _ in range(turns):
                x,y=48-y,x
            return x,y
        for i in range(4):
            self.add_line(f'shaft-{i}', rotate((24,6),i), rotate((24,16),i))
            self.add_polyline(f'head-{i}', *(rotate(p,i) for p in [(18,10),(24,16),(30,10)]))
            self.relate('connect', f'shaft-{i}', f'head-{i}')
