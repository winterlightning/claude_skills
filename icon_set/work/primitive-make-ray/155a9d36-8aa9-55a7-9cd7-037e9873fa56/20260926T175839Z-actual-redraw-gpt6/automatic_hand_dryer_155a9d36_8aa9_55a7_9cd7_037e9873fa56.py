"An open hand extends palm-up beneath a domed wall dryer. Three short wavy air streams descend from the dryer's flat underside toward the fingers and palm.\n\nConstruction: Domed dryer above a cupped hand; two airflow marks retained; minor creases omitted to give the palm enough depth. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '155a9d36-8aa9-55a7-9cd7-037e9873fa56'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-under-automatic-dryer/20260926T172218Z-thuan-mac-1/reference/automatic hand dryer_155a9d36-8aa9-55a7-9cd7-037e9873fa56.svg'
AUTHOR = "gpt-6"

class HandUnderAutomaticDryer(Solo48):
    icon_id = 'hand-under-automatic-dryer'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('hand', 'dryer', 'automatic', 'hygiene', 'washroom', 'air')

    def build(self):
        # A domed wall unit sends two separated air strokes to a lower open palm.
        self.add_arc('dome-left',(8,13),(18,4),radius_x=10,radius_y=9,sweep=True)
        self.add_line('dome-top',(18,4),(30,4))
        self.add_arc('dome-right',(30,4),(40,13),radius_x=10,radius_y=9,sweep=True)
        self.add_line('dryer-base',(40,13),(8,13))
        self.add_contour('dryer','dome-left','dome-top','dome-right','dryer-base',closed=True)
        self.add_line('hand-rise',(8,38),(16,32))
        self.add_line('palm-top',(16,32),(27,32))
        self.add_line('finger-top',(27,32),(33,29))
        self.add_line('finger-flat',(33,29),(37,29))
        self.add_arc('fingertip',(37,29),(39,32),radius_x=4,sweep=True)
        self.add_arc('finger-under',(39,32),(38,35),radius_x=3,sweep=True)
        self.add_line('palm-under',(38,35),(24,44))
        self.add_line('wrist',(24,44),(8,44))
        self.add_contour('hand','hand-rise','palm-top','finger-top','finger-flat','fingertip','finger-under','palm-under','wrist')
        self.add_line('thumb',(27,32),(31,36))
        self.relate('connect','thumb','hand')
        for index,x in enumerate((17,25)):
            self.add_line(f'air-{index}',(x,22),(x,23))
