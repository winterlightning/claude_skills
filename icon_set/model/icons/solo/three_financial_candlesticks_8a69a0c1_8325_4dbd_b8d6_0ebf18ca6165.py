"""Financial Candlestick Trading Chart.

Plan: Three identical width candle bodies at stepped heights, real center wick attachments. Bounds4,8,44,40.
Construction reference: chart-candlestick.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a69a0c1-8325-4dbd-b8d6-0ebf18ca6165'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/candles chart_8a69a0c1-8325-4dbd-b8d6-0ebf18ca6165.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-financial-candlesticks'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('three', 'financial', 'candlesticks')

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

        for j,(x,y) in enumerate([(4,24),(20,16),(36,8)]):
         poly(f'body-{j}',(x,y+4),(x+4,y+4),(x+8,y+4),(x+8,y+12),(x+4,y+12),(x,y+12),closed=True)
         line(f'top-{j}',(x+4,y),(x+4,y+4));line(f'bottom-{j}',(x+4,y+12),(x+4,y+16));join(f'body-{j}',f'top-{j}');join(f'body-{j}',f'bottom-{j}')
