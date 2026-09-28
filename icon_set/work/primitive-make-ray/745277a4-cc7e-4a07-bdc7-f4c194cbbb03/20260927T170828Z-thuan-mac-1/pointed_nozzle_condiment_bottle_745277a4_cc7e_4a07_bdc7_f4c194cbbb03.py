"""Pointed Nozzle Condiment Bottle
Plan: Squeeze bottle with pointed nozzle, screw collar and upright label.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Oval label omitted after vertical spacing repair; pointed nozzle, collar and squeeze body retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '745277a4-cc7e-4a07-bdc7-f4c194cbbb03'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pointed-nozzle-condiment-bottle/20260927T170540Z-thuan-mac-1/reference/catsup_745277a4-cc7e-4a07-bdc7-f4c194cbbb03.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'pointed-nozzle-condiment-bottle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bottle', 'condiment', 'squeeze', 'nozzle', 'label', 'sauce', 'kitchen')

    def build(self):
        # Wide labeled body, shallow collar and pointed nozzle.
        self.add_line('body-top',(14,16),(34,16))
        self.add_line('body-right',(34,16),(40,40))
        self.add_arc('body-br',(40,40),(36,44),radius_x=4)
        self.add_line('body-bottom',(36,44),(12,44))
        self.add_arc('body-bl',(12,44),(8,40),radius_x=4)
        self.add_line('body-left',(8,40),(14,16))
        self.add_contour('body','body-top','body-right','body-br','body-bottom','body-bl','body-left',closed=True)
        self.add_line('collar-left',(14,16),(14,12))
        self.add_line('collar-right',(34,12),(34,16))
        self.add_polyline('nozzle',(14,12),(24,4),(34,12))
        self.relate('connect','body','collar-left','collar-right')
        self.relate('connect','nozzle','collar-left','collar-right')
        self.add_arc('label-upper',(19,30),(29,30),radius_x=5,radius_y=4)
        self.add_arc('label-lower',(29,30),(19,30),radius_x=5,radius_y=4)
        self.add_contour('label','label-upper','label-lower',closed=True)
