"""Rejected worker loses furniture outlines and has an oversized ring head. Restore standing pose and side-view desktop monitor over a complete desk. Keep aligned circular head and exactly 4px detached head/body gap.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: human_ref/full_body_ref.png; monitor.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='2fd37035-c393-4771-b96f-502ab4be6f36'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__standing-desktop-computer-worker/20260928T173014Z-thuan-mac/reference/desk computer base work standing user_2fd37035-c393-4771-b96f-502ab4be6f36.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='standing-desktop-computer-worker'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('desk', 'computer', 'base', 'work', 'standing', 'user')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        circle('head',36,8,4)
        line('torso-upper',(36,20),(36,23));line('torso-lower',(36,23),(36,32));join('torso-upper','torso-lower')
        self.mark_human_figure('worker',head='head',torso='torso-upper',torso_junction='start')
        # 20-(8+4)-4=4px visible head-to-body gap, head and upper torso aligned.

        poly('legs',(32,44),(36,32),(42,44));join('legs','torso-lower')

        poly('desk',(4,30),(6,30),(18,30),(24,30),(24,44),(4,44),closed=True)

        poly('arm',(36,23),(28,27),(22,27),(24,30));join('arm','torso-upper');join('arm','torso-lower');join('arm','desk')
        poly('monitor',(8,4),(12,16),(14,22))
        path('monitor-stand',(12,16),[('C',(6,30),(7,16),(6,20))]);join('monitor-stand','monitor');join('monitor-stand','desk')


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

