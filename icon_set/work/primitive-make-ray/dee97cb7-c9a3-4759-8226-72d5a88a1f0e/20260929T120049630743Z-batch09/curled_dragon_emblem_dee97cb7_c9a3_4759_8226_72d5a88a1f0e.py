"""Dragon emblem: rejected dragon looks like a circular letter G. Restore pointed dragon head and stronger curved wing/tail silhouette. Restore pointed beak and sweeping upper wing in a round curled dragon silhouette.
Symbol plan: Original pointed inner head, large circular wing and curled tail; no useful direct Lucide match.
Keyshape CIRCLE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'dee97cb7-c9a3-4759-8226-72d5a88a1f0e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__curled-dragon-emblem/20260929T115456Z-thuan-mac/reference/dragon sigil_dee97cb7-c9a3-4759-8226-72d5a88a1f0e.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'curled-dragon-emblem'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('curled', 'dragon', 'emblem')

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

        path('dragon',(24,4),[('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(4,24),20,20,True),('C',(12,9),(4,18),(8,12)),('C',(20,26),(7,22),(12,27)),('C',(32,16),(28,28),(32,21)),('L',(22,16)),('C',(24,4),(17,12),(18,6))],True)
