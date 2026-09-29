"""Rounded wallet with a capsule clasp and an occluded right wall.
Reference comparison: Current wallet tab and lower-right corner are lumpy with inconsistent radii. Use a rounded body with an interrupted right wall and a smooth capsule tab.
Construction reference: Lucide wallet: rounded body and continuous tab.
SOLO48 keyshape HRECT_L; uniform 4-unit strokes; explicit coherent symbol ownership.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='91844974-1ccf-5069-b269-c37c2543e7f4'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__money-wallet/20260928T172849Z-thuan-mac/reference/money wallet_91844974-1ccf-5069-b269-c37c2543e7f4.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='money-wallet'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('money', 'wallet')

    def build(self):

        # Typed path helpers own continuous contours, repeated radii and real junctions.
        def path(name,start,commands,closed=False):
            here=start;members=[]
            for i,c in enumerate(commands):
                kind,end,*args=c; ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A':
                    rx,ry,sweep=args
                    self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                elif kind=='C':
                    c1,c2=args
                    self.add_bezier(ident,here,(c1,c2,end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path('body',(40,19),[('L',(40,12)),('A',(36,8),4,4,False),('L',(8,8)),('A',(4,12),4,4,False),('L',(4,36)),('A',(8,40),4,4,False),('L',(36,40)),('A',(40,36),4,4,False),('L',(40,29))])
        path('tab',(33,19),[('L',(41,19)),('A',(44,22),3,3,True),('L',(44,26)),('A',(41,29),3,3,True),('L',(33,29)),('A',(33,19),5,5,True)],True)
        join('body','tab')
