"""Round Glasses and Book.

Plan: Reading glasses above closed book; bounds6,6,42,42. Round paired lenses and one page line.
Construction reference: Lucide glasses: paired circles and arched bridge
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0f68711c-573b-484f-8105-ef528e12b59c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/read glasses_0f68711c-573b-484f-8105-ef528e12b59c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'reading-glasses-above-closed-book'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('reading', 'glasses', 'above', 'closed', 'book')

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

        circle('left',14,14,8);circle('right',34,14,8)
        path('bridge',(22,14),[('A',(26,14),2,2,True)]);join('bridge','left');join('bridge','right')
        path('book',(42,30),[('L',(12,30)),('A',(6,36),6,6,False),('A',(12,42),6,6,False),('L',(42,42))])
