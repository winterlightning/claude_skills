"""Rejected bicycle has tiny wheels and a dense blocky frame. Restore two large thin-rim wheels, an open diamond frame, saddle and dropped road handlebar."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='b43a6544-1e7b-481a-aad7-01ad2bdb307d'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__road-bicycle/20260929T044747Z-thuan-mac/reference/bicycle_b43a6544-1e7b-481a-aad7-01ad2bdb307d.svg'
AUTHOR='gpt-6'
PLAN='Rejected bicycle has tiny wheels and a dense blocky frame. Restore two large thin-rim wheels, an open diamond frame, saddle and dropped road handlebar.'
CONSTRUCTION_REFERENCE='Lucide bike original and atomic-debug: true circular wheels and diagonal structural strokes; source owns road-bike geometry.'
OMISSIONS='Secondary source detail simplified only where needed for 48 px legibility.'
class Drawing(Solo48):
    icon_id='road-bicycle'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def path(self,n,start,commands,closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid); here=end
        self.add_contour(n,*ids,closed=closed)
    def box(self,n,l,t,r,b,rad=3):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):
        self.circle('rear-wheel',11,33,7);self.circle('front-wheel',37,33,7)
        self.add_polyline('frame',(11,33),(20,19),(31,19),(23,33),(11,33))
        self.add_line('seat-tube',(18,12),(23,33));self.add_line('saddle',(15,12),(23,12))
        self.add_line('fork',(29,8),(37,33));self.path('bars',(29,8),[('L',(36,8)),('A',(40,12),4,4,True),('L',(40,14))])
        self.relate('connect','frame','rear-wheel','seat-tube','fork');self.relate('connect','fork','front-wheel','bars');self.relate('connect','seat-tube','saddle')
