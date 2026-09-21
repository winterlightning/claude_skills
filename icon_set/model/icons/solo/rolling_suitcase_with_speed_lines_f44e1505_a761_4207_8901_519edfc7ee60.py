"""Fast Moving Travel Luggage.

Plan: Tall suitcase, handle and rolling supports; bounds6,6,42,42. Two side trails; omit face grooves for clear native size.
Construction reference: luggage.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f44e1505-a761-4207-8901-519edfc7ee60'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/baggage roll_f44e1505-a761-4207-8901-519edfc7ee60.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rolling-suitcase-with-speed-lines'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('rolling', 'suitcase', 'with', 'speed', 'lines')

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
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        poly('case',(22,18),(26,18),(34,18),(42,18),(42,36),(22,36),closed=True)
        poly('handle',(26,18),(26,6),(34,6),(34,18));join('handle','case')
        line('wheel-left',(26,36),(26,42));line('wheel-right',(38,36),(38,42));join('wheel-left','case');join('wheel-right','case')
        line('trail-top',(6,24),(12,24));line('trail-low',(6,36),(12,36))
