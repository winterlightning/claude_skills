"""Rounded left-facing head and broad curved mask with rising rear strap; mask side seam shares exact attachment nodes.
Keyshape VRECT_L. Shared human user.svg for circular skull; supplied reference for mask curve.
Omissions: Small eye and inner ear omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6125bb03-817d-547b-932c-5f4a4b4f96ed'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/air pollution mask_6125bb03-817d-547b-932c-5f4a4b4f96ed.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'head-profile-wearing-broad-protective-mask'
    keyshape = Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/ecology"
    aliases=()
    keywords=('head', 'profile', 'wearing', 'broad', 'protective', 'mask')

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

        path('skull',(8,20),[('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,30)),('C',(35,38),(40,34),(35,34)),('L',(35,44))])
        path('mask',(8,20),[('L',(8,30)),('A',(14,36),6,6,False),('L',(17,36)),('L',(23,36)),('L',(40,30))])
        path('strap',(8,20),[('C',(23,22),(14,22),(18,23)),('L',(40,20))])
        path('seam',(23,22),[('L',(23,36))]);join('mask','seam');join('strap','seam');join('mask','skull');join('strap','skull');join('strap','mask')
        line('neck',(17,36),(17,44));join('neck','mask')
        # The rear strap terminates at the crown and side shared node.

