from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3bcbac7-70e3-4df1-87c4-0e740b47f92b'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/children safety door unlock 1_e3bcbac7-70e3-4df1-87c4-0e740b47f92b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'unlocked-child-safety-lock'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('unlocked', 'child', 'safety', 'lock')

    def build(self):
        # Open shackle extends left of lock body containing a small child. Body offset right preserves opening; circular head r2 at(28,26), torso starts(28,36), exact4 ink gap. VRECT_L extremes(6,2)-(42,46).
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
        rounded('lock-body',16,15,40,44,4)
        self.add_line('open-end',(8,22),(8,12))
        self.add_arc('shackle-top',(8,12),(24,12),radius_x=8)
        self.add_line('shackle-right',(24,12),(24,15))
        self.add_contour('shackle','open-end','shackle-top','shackle-right')
        self.relate('connect','shackle','lock-body')
        circle('head',28,26,2)
        self.add_line('torso',(28,36),(28,44))
        self.add_polyline('arms',(24,36),(28,36),(32,36))
        self.relate('connect','torso','arms')
        self.relate('connect','torso','lock-body')
        self.mark_human_figure('child',head='head',torso='torso',torso_junction='start')
