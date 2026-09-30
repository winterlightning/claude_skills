"""The rejected moustache resembles goggles: round lobes and central pinches. Restore the broad flowing moustache contour and distinct upturned outer tips.
Plan: HRECT_M; exact SOLO48 centerline envelope, stroke4, integer coordinates.
Construction: No useful exact Lucide moustache match; mirrored flowing lobes and upturned tips derive from one axis.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '00ac7dca-2cda-4195-b41c-814f500675f8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__handlebar-moustache-with-upturned-tips/20260929T105027Z-thuan-mac/reference/moustache_00ac7dca-2cda-4195-b41c-814f500675f8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'handlebar-moustache-with-upturned-tips'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('handlebar', 'moustache', 'with', 'upturned', 'tips')

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
        path('moustache',(24,17),('C',(14,10),(20,10),(18,10)),('C',(4,20),(10,10),(10,24)),('C',(14,38),(4,33),(8,38)),('C',(24,29),(19,38),(22,34)),('C',(34,38),(26,34),(29,38)),('C',(44,20),(40,38),(44,33)),('C',(34,10),(38,24),(38,10)),('C',(24,17),(30,10),(28,10)),closed=True)
