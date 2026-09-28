"""Shabbat Candles and Challah Bread.

Plan: Retained both candles, both flame marks, the shared holder and the adjacent loaf. Narrow candle bodies and flames become strokes; the loaf scores are omitted.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '592d01da-42b5-4d10-a3c2-5fef9f0cdb51'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/candle bread_592d01da-42b5-4d10-a3c2-5fef9f0cdb51.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'paired-candles-beside-loaf'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('paired', 'candles', 'beside', 'loaf')

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

        for x in (6,18):
         line('flame-'+str(x),(x,6),(x,8));line('candle-'+str(x),(x,17),(x,26))
        path('holder',(6,26),[('A',(12,32),6,6,False),('A',(18,26),6,6,False)])
        join('holder','candle-6');join('holder','candle-18');line('stem',(12,32),(12,42));line('foot',(6,42),(18,42));join('stem','holder');join('stem','foot')
        path('loaf',(28,42),[('L',(28,32)),('A',(34,26),6,6,True),('L',(36,26)),('A',(42,32),6,6,True),('L',(42,42)),('L',(28,42))],True)
