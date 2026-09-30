"""The rejected hand was an ordinary closed-finger palm. Restore the identifying V separation between paired fingers and a projecting thumb.
Symbol plan: Lucide hand original and atoms for round finger tips; source paired-finger V separation retained with single strokes.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e707413f-0adc-48cf-b5cf-de4b6e2e3b22'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__vulcan-salute-hand/20260929T122443Z-thuan-mac/reference/vulcan salute 2_e707413f-0adc-48cf-b5cf-de4b6e2e3b22.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'vulcan-salute-hand'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('vulcan', 'salute', 'hand')

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

        path('palm',(8,24),[('L',(8,30)),('A',(20,42),12,12,False),('L',(26,42)),('C',(42,26),(36,42),(42,33)),('L',(39,29))])
        line('little',(8,24),(6,12));join('little','palm')
        poly('inner-left',(8,24),(16,24),(14,6));join('inner-left','palm');join('inner-left','little')
        poly('inner-right',(16,24),(27,24),(32,6));join('inner-right','inner-left')
        poly('outer-right',(27,24),(36,24),(40,12));join('outer-right','inner-right')
