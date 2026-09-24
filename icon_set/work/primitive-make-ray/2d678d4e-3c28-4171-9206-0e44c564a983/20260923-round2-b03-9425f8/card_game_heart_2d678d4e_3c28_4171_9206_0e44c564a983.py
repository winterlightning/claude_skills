from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2d678d4e-3c28-4171-9206-0e44c564a983'
SOURCE_PATH = 'icon_set/work/todo-references/card game heart_2d678d4e-3c28-4171-9206-0e44c564a983.svg'
AUTHOR = 'gpt-6'

PLAN = 'Three hearts on an upright playing card; reduce the central suit while preserving both opposing corner marks.'
PARENT_RESULT = 'icon_set/work/primitive-make-ray/2d678d4e-3c28-4171-9206-0e44c564a983/20260922T222359-37f3f9/result.json'

class Drawing(Solo48):
    icon_id = 'card-game-heart'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('ace', 'of', 'hearts', 'playing', 'card')

    def build(self):
        # Rounded ace card with central heart and opposing corner hearts. Heart helper owns lobe radii, mirrored sides and orientation; lower corner rotates 180 degrees. VRECT_L ink (6,2)-(42,46).
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
        rounded('card',8,4,40,44,4)
        def heart(n,x,y,r,h,flip=False):
            s=-1 if flip else 1
            self.add_arc(n+'-l',(x-2*r,y),(x,y),radius_x=r,sweep=not flip)
            self.add_arc(n+'-r',(x,y),(x+2*r,y),radius_x=r,sweep=not flip)
            self.add_line(n+'-a',(x+2*r,y),(x,y+s*h))
            self.add_line(n+'-b',(x,y+s*h),(x-2*r,y))
            self.add_contour(n,n+'-l',n+'-r',n+'-a',n+'-b',closed=True)
        heart('main',24,24,3,7)
        heart('upper',17,13,2,4)
        heart('lower',31,35,2,4,True)
