"""Feedback names the monitor. The rejected screen is almost square and its figure is a dot above a narrow arch. Rebuild a broader screen and outlined circular head over smooth broad shoulders, with a centered stand.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: monitor; human_ref/user.svg.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='ec2d4eb4-b488-4b60-b260-7de322e396fd'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__video-conference-monitor/20260928T171322Z-thuan-mac/reference/monitor person_ec2d4eb4-b488-4b60-b260-7de322e396fd.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='video-conference-monitor'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('monitor', 'person')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('screen',(8,4),[('L',(40,4)),('A',(44,8),4,True),('L',(44,32)),('A',(40,36),4,True),('L',(24,36)),('L',(8,36)),('A',(4,32),4,True),('L',(4,8)),('A',(8,4),4,True)],True)
        line('stand',(24,36),(24,44));join('stand','screen')
        poly('base',(16,44),(24,44),(32,44));join('base','stand')
        circle('head',24,14,3)
        path('shoulders',(16,29),[('E',(24,25),8,4,True),('E',(32,29),8,4,True)])
        # Shared human user.svg: circular head; broad shoulders. 25-(14+3)=8 centerline =4 ink gap.


    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            ident=f'{n}-{i}';k,end,*a=c
            if k=='L':self.add_line(ident,start,end)
            elif k=='A':self.add_arc(ident,start,end,radius_x=a[0],sweep=a[1])
            elif k=='E':self.add_arc(ident,start,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif k=='C':self.add_bezier(ident,start,(a[0],a[1],end))
            ids.append(ident);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),[('A',(x+r,y),r,True),('A',(x,y+r),r,True),('A',(x-r,y),r,True),('A',(x,y-r),r,True)],True)
    def box(self,n,l,t,r,b,q):
        self.path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,True),('L',(r,b-q)),('A',(r-q,b),q,True),('L',(l+q,b)),('A',(l,b-q),q,True),('L',(l,t+q)),('A',(l+q,t),q,True)],True)

