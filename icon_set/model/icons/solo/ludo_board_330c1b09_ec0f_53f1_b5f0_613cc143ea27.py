"""Ludo Board.

Plan: Intrinsic Ludo playing field, paired crossing tracks and central circle. Board is the subject, not a generic hosting frame. Remove counters. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '330c1b09-ec0f-53f1-b5f0-613cc143ea27'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/board game ludo_330c1b09-ec0f-53f1-b5f0-613cc143ea27.svg'
AUTHOR = 'gpt-6'

class LudoBoard(Solo48):
    icon_id = 'ludo-board'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hobbies"
    aliases = ()
    keywords = ('ludo', 'board')

    def build(self):
        self.add_polyline('board',(6,6),(18,6),(30,6),(42,6),(42,18),(42,30),(42,42),(30,42),(18,42),(6,42),(6,30),(6,18),closed=True)
        pts=[(18,16),(30,16),(32,18),(32,30),(30,32),(18,32),(16,30),(16,18),(18,16)]
        for i in range(8):self.add_arc(f'hub-{i}',pts[i],pts[i+1],radius_x=10)
        self.add_contour('hub',*[f'hub-{i}' for i in range(8)],closed=True)
        for name,a,b in [('tl',(18,6),(18,16)),('tr',(30,6),(30,16)),('bl',(18,32),(18,42)),('br',(30,32),(30,42)),('lt',(6,18),(16,18)),('lb',(6,30),(16,30)),('rt',(32,18),(42,18)),('rb',(32,30),(42,30))]:
         self.add_line(name,a,b);self.relate('connect','board',name);self.relate('connect','hub',name)
