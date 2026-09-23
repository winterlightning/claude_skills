from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94d5a32b-ed7e-407e-b22e-5de85f0623bf'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/children safety door lock 1_94d5a32b-ed7e-407e-b22e-5de85f0623bf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'child-safety-padlock'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('child', 'safety', 'padlock')

    def build(self):
        # Padlock with arched shackle and child figure embedded in lower body. Shared symmetry axis24; head radius3 at(24,25), torso begins(24,36) giving exactly8 centerline/4 ink gap. VRECT_L ink(6,2)-(42,46).
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
        rounded('lock-body',8,13,40,44,4)
        self.add_line('shackle-left',(16,13),(16,12))
        self.add_arc('shackle-top',(16,12),(32,12),radius_x=8)
        self.add_line('shackle-right',(32,12),(32,13))
        self.add_contour('shackle','shackle-left','shackle-top','shackle-right')
        self.relate('connect','lock-body','shackle')
        circle('head',24,25,3)
        self.add_line('torso',(24,36),(24,44))
        self.add_polyline('arms',(16,33),(20,36),(24,36),(28,36),(32,33))
        self.relate('connect','torso','arms')
        self.relate('connect','torso','lock-body')
        self.mark_human_figure('child',head='head',torso='torso',torso_junction='start')
