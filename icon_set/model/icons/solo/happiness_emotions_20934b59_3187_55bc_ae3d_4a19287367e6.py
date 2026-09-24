"""Smooth continuous skull, sloping nose, rounded chin and a gentle smile terminating on the profile.
Keyshape VRECT_L. Shared human user.svg: smooth head vocabulary; original profile has continuous neck, so no detached gap.
Omissions: No eye added; preserve the original smile."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '20934b59-3187-55bc-ae3d-4a19287367e6'
SOURCE_PATH = 'pictographic-primitives/health/happiness emotions_20934b59-3187-55bc-ae3d-4a19287367e6.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'happiness-emotions'
    keyshape = Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="health"
    aliases=()
    keywords=('happiness', 'emotions')

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

        path('profile',(16,44),[('L',(16,36)),('C',(8,20),(16,30),(8,28)),('A',(24,4),16,16,True),('C',(40,25),(36,4),(35,15)),('L',(34,26)),('L',(34,30)),('A',(26,38),8,8,True),('L',(26,44))])
        path('smile',(26,27),[('C',(34,30),(28,30),(31,31))]);join('smile','profile')
