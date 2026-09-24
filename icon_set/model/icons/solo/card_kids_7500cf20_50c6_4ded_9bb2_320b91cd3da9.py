from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7500cf20-50c6-4ded-9bb2-320b91cd3da9'
SOURCE_PATH = 'icon_set/work/todo-references/card kids_7500cf20-50c6-4ded-9bb2-320b91cd3da9.svg'
AUTHOR = 'gpt-6'

PLAN = 'Child symbol in a square card; isolate straight shoulder junction for an exact detached-head gap and curve the raised arms outside it.'
PARENT_RESULT = 'icon_set/work/primitive-make-ray/7500cf20-50c6-4ded-9bb2-320b91cd3da9/20260923-batch07-b9ebd4/result.json'

class Drawing(Solo48):
    icon_id = 'card-kids'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('card', 'kids')

    def build(self):
        # Rounded square card encloses circular head, bowed arms and short vertical torso. Axis24; bounds6/42. Head cy18 r3; torso starts29: exact head-to-torso ink gap4.

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
        rounded('card',6,6,42,42,4)
        circle('head',24,18,3)

        self.add_bezier('arm-left',(15,25),((16,28),(18,29),(20,29)))
        self.add_polyline('shoulder',(20,29),(24,29),(28,29))
        self.add_bezier('arm-right',(28,29),((30,29),(32,28),(33,25)))
        self.add_line('torso',(24,29),(24,33))
        self.relate('connect','arm-left','shoulder')
        self.relate('connect','shoulder','arm-right','torso')
        self.mark_human_figure('child',head='head',torso='torso',torso_junction='start')
        # Actual head bottom 21; torso junction 29: 29-21-4=4 ink gap.
