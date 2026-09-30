"""Rejected dollop was flattened and nozzle reduced to a line. Restore a fuller rounded icing mound and an outlined taper.
Plan: SQUARE envelope; preserve source arrangement with coherent connected contours.
References: original and rejected SVGs visually compared before drawing.
Lucide apple/leaf for fruit and leaves, luggage for rounded case and straps,
scissors for crossing blades and loops, hand for rounded fingertips.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='aff563ce-3eaf-4937-9894-dfe356ba0aa4'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__piping-nozzle-above-icing-dollop/20260929T130116Z-thuan-mac/reference/cookies decirating 2_aff563ce-3eaf-4937-9894-dfe356ba0aa4.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='piping-nozzle-above-icing-dollop'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('cookies', 'decirating', '2')
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

        self.add_polyline('nozzle',(30,6),(42,10),(30,22),(22,16),closed=True)
        path('icing',(6,36),[('C',(14,29),(6,32),(10,29)),('C',(20,26),(15,26),(18,26)),('C',(27,32),(20,30),(23,31)),('C',(32,37),(30,33),(32,35)),('C',(19,42),(32,41),(25,42)),('C',(6,36),(10,42),(6,41))],True)
