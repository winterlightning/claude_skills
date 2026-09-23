from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5dd7944c-8248-40cb-8bd4-400ceb51cae0'
SOURCE_PATH = 'icon_set/work/todo-references/car wrench_5dd7944c-8248-40cb-8bd4-400ceb51cae0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'car-wrench'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('car', 'wrench')

    def build(self):
        # Same symmetric car envelope with horizontal double-ended wrench: mirrored jaws connect to shared central shaft.

        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
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
        self.add_polyline('roof',(8,20),(12,20),(18,8),(30,8),(36,20),(40,20))
        self.add_arc('nose-right',(40,20),(44,24),radius_x=4)
        self.add_line('side-right',(44,24),(44,34))
        self.add_line('bumper-right',(44,34),(40,34))
        self.add_arc('wheel-right',(40,34),(28,34),radius_x=6)
        self.add_line('base',(28,34),(20,34))
        self.add_arc('wheel-left',(20,34),(8,34),radius_x=6)
        self.add_line('bumper-left',(8,34),(4,34))
        self.add_line('side-left',(4,34),(4,24))
        self.add_arc('nose-left',(4,24),(8,20),radius_x=4)
        self.add_contour('body','nose-right','side-right','bumper-right','wheel-right','base','wheel-left','bumper-left','side-left','nose-left')
        self.relate('connect','roof','body')

        self.add_arc('jaw-left-upper',(16,20),(20,24),radius_x=4)
        self.add_arc('jaw-left-lower',(20,24),(16,28),radius_x=4)
        self.add_arc('jaw-right-upper',(32,20),(28,24),radius_x=4,sweep=False)
        self.add_arc('jaw-right-lower',(28,24),(32,28),radius_x=4,sweep=False)
        self.add_line('shaft',(20,24),(28,24))
        self.add_contour('jaw-left','jaw-left-upper','jaw-left-lower')
        self.add_contour('jaw-right','jaw-right-upper','jaw-right-lower')
        self.relate('connect','jaw-left','shaft')
        self.relate('connect','jaw-right','shaft')
