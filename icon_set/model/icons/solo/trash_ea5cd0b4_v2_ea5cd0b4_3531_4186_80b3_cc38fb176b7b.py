'trash-ea5cd0b4: distinct review variant.\n\nConstruction: Waste bin with an arched handle and two vertical ribs; separate it from the plain bin with a stem handle.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nConstruction reference: trash-2 from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'ea5cd0b4-3531-4186-80b3-cc38fb176b7b'
SOURCE_PATH = 'pictographic-primitives/symbol/trash_ea5cd0b4-3531-4186-80b3-cc38fb176b7b.svg'
AUTHOR = 'gpt-6'


class TrashEa5cd0b4Variant2(Solo48):
    icon_id = 'trash-ea5cd0b4-v2'
    variant_of = 'trash-ea5cd0b4'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('trash', 'symbol')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'bin',(10,14),('L',(10,39)),('A',5,5,False,(15,44)),('L',(33,44)),('A',5,5,False,(38,39)),('L',(38,14)))
        line(self,'lid',(8,14),(40,14))
        path(self,'handle',(18,14),('L',(18,9)),('A',5,5,True,(23,4)),('L',(25,4)),('A',5,5,True,(30,9)),('L',(30,14)))
        for x in (20,28):line(self,f'rib-{x}',(x,24),(x,34))
        contacts(self)
