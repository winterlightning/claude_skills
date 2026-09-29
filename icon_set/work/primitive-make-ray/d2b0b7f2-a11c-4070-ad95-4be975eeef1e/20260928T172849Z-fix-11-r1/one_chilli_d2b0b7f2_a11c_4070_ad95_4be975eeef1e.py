"""An asymmetrical tapered chilli with a continuous curved stalk.
Reference comparison: Current chilli has a lumpy shoulder and abrupt stalk junction. Rebuild a flowing tapered pepper body and curved stalk.
Construction reference: No useful exact match; natural asymmetric silhouette.
SOLO48 keyshape HRECT_L; uniform 4-unit strokes; explicit coherent symbol ownership.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d2b0b7f2-a11c-4070-ad95-4be975eeef1e'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__one-chilli/20260928T172849Z-thuan-mac/reference/one chilli_d2b0b7f2-a11c-4070-ad95-4be975eeef1e.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='one-chilli'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('one', 'chilli')

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
        path('pepper',(4,27),[('C',(31,18),(15,32),(23,20)),('C',(39,22),(34,16),(39,18)),('C',(24,40),(43,32),(31,40)),('C',(4,27),(14,40),(7,35))],True)
        path('stem',(37,18),[('C',(44,8),(43,18),(44,12))]);join('stem','pepper')
