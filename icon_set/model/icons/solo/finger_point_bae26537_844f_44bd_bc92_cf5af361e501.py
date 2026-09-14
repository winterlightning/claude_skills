'Pointing hand: proportional fingers with equal circular caps and a smooth, balanced palm.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bae26537-844f-44bd-bc92-cf5af361e501'
SOURCE_PATH = 'icons-json/wayfinding/finger point_bae26537-844f-44bd-bc92-cf5af361e501.json'
AUTHOR = 'gpt-6'

class FingerPoint(Solo48):
    icon_id = 'finger-point'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('finger', 'point', 'wayfinding')

    def build(self):
        # Pointing hand: proportional fingers with equal circular caps and a smooth, balanced palm.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        # Human hand: circular fingertip caps and one smooth palm, no tiny joints.
        mirror=False
        def pt(x,y):
            return (48-x if mirror else x,y)
        def arc(name,start,end,rx,ry=None,sweep=True):
            a(name,pt(*start),pt(*end),rx,ry,not sweep if mirror else sweep)
        def line(name,start,end):
            l(name,pt(*start),pt(*end))
        arc('palm',(8,32),(40,32),16,12,sweep=False)
        line('right',(40,32),(40,24))
        arc('little',(40,24),(32,24),4,sweep=False)
        line('rise',(32,24),(32,20))
        arc('middle',(32,20),(24,20),4,sweep=False)
        line('finger-right',(24,20),(24,8))
        arc('fingertip',(24,8),(16,8),4,sweep=False)
        line('finger-left',(16,8),(16,24))
        arc('thumb',(16,24),(8,24),4,sweep=False)
        line('left',(8,24),(8,32))
        self.add_contour('hand','palm','right','little','rise','middle','finger-right','fingertip','finger-left','thumb','left',closed=True)
        for x,y in ((16,24),(24,20),(32,24)):
            line(f'crease-{x}',(x,y),(x,y+4))
            link('connect',f'crease-{x}','hand')
