"""Chisel with Wood Shaving.

Plan: Diagonal capsule grip, narrow shaft and flared blade beside a curled shaving. Pythagorean cap nodes retain tangent joins. Bounds (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0541fbf8-91e3-430d-b90b-d3ebc73efb34'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/crafts carving_0541fbf8-91e3-430d-b90b-d3ebc73efb34.svg'
AUTHOR = 'gpt-6'


class ChiselWithWoodShaving(Solo48):
    icon_id = 'chisel-with-wood-shaving'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hobbies'
    aliases = ()
    keywords = ('chisel', 'with', 'wood', 'shaving')

    def build(self):
        self.add_arc('handle-top',(31,6),(39,12),radius_x=5)
        self.add_line('handle-r',(39,12),(36,16))
        self.add_arc('handle-bottom-r',(36,16),(29,17),radius_x=5)
        self.add_arc('handle-bottom-l',(29,17),(28,10),radius_x=5)
        self.add_line('handle-l',(28,10),(31,6))
        self.add_contour('handle','handle-top','handle-r','handle-bottom-r','handle-bottom-l','handle-l',closed=True)

        self.add_line('shaft',(29,17),(25,30))
        self.add_polyline('blade',(22,28),(25,30),(28,32),(20,44),(12,40),closed=True)
        self.relate('connect','handle','shaft')
        self.relate('connect','shaft','blade')
        self.add_arc('shaving-outer',(16,22),(16,6),radius_x=8)
        self.add_arc('shaving-turn',(16,6),(20,10),radius_x=4)
        self.add_arc('shaving-tip',(20,10),(16,14),radius_x=4)
        self.add_contour('shaving','shaving-outer','shaving-turn','shaving-tip')
