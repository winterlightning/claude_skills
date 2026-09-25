"""peso-money: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bfac5a0c-eae9-420e-af5e-4ac03cb24f16'
SOURCE_PATH = 'pictographic-primitives/money/peso_bfac5a0c-eae9-420e-af5e-4ac03cb24f16.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class PesoMoney(Solo48):
    icon_id = 'peso-money'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    categories = ('primitives', 'money')
    aliases = ()
    keywords = ('peso', 'money')

    def build(self):
        # Plan: SQUARE; one semicircular P bowl meets horizontal top and crossbar.
        # Reference: Geometric letter construction with tangent bowl.
        self.add_polyline('stem',(14,42),(14,6),(33,6))
        self.add_arc('bowl',(33,6),(33,24),radius_x=9)
        self.add_line('bar',(33,24),(6,24))
        self.add_contour('run','stem-1','stem-2','bowl','bar')
        self.contours.pop(0)
