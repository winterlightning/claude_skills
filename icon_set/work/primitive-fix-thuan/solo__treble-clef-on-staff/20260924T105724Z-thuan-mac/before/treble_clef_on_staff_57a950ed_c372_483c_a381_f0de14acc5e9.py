"""Treble clef with a tall loop, central bowl and hooked tail. Short staff fragments repeat every 8 units on both sides. Centerline extremes (4,8)-(44,40). Deliberate clef asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='57a950ed-c372-483c-a381-f0de14acc5e9'
SOURCE_PATH='pictographic-primitives/music/music clef sheet_57a950ed-c372-483c-a381-f0de14acc5e9.svg'
AUTHOR='gpt-6'

class TrebleClefOnStaff(Solo48):
    icon_id='treble-clef-on-staff'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/music"
    aliases=()
    keywords=('treble-clef', 'clef', 'staff', 'sheet-music', 'notation', 'score', 'music')

    def build(self):
        self.add_polyline('stem',(24,8),(24,20),(24,30),(24,36))
        self.add_arc('tail',(24,36),(20,40),radius_x=4)
        self.relate('connect','stem','tail')
        self.add_bezier('clef-loop',(24,8),((34,8),(34,14),(24,20)),((14,26),(14,30),(24,30)),((34,30),(34,20),(24,20)))
        self.relate('connect','clef-loop','stem')
        for n,y in enumerate((12,20,28,36)):
            self.add_line(f'staff-left-{n}',(4,y),(7,y))
            self.add_line(f'staff-right-{n}',(41,y),(44,y))
