"""LEO rotational interlock with opposing outer arcs and three bent inner arms. Radius20 at24. Reduce doubled hook returns to open bent strokes. No useful exact Lucide match; circle construction uses cardinal arc endpoints."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='9d537bb3-e057-462e-a9b5-a4b2ec7bf39b'
SOURCE_PATH='pictographic-primitives/money/virtual coin crypto unus sed leo_9d537bb3-e057-462e-a9b5-a4b2ec7bf39b.svg'
AUTHOR='gpt-6'

class UnusSedLeoEmblem(Solo48):
    icon_id='unus-sed-leo-emblem'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="symbols/finance"
    aliases=()
    keywords=('unus sed leo', 'leo', 'crypto', 'emblem', 'swirl', 'interlock')

    def build(self):
        self.add_arc('upper-a',(8,12),(24,4),radius_x=20)
        self.add_arc('upper-b',(24,4),(44,24),radius_x=20)
        self.add_arc('lower-a',(40,36),(24,44),radius_x=20)
        self.add_arc('lower-b',(24,44),(4,24),radius_x=20)
        self.add_contour('upper','upper-a','upper-b')
        self.add_contour('lower','lower-a','lower-b')
        self.add_polyline('hook-top',(22,13),(30,18),(30,22))
        self.add_polyline('hook-right',(32,31),(24,35),(21,33))
        self.add_polyline('hook-left',(14,29),(14,22),(16,20))
