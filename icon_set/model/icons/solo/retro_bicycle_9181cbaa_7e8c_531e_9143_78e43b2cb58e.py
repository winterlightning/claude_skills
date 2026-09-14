'Retro bicycle: independent spacing revision.\n\nOpen triangular frame replaces narrow diamond subdivisions; retain paired wheels, saddle and hooked bar.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: bike: round wheels and economical frame strokes. Local Lucide originals and atomic-debug renders were inspected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9181cbaa-7e8c-531e-9143-78e43b2cb58e'
SOURCE_PATH = 'pictographic-primitives/transportation/bicycle retro_9181cbaa-7e8c-531e-9143-78e43b2cb58e.svg'
AUTHOR = 'gpt-6'

class RetroBicycle(Solo48):
    icon_id = 'retro-bicycle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('bicycle', 'bike', 'retro', 'cycling', 'vintage', 'pedal', 'transport', 'two wheels')

    def build(self):
        self.add_arc('rear-a',(12, 30),(12, 42),radius_x=6,radius_y=6,sweep=True)
        self.add_arc('rear-b',(12, 42),(12, 30),radius_x=6,radius_y=6,sweep=True)
        self.add_contour('rear-wheel','rear-a','rear-b',closed=True)
        self.add_arc('front-a',(36, 30),(36, 42),radius_x=6,radius_y=6,sweep=True)
        self.add_arc('front-b',(36, 42),(36, 30),radius_x=6,radius_y=6,sweep=True)
        self.add_contour('front-wheel','front-a','front-b',closed=True)
        self.add_polyline('frame',(12, 21),(24, 12),(30, 21),(12, 21),closed=False)
        self.add_line('strut',(12, 21),(12, 30))
        self.add_polyline('fork',(36, 30),(30, 21),(32, 6),(38, 6),closed=False)
        self.add_arc('handlebar',(38, 6),(38, 14),radius_x=4,radius_y=4,sweep=True)
        self.add_polyline('seat-post',(24, 12),(20, 6),closed=False)
        self.add_polyline('saddle',(16, 6),(20, 6),(24, 6),closed=False)
        self.relate('connect','frame','strut')
        self.relate('connect','strut','rear-wheel')
        self.relate('connect','frame','fork')
        self.relate('connect','fork','front-wheel')
        self.relate('connect','fork','handlebar')
        self.relate('connect','frame','seat-post')
        self.relate('connect','seat-post','saddle')
