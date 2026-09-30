"""Rejected case has sharp corners and merges into its conveyor. Round suitcase and handle, separate belt below, and preserve two straps.
Plan: SQUARE envelope; preserve source arrangement with coherent connected contours.
References: original and rejected SVGs visually compared before drawing.
Lucide apple/leaf for fruit and leaves, luggage for rounded case and straps,
scissors for crossing blades and loops, hand for rounded fingertips.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='c4455d4c-79af-42dd-8eec-2199e03f8d83'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__strapped-suitcase-above-a-conveyor/20260929T130116Z-thuan-mac/reference/baggage line_c4455d4c-79af-42dd-8eec-2199e03f8d83.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='strapped-suitcase-above-a-conveyor'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('baggage', 'line')
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for i,step in enumerate(steps):
                kind,end,*args=step; ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end; members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def join(a,b): self.relate('connect',a,b)

        def box(name,l,t,r,b,rad=0):
            if rad==0:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
            else:
                path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        box('case',8,12,40,27,3)
        path('handle',(17,12),[('L',(17,8)),('A',(21,4),4,4,True),('L',(27,4)),('A',(31,8),4,4,True),('L',(31,12))]);join('handle','case')
        for x in (17,31):self.add_line(f'strap-{x}',(x,12),(x,27));join(f'strap-{x}','case')
        path('belt',(40,36),[('L',(12,36)),('A',(12,44),4,4,False),('L',(40,44))])
