"""Rejected tube lacks an eyepiece and objective; the support is a disconnected large hook. Restore eyepiece, tube, objective, curved arm, stage and pedestal."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='101aaf57-5431-5ae4-a7e5-f05c16647c10'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__laboratory-microscope-101aaf57-solo/20260929T041010Z-thuan-mac/reference/microscope_101aaf57-5431-5ae4-a7e5-f05c16647c10.svg'
AUTHOR='gpt-6'
PLAN='Rejected tube lacks an eyepiece and objective; the support is a disconnected large hook. Restore eyepiece, tube, objective, curved arm, stage and pedestal.'
CONSTRUCTION_REFERENCE='No useful subject-specific Lucide match; original reference determines the silhouette.'
OMISSIONS='Only insignificant source detail omitted.'
class Drawing(Solo48):
    icon_id='laboratory-microscope-101aaf57-solo'
    keyshape=Keyshape.VRECT_L
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
        self.add_polyline('tube',(24,10),(32,14),(23,29),(15,25),closed=True)
        self.add_polyline('eyepiece',(26,11),(30,4),(36,8),(32,14))
        self.add_line('objective',(19,27),(16,32))
        self.path('support',(32,16),[('C',(34,37),(44,21),(43,32)),('C',(24,39),(31,40),(27,40)),('L',(22,44))])
        self.add_line('stage',(8,34),(25,34))
        self.add_line('base',(14,44),(40,44))
        self.relate('connect','tube','eyepiece','objective','support'); self.relate('connect','support','base')
