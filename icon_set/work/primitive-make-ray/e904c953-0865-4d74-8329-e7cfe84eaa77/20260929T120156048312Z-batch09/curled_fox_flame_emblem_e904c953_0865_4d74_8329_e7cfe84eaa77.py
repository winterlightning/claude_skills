"""Fox flame: rejected emblem is an open loop without fox head. Restore pointed ear, snout notch, flame crest and closed curling silhouette. Restore closed curling flame with fox ear and snout notch.
Symbol plan: Original Firefox fox/flame silhouette; no useful direct Lucide match.
Keyshape VRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e904c953-0865-4d74-8329-e7cfe84eaa77'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__curled-fox-flame-emblem/20260929T115456Z-thuan-mac/reference/firefox logo_e904c953-0865-4d74-8329-e7cfe84eaa77.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'curled-fox-flame-emblem'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('curled', 'fox', 'flame', 'emblem')

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

        path('flame',(8,27),[('C',(16,13),(8,21),(12,17)),('C',(21,22),(15,18),(18,21)),('L',(27,24)),('L',(21,28)),('A',(32,29),6,6,False),('C',(24,16),(35,23),(31,18)),('C',(26,4),(23,10),(24,7)),('C',(37,20),(32,8),(36,14)),('L',(39,16)),('C',(40,28),(40,20),(40,24)),('A',(24,44),16,16,True),('A',(8,28),16,16,True),('L',(8,27))],True)
