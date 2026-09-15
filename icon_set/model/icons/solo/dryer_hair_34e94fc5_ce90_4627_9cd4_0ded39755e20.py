"""dryer-hair: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '34e94fc5-ce90-4627-9cd4-0ded39755e20'
SOURCE_PATH = 'pictographic-primitives/symbol/dryer hair_34e94fc5-ce90-4627-9cd4-0ded39755e20.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class DryerHair(Solo48):
    icon_id = 'dryer-hair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('dryer', 'hair', 'symbol')

    def build(self):
        # Plan: SQUARE; smooth motor housing and rounded handle base, retaining directional nozzle.
        # Reference: Geometric smooth housing; no close Lucide hairdryer match.
        self.add_line('nozzle-top',(6,10),(28,7))
        self.add_bezier('back-top',(28,7),((32,7-6/11),(32,6),(34,6)),((39,6),(42,10),(42,16)))
        self.add_bezier('back-bottom',(42,16),((42,21),(38,23),(36,28)))
        self.add_line('handle-right',(36,28),(31,38))
        self.add_bezier('handle-base',(31,38),((30,40),(29,42),(26,42)),((23,42),(21,41),(20,40)))
        self.add_line('handle-left',(20,40),(25,26))
        self.add_polyline('nozzle-bottom',(25,26),(6,22),(6,10))
        self.add_contour('outline','nozzle-top','back-top','back-bottom','handle-right','handle-base','handle-left','nozzle-bottom-1','nozzle-bottom-2',closed=True)
        self.contours.pop(0)
