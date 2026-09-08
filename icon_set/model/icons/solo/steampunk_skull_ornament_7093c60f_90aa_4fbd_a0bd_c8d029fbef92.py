"""Skull ornament with circular sockets and projecting forehead band. SQUARE (2,2)-(46,46). Lucide skull informs round cranium and compact jaw. Radial eye ticks omitted and scalloped teeth reduced to two divisions; left band preserves mechanical asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7093c60f-90aa-4fbd-a0bd-c8d029fbef92'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/steampunk decoration dia de los muertos_7093c60f-90aa-4fbd-a0bd-c8d029fbef92.svg'
AUTHOR = 'gpt-6'


class SteampunkSkullOrnament(Solo48):
    icon_id = 'steampunk-skull-ornament'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('skull', 'steampunk', 'ornament', 'teeth', 'eyes', 'dia de los muertos', 'decor')

    def build(self) -> None:
        self.add_line('top', (18, 2), (34, 2))
        self.add_arc('tr', (34, 2), (46, 14), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_line('r', (46, 14), (46, 29))
        self.add_arc('cheek-r', (46, 29), (38, 37), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_line('jaw-1', (38, 37), (38, 46))
        self.add_line('jaw-2', (38, 46), (16, 46))
        self.add_line('jaw-3', (16, 46), (16, 37))
        self.add_arc('cheek-l', (16, 37), (8, 29), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_line('l', (8, 29), (8, 12))
        self.add_arc('tl', (8, 12), (18, 2), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_contour('outline', 'top', 'tr', 'r', 'cheek-r', 'jaw-1', 'jaw-2', 'jaw-3', 'cheek-l', 'l', 'tl', closed=True)
        self.add_polyline('band', (2, 8), (2, 14), (46, 14), closed=False)
        self.relate('connect', 'band', 'outline')
        self.add_arc('eye-left-a', (15, 25), (21, 25), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('eye-left-b', (21, 25), (15, 25), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('eye-left', 'eye-left-a', 'eye-left-b', closed=True)
        self.add_arc('eye-right-a', (33, 25), (39, 25), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('eye-right-b', (39, 25), (33, 25), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('eye-right', 'eye-right-a', 'eye-right-b', closed=True)
        self.add_polyline('nose', (24, 36), (27, 32), (30, 36), closed=False)
        self.add_line('tooth-left', (23, 42), (23, 46))
        self.add_line('tooth-right', (31, 42), (31, 46))
        self.relate('connect', 'tooth-left', 'outline')
        self.relate('connect', 'tooth-right', 'outline')
