"""Hand-holding pair: rejected outside arms are rigid horizontal bars and heads too small. Restore sloping arms, larger heads and a joined central hand. Enlarge both heads and slope the outside arms while keeping symmetric joined hands.
Symbol plan: human_ref/full_body_ref.png: equal radius5 heads, lower16 to neck24 gives exact4 ink gap; mirrored anatomy.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b1093f49-5d2c-4508-a577-bc47b584a0c8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-angular-figures-holding-hands/20260929T115456Z-thuan-mac/reference/group 1_b1093f49-5d2c-4508-a577-bc47b584a0c8.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'two-angular-figures-holding-hands'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('two', 'angular', 'figures', 'holding', 'hands')

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

        for x in [14,34]:
         circle(f'head-{x}',x,11,5)
         line(f'torso-{x}',(x,24),(x,33))
         poly(f'legs-{x}',(x-6,42),(x,33),(x+6,42));join(f'torso-{x}',f'legs-{x}')
         self.mark_human_figure(f'person-{x}',head=f'head-{x}',torso=f'torso-{x}',torso_junction='start')
        poly('arms',(6,29),(14,24),(24,31),(34,24),(42,29))
        join('arms','torso-14');join('arms','torso-34')
