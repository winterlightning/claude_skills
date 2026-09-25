"""Rising Moon with Craters.

Plan: Moon above curving horizon, two broad craters replacing three; bounds6,6,42,42.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f691cb5-2291-494c-bb9b-480b4d6be086'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/moonscape_3f691cb5-2291-494c-bb9b-480b4d6be086.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cratered-moon-rising-behind-curved-horizon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('cratered', 'moon', 'rising', 'behind', 'curved', 'horizon')

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

        path('moon',(10,37),[('C',(6,24),(7,33),(6,29)),('A',(24,6),18,18,True),('A',(42,24),18,18,True),('C',(37,39),(42,31),(40,36))])
        path('horizon',(6,40),[('C',(24,38),(12,37),(17,36)),('C',(42,42),(31,41),(36,42))]);join('horizon','moon')
        circle('crater-a',19,21,3);self.add_dot('crater-b',(31,24))
