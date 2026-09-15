'Sitting rabbit: independent spacing revision.\n\nEight-unit ears and broader haunches; single nose replaces crowded eyes.\nNative solo family, VRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c76e3bee-26aa-4b66-9845-18e5b5d46930'
SOURCE_PATH = 'pictographic-primitives/animals/rabbit body_c76e3bee-26aa-4b66-9845-18e5b5d46930.svg'
AUTHOR = 'gpt-6'

class SittingRabbit(Solo48):
    icon_id = 'sitting-rabbit'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ('sitting-bunny',)
    keywords = ('rabbit', 'bunny', 'sitting', 'ears', 'hare', 'animal', 'pet', 'easter')

    def build(self):
        self.add_polyline('left-ear',(12, 24),(12, 8),closed=False)
        self.add_arc('left-tip',(12, 8),(20, 8),radius_x=4,radius_y=4,sweep=True)
        self.add_line('left-inner',(20, 8),(20, 21))
        self.contours = [c for c in self.contours if c.contour_id != 'left-ear']
        self.add_contour('ear-left','left-ear-1','left-tip','left-inner',closed=False)
        self.add_polyline('right-inner',(28, 21),(28, 8),closed=False)
        self.add_arc('right-tip',(28, 8),(36, 8),radius_x=4,radius_y=4,sweep=True)
        self.add_line('right-ear',(36, 8),(36, 24))
        self.contours = [c for c in self.contours if c.contour_id != 'right-inner']
        self.add_contour('ear-right','right-inner-1','right-tip','right-ear',closed=False)
        self.add_arc('crown-left',(12, 24),(24, 20),radius_x=12,radius_y=4,sweep=True)
        self.add_arc('crown-right',(24, 20),(36, 24),radius_x=12,radius_y=4,sweep=True)
        self.add_polyline('face-right',(36, 24),(38, 30),(32, 34),(40, 40),closed=False)
        self.add_arc('foot-right',(40, 40),(36, 44),radius_x=4,radius_y=4,sweep=True)
        self.add_line('bottom',(36, 44),(12, 44))
        self.add_arc('foot-left',(12, 44),(8, 40),radius_x=4,radius_y=4,sweep=True)
        self.add_polyline('face-left',(8, 40),(16, 34),(10, 30),(12, 24),closed=False)
        self.contours = [c for c in self.contours if c.contour_id != 'face-right']
        self.contours = [c for c in self.contours if c.contour_id != 'face-left']
        self.add_contour('body','crown-left','crown-right','face-right-1','face-right-2','face-right-3','foot-right','bottom','foot-left','face-left-1','face-left-2','face-left-3',closed=True)
        self.relate('connect','body','ear-left')
        self.relate('connect','body','ear-right')
        self.add_dot('nose',(24, 30))
