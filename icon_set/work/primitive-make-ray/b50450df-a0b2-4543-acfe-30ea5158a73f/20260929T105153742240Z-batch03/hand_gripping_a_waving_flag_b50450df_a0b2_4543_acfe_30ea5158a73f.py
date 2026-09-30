"""romance pride lesbian lgbt flag hand.
Symbol plan: SQUARE extremes (6,6)-(42,42). Flag attached to pole at24,6/18, short exposed pole to24,26, broad left-entering hand with rounded knuckles.
Lucide hand and hand-fist: rounded fingertips, coherent palm contours. Shared human references inspected; detached-head spacing does not apply to hands.
Deliberate anatomical asymmetry preserves the supplied pose."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b50450df-a0b2-4543-acfe-30ea5158a73f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-gripping-a-waving-flag/20260929T104744Z-thuan-mac/reference/romance pride lesbian lgbt flag hand_b50450df-a0b2-4543-acfe-30ea5158a73f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-gripping-a-waving-flag'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hand', 'gripping', 'a', 'waving', 'flag')
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def bez(n,a,*segments): self.add_bezier(n,a,*segments)
        def path(n,*points,closed=False): self.add_polyline(n,*points,closed=closed)
        def contour(n,*members,closed=False): self.add_contour(n,*members,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r)
            arc(n+'b',(x+r,y),(x-r,y),r)
            contour(n,n+'a',n+'b',closed=True)


        bez('flag-top',(24,6),((31,6),(33,12),(42,9)))
        line('flag-right',(42,9),(42,20))
        bez('flag-bottom',(42,20),((33,23),(31,17),(24,17)))
        line('flag-hoist',(24,17),(24,6))
        contour('flag','flag-top','flag-right','flag-bottom','flag-hoist',closed=True)
        line('pole',(24,17),(24,29));connect('pole','flag')
        bez('hand-top',(6,31),((16,31),(13,25),(20,25)),((22,25),(24,25),(27,25)))
        bez('thumb',(27,25),((30,25),(31,27),(30,31)))
        line('knuckle-top',(30,31),(34,31))
        bez('fingers',(34,31),((40,31),(40,36),(34,36)),((40,36),(40,42),(34,42)))
        bez('hand-bottom',(34,42),((22,42),(15,42),(6,40)))
        contour('hand','hand-top','thumb','knuckle-top','fingers','hand-bottom')
        connect('pole','hand')

