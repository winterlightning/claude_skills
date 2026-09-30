"""Trees: rejected rear trees have no trunks and read as mountain peaks. Restore layered tree silhouettes and three trunks. Restore three centered trunks, with a tall narrow foreground tree and smaller rear canopies.
Symbol plan: Lucide trees original/atoms: staggered pointed canopies and three centered trunks; branch steps omitted.
Keyshape HRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '309d15f7-00c9-465a-a770-df107f7c15ef'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-evergreen-trees/20260929T115456Z-thuan-mac/reference/forest_309d15f7-00c9-465a-a770-df107f7c15ef.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'three-evergreen-trees'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('three', 'evergreen', 'trees')

    def build(self):

        def path(n,start,steps,closed=False):
            point=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L': self.add_line(m,point,end)
                elif kind=='A': self.add_arc(m,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(m,point,(args[0],args[1],end))
                point=end; members.append(m)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        poly('front',(24,8),(28,24),(30,32),(24,32),(18,32),(20,24),closed=True)
        poly('left',(20,24),(4,24),(10,16),(20,24))
        poly('right',(28,24),(44,24),(38,16),(28,24));join('left','front');join('right','front')
        for n,x,top in [('mid',24,32),('left',10,24),('right',38,24)]:
         line(f'trunk-{n}',(x,top),(x,40));join(f'trunk-{n}','front' if n=='mid' else n)
