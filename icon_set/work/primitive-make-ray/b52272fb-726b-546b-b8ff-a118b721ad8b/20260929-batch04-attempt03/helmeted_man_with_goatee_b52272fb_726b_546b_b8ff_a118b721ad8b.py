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
        circle('head',24,20,16)
        path('helmet',(8,20),('C',(14,12),(10,17),(12,14)),('C',(24,13),(17,12),(20,13)),('C',(34,12),(28,13),(31,12)),('C',(40,20),(36,14),(38,17)));join('helmet','head')
        path('goatee',(20,23),('L',(20,25)),('A',(22,27),2,2,False),('L',(26,27)),('A',(28,25),2,2,False),('L',(28,23)))
        path('body',(8,44),('A',(24,40),16,4,True),('A',(40,44),16,4,True));join('body','head')
