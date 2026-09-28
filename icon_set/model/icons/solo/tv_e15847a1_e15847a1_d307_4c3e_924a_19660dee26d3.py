'tv-e15847a1: independent smooth-curve repair.\n\nConstruction: Television with matched rounded corners and a centered pair of aerials; feet attach to exact lower nodes.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/tv.svg and atomic-debug/tv.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'e15847a1-d307-4c3e-924a-19660dee26d3'
SOURCE_PATH = 'pictographic-primitives/tv/tv_e15847a1-d307-4c3e-924a-19660dee26d3.svg'
AUTHOR = 'gpt-6'


class TvE15847a1(Solo48):
    icon_id = 'tv-e15847a1'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tv'
    categories = ('tv', 'primitives')
    aliases = ()
    keywords = ('tv',)
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'screen',6,16,42,38,4,xs=(12,24,36))
        poly(self,'antenna',(15,6),(24,16),(33,6))
        line(self,'foot-left',(12,38),(12,42));line(self,'foot-right',(36,38),(36,42))
        contacts(self)
