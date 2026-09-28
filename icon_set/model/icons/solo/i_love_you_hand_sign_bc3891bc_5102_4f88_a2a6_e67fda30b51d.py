"""Two raised fingers with rounded tips, folded middle valley and broad palm; rounded diagonal thumb replaces squared thumb.
Keyshape SQUARE. Lucide hand-metal: rounded fingertips, curved thumb and flowing palm. Human hand has no detached head gap.
Omissions: Two folded fingers consolidated into broad U-shaped valley."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bc3891bc-5102-4f88-a2a6-e67fda30b51d'
SOURCE_PATH = 'pictographic-primitives/wayfinding/love you sign_bc3891bc-5102-4f88-a2a6-e67fda30b51d.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'i-love-you-hand-sign'
    keyshape = Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "wayfinding"
    categories = ("wayfinding", "primitives")
    aliases=()
    keywords=('i', 'love', 'you', 'hand', 'sign')

    def build(self):

        def path(n, start, steps, closed=False):
            members=[]; here=start
            for i,(kind,end,*a) in enumerate(steps):
                if here==end: continue
                tag=f'{n}-{i}'
                if kind=='L': self.add_line(tag,here,end)
                elif kind=='A': self.add_arc(tag,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C': self.add_bezier(tag,here,(a[0],a[1],end))
                members.append(tag); here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,q=4):
            path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('hand',(14,33),[('L',(7,27)),('C',(6,23),(6,26),(6,25)),('C',(14,25),(6,19),(12,23)),('L',(14,10)),('A',(22,10),4,4,True),('L',(22,26)),('A',(34,26),6,6,False),('L',(34,14)),('A',(42,14),4,4,True),('L',(42,28)),('A',(28,42),14,14,True),('L',(23,42)),('C',(14,33),(18,42),(16,37))],True)

