'Dolphin through a hoop: preserve the curved swimming body and fins, trimming the visible hoop segments to open the separating gaps.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd4fb0227-9b14-58a1-aeaf-56f5e901881f'
SOURCE_PATH = 'pictographic-primitives/animals/dolphin jump_d4fb0227-9b14-58a1-aeaf-56f5e901881f.svg'
AUTHOR = 'gpt-6'


class DolphinThroughHoop(Solo48):
    icon_id = 'dolphin-through-hoop'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    aliases = ()
    keywords = ('dolphin', 'hoop', 'jump', 'circus', 'trick', 'marine', 'show', 'sea')

    def build(self) -> None:
        self.add_bezier('head',(6,26),((7,22),(11,19),(16,18)))
        self.add_polyline('dorsal',(16,18),(23,15),(23,20))
        self.add_bezier('back',(23,20),((29,20),(34,21),(37,23)))
        self.add_polyline('tail',(37,23),(42,20),(42,32),(35,29))
        self.add_bezier('belly',(35,29),((31,28),(27,29),(24,30)))
        self.add_polyline('flipper',(24,30),(24,33),(17,29),(6,33),(6,26))
        for a,b in (('head','dorsal'),('dorsal','back'),('back','tail'),('tail','belly'),('belly','flipper'),('flipper','head')):self.relate('connect',a,b)
        self.add_bezier('hoop-top',(16,9),((18,7),(21,6),(24,6)),((28,6),(31,7),(34,10)))
        self.add_bezier('hoop-bottom',(32,40),((30,42),(27,42),(24,42)),((21,42),(18,42),(16,40)))
