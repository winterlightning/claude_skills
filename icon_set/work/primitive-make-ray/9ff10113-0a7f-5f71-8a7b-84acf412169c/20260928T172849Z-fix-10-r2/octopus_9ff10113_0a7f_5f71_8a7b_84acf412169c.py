"""Smooth dome and four visible sweeping tentacles, mirrored about x=24.
Reference comparison: Current octopus has sharp shoulders and bent tentacle joins. Rebuild a smooth dome and sweeping paired arms, preserving the four visible arm strokes.
Construction reference: No useful exact Lucide match; shared smooth curve construction.
SOLO48 keyshape HRECT_L; uniform 4-unit strokes; explicit coherent symbol ownership.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='9ff10113-0a7f-5f71-8a7b-84acf412169c'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__octopus/20260928T172849Z-thuan-mac/reference/octopus_9ff10113-0a7f-5f71-8a7b-84acf412169c.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='octopus'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('octopus',)

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
        path('body',(4,26),[('C',(14,27),(4,32),(11,32)),('C',(12,20),(14,25),(12,24)),('A',(36,20),12,12,True),('C',(34,27),(36,24),(34,25)),('C',(44,26),(37,32),(44,32))])
        path('left-arm',(19,34),[('C',(8,40),(17,38),(14,40))])
        path('right-arm',(29,34),[('C',(40,40),(31,38),(34,40))])
