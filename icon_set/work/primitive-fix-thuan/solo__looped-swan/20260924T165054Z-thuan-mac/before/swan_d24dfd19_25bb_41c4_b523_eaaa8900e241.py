'Rebuilt smooth head, neck and hull curves around an open counter; retained the curled wing silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd24dfd19-25bb-41c4-b523-eaaa8900e241'
SOURCE_PATH = 'pictographic-primitives/animals/swan_d24dfd19-25bb-41c4-b523-eaaa8900e241.svg'
AUTHOR = 'gpt-6'


class LoopedSwan(Solo48):
    icon_id = 'looped-swan'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('swan', 'bird', 'neck', 'curve', 'pond', 'elegant', 'waterfowl', 'loop')

    def build(self) -> None:
        self.add_bezier('head-left',(24,17),((24,10),(28,6),(34,6)))
        self.add_bezier('head-right',(34,6),((39,6),(42,10),(42,15)))
        self.add_line('beak',(42,15),(34,15))
        self.add_bezier('neck-inner',(34,15),((32,20),(36,24),(40,28)))
        self.add_bezier('breast',(40,28),((42,30),(42,32),(42,33)))
        self.add_bezier('hull-right',(42,33),((42,39),(33,42),(24,42)))
        self.add_bezier('hull-left',(24,42),((14,42),(6,38),(6,32)))
        self.add_bezier('wing-back',(6,32),((6,28),(10,24),(15,24)))
        self.add_bezier('wing-top',(15,24),((21,24),(21,32),(15,32)))
        self.add_bezier('neck-outer',(15,32),((29,32),(24,24),(24,17)))
        self.add_contour('outline','head-left','head-right','beak','neck-inner','breast','hull-right','hull-left','wing-back','wing-top','neck-outer',closed=True)
