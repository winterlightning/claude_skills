"""Shoreline with Ocean Waves.

Plan: Retained the rising shore, horizon and two water waves. Omitted the second narrow descending slope and widened spacing between the waves.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8b9cdd9-b59e-4f2c-ab98-eaec94fa56c4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/coast_c8b9cdd9-b59e-4f2c-ab98-eaec94fa56c4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-shoreline-and-water'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('curved', 'shoreline', 'and', 'water')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        poly('horizon',(6,22),(20,22),(42,22))
        path('shore',(20,22),[('C',(42,6),(28,22),(28,6))]);join('shore','horizon')
        path('near-wave',(6,32),[('C',(24,32),(12,28),(16,36)),('C',(42,32),(32,28),(36,36))])
        path('far-wave',(18,42),[('C',(30,42),(22,41),(26,41)),('C',(42,42),(34,42),(38,42))])
