'Mouse with long tail: independent spacing revision.\n\nA single broad tail loop replaces the two-unit return; body/tail gap enlarged.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5de17e52-807d-512f-bec7-d16365517673'
SOURCE_PATH = 'pictographic-primitives/animals/mouse tail_5de17e52-807d-512f-bec7-d16365517673.svg'
AUTHOR = 'gpt-6'

class MouseWithLongTail(Solo48):
    icon_id = 'mouse-with-long-tail'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('mouse', 'with', 'long', 'tail')

    def build(self):
        self.add_arc('back',(24, 14),(14, 24),radius_x=10,radius_y=10,sweep=False)
        self.add_arc('rump',(14, 24),(22, 32),radius_x=8,radius_y=8,sweep=False)
        self.add_polyline('underside',(22, 32),(30, 32),(34, 22),(42, 16),(36, 12),closed=False)
        self.add_arc('ear',(36, 12),(24, 12),radius_x=6,radius_y=6,sweep=False)
        self.add_line('neck',(24, 12),(24, 14))
        self.contours = [c for c in self.contours if c.contour_id != 'underside']
        self.add_contour('mouse','back','rump','underside-1','underside-2','underside-3','underside-4','ear','neck',closed=True)
        self.add_arc('tail-turn',(14, 24),(14, 42),radius_x=8,radius_y=9,sweep=False)
        self.add_line('tail-end',(14, 42),(30, 42))
        self.add_contour('tail','tail-turn','tail-end',closed=False)
        self.relate('connect','mouse','tail')
