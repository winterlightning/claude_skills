'A winding snake with a rounded head end and tapered tail.\nPlan: VRECT_L provides height for two broad turns with legal body width.\nReduction: Simplified the diagonal winding body to a continuous S ribbon and fewer turns; retained a tapered tail and rounded head end.\nConstruction: No useful exact Lucide match; supplied reference governs the winding body and taper.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22672d31-d164-4dfa-a6e8-c5a29193cea8'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/anaconda_22672d31-d164-4dfa-a6e8-c5a29193cea8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 's-curved-snake'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('snake', 'serpent', 'reptile', 'anaconda', 'curve', 'tail', 'wildlife')

    def build(self):
        # Plan: one continuous rounded S ribbon. Shared turn centers/radii keep
        # the body eight units wide; VRECT_L extremes (8,4)-(40,44).
        self.add_arc('head-cap',(36,4),(36,12),radius_x=4)
        self.add_line('upper-inner',(36,12),(20,12))
        self.add_arc('upper-inner-turn',(20,12),(20,20),radius_x=4,sweep=False)
        self.add_line('middle-upper',(20,20),(28,20))
        self.add_arc('lower-outer-turn',(28,20),(28,44),radius_x=12)
        self.add_line('tail-lower',(28,44),(8,44))
        self.add_line('tail-cap',(8,44),(12,36))
        self.add_line('tail-upper',(12,36),(28,36))
        self.add_arc('lower-inner-turn',(28,36),(28,28),radius_x=4,sweep=False)
        self.add_line('middle-lower',(28,28),(20,28))
        self.add_arc('upper-outer-turn',(20,28),(20,4),radius_x=12)
        self.add_line('head-upper',(20,4),(36,4))
        self.add_contour('snake','head-cap','upper-inner','upper-inner-turn','middle-upper',
            'lower-outer-turn','tail-lower','tail-cap','tail-upper','lower-inner-turn',
            'middle-lower','upper-outer-turn','head-upper',closed=True)
