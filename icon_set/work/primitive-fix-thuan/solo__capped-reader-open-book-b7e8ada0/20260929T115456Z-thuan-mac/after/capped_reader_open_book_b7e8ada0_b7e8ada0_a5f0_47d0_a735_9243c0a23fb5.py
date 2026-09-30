"""Capped reader: rejected face resembles a barred circle and book is flat-bottomed. Restore cap silhouette and a deeper open-book fold. Give the cap a domed crown over a circular jaw and deepen the book pages around a central fold.
Symbol plan: human_ref/user.svg circular jaw lower24 and shoulder28 touching ink; source cap and open book.
Keyshape VRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b7e8ada0-a5f0-47d0-a735-9243c0a23fb5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__capped-reader-open-book-b7e8ada0/20260929T115456Z-thuan-mac/reference/muslim reading quraan 3_b7e8ada0-a5f0-47d0-a735-9243c0a23fb5.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'capped-reader-open-book-b7e8ada0'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('capped', 'reader', 'open', 'book', 'b7e8ada0')
    human_construction = "bust"
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

        path('head',(16,12),[('A',(32,12),8,8,True),('L',(32,16)),('A',(16,16),8,8,True),('L',(16,12))],True)
        line('cap',(16,12),(32,12));join('head','cap')
        path('shoulders',(8,31),[('A',(24,28),16,3,True),('A',(40,31),16,3,True)]);join('head','shoulders')
        poly('book',(8,31),(24,35),(40,31),(40,40),(24,44),(8,40),closed=True)
        line('fold',(24,35),(24,44));join('fold','book');join('shoulders','book')
