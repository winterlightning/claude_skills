from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '207acda0-b0e1-481e-9cb8-b0522fe56419'
SOURCE_PATH = 'icon_set/work/todo-references/chat conversation love romance talk_207acda0-b0e1-481e-9cb8-b0522fe56419.svg'
AUTHOR = 'gpt-6'

PLAN = 'Two overlapping speech bubbles and a front heart; redistribute front-bubble area and use an oblique rear tail.'
PARENT_RESULT = 'icon_set/work/primitive-make-ray/207acda0-b0e1-481e-9cb8-b0522fe56419/20260922T222907-8c0fa4/result.json'

class Drawing(Solo48):
    icon_id = 'chat-conversation-love-romance-talk'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('romantic', 'chat', 'conversation')

    def build(self):
        # Two overlapping speech bubbles, foreground carrying a heart. Front/right and rear/left tails keep conversation arrangement. Square ink(4,4)-(44,44). Heart lobes share radius3 around axis29.
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def rect(n,l,t,r,b):
            self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True)
        def rounded(n,l,t,r,b,k):
            self.add_line(n+'-t',(l+k,t),(r-k,t))
            self.add_arc(n+'-tr',(r-k,t),(r,t+k),radius_x=k)
            self.add_line(n+'-r',(r,t+k),(r,b-k))
            self.add_arc(n+'-br',(r,b-k),(r-k,b),radius_x=k)
            self.add_line(n+'-b',(r-k,b),(l+k,b))
            self.add_arc(n+'-bl',(l+k,b),(l,b-k),radius_x=k)
            self.add_line(n+'-l',(l,b-k),(l,t+k))
            self.add_arc(n+'-tl',(l,t+k),(l+k,t),radius_x=k)
            self.add_contour(n,*[n+'-'+s for s in ['t','tr','r','br','b','bl','l','tl']],closed=True)

        self.add_polyline('rear',(30,14),(30,6),(6,6),(6,22),(10,22),(6,30),(14,24))
        self.add_polyline('front',(14,14),(42,14),(42,38),(36,38),(36,42),(32,38),(14,38),closed=True)
        self.relate('connect','front','rear')
        self.add_arc('heart-left',(24,25),(28,25),radius_x=2)
        self.add_arc('heart-right',(28,25),(32,25),radius_x=2)
        self.add_polyline('heart-point',(32,25),(28,29),(24,25))
        self.add_contour('heart','heart-left','heart-right','heart-point-1','heart-point-2',closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='heart-point']
