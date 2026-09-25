"""Hestia extends a hand under a pointed flame. Lucide user-round informs the figure; omit tunic folds and tiny facial details while preserving fire and long hair."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c274181e-f042-4328-adad-24b896725381'
SOURCE_PATH = 'pictographic-primitives/religion/hestia_c274181e-f042-4328-adad-24b896725381.svg'
AUTHOR = 'gpt-6'

class HestiaWithFlame(Solo48):
    icon_id = 'hestia-with-flame'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "religion"
    aliases = ()
    keywords = ('hestia', 'goddess', 'flame', 'hearth', 'greek', 'mythology', 'figure')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Centerline box (8,4)-(40,44), asymmetric flame over outstretched hand.
        self.oval('head',15,10,6)
        self.add_line('hair',(9,10),(8,20));self.relate('connect','head','hair')
        self.add_polyline('gown',(13,27),(8,44),(27,44),(25,34),(23,27),(13,27))
        self.add_line('arm',(25,34),(40,34));self.relate('connect','arm','gown')
        self.add_line('flame-left',(36,4),(30,15))
        self.add_arc('flame-base',(30,15),(40,15),radius_x=5,radius_y=7,sweep=False)
        self.add_line('flame-tip',(40,15),(36,4))
        self.add_contour('flame','flame-left','flame-base','flame-tip',closed=True)
