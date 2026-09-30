"""The rejected portrait has a V-shaped helmet and a dot instead of goatee. Restore rounded helmet sides, a recognizable goatee and smooth shoulders.
Plan: VRECT_L; exact SOLO48 centerline envelope, stroke4, integer coordinates.
Construction: Shared human circular jaw and smooth shoulders; rounded helmet shape with an outlined goatee.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b52272fb-726b-546b-b8ff-a118b721ad8b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__helmeted-man-with-goatee/20260929T105027Z-thuan-mac/reference/ironman_b52272fb-726b-546b-b8ff-a118b721ad8b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'helmeted-man-with-goatee'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('helmeted', 'man', 'with', 'goatee')
    human_construction = "bust"

    def build(self):

        def path(n,start,*commands,closed=False):
            here=start; members=[]
            for j,cmd in enumerate(commands):
                k=f'{n}-{j}';kind,end,*args=cmd
                if kind=='L': self.add_line(k,here,end)
                elif kind=='A': self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k);here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x,y-r),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True),closed=True)
        def poly(n,*pts,closed=False):self.add_polyline(n,*pts,closed=closed)
        def line(n,a,b):self.add_line(n,a,b)
        def bez(n,a,*parts):self.add_bezier(n,a,*parts)
        def arc(n,a,b,r,ry=None,s=True):self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(a,b):self.relate('connect',a,b)
        def rect(n,l,t,r,b,rad=3):
            path(n,(l+rad,t),('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True),closed=True)
        path('helmet',(10,25),('L',(10,18)),('A',(38,18),14,14,True),('L',(38,25)))
        path('face',(14,16),('L',(14,24)),('A',(34,24),10,10,False),('L',(34,16)))
        path('hairline',(14,16),('C',(24,18),(17,13),(20,18)),('C',(34,16),(28,18),(31,13)));join('hairline','face')
        path('goatee',(20,29),('L',(20,25)),('A',(28,25),4,4,True),('L',(28,29)))
        path('body',(8,44),('A',(20,38),12,6,True),('L',(28,38)),('A',(40,44),12,6,True));join('body','face')
