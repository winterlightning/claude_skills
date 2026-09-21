"""Hand Dropping Coin into Cup.

Plan: SQUARE, centerline extremes (6, 6, 42, 42); 48 x 48, stroke 4.
The pinched coin remains visible above the cup. The cup and coin keep a clear gap.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: hand-coins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b756b0fb-ba2c-4349-bad0-de1ee11adb74'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/begging cup give coin_b756b0fb-ba2c-4349-bad0-de1ee11adb74.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-lowering-a-coin-toward-a-cup'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('hand', 'lowering', 'a', 'coin', 'toward', 'a', 'cup')

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

        poly('cup',(20,30),(42,30),(38,42),(24,42),closed=True)
        circle('coin',32,18,4)
        path('hand',(6,6),[('L',(20,6)),('C',(30,14),(26,6),(28,10)),('L',(24,14)),('L',(20,18)),('L',(6,14))]);join('coin','hand')
