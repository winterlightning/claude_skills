"""Rejected worker loses furniture outlines and has an oversized ring head. Restore seated pose with chair back, pedestal and laptop over a complete desk. Keep aligned circular head and exactly 4px detached head/body gap.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: human_ref/full_body_ref.png; laptop.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4b08589f-758f-4ceb-88c8-6fb2b68847fc'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__seated-laptop-worker/20260928T173014Z-thuan-mac/reference/desk computer base work laptop sitting user_4b08589f-758f-4ceb-88c8-6fb2b68847fc.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'Preserve the laptop, seated worker, full desk and pedestal chair. The laptop-to-desk and foot-to-desk ink gaps are 2px. Both remain visibly open at 48px; the head/body gap remains exactly 4px and the natural envelope stays 2px inside the canvas. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'fbf7b27ef167898b715eced1a7c45b7a8ac729f7b31b78d548bb8c71b705d132'}
    icon_id='seated-laptop-worker'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('desk', 'computer', 'base', 'work', 'laptop', 'sitting', 'user')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        circle('head',34,8,4)
        line('torso-upper',(34,20),(34,23));line('torso-lower',(34,23),(34,32));join('torso-upper','torso-lower')
        self.mark_human_figure('worker',head='head',torso='torso-upper',torso_junction='start')
        # 20-(8+4)-4=4px visible head-to-body gap, head and upper torso aligned.

        poly('leg',(34,32),(28,32),(24,44));join('leg','torso-lower')
        path('chair',(34,32),[('L',(36,32)),('L',(38,32)),('C',(44,25),(42,32),(44,29)),('L',(44,20))]);join('chair','leg');join('chair','torso-lower')
        line('chair-stem',(36,32),(36,44));join('chair-stem','chair')
        poly('chair-base',(30,44),(36,44),(42,44));join('chair-base','chair-stem')

        poly('desk',(4,30),(6,30),(18,30),(18,44),(4,44),closed=True)

        poly('laptop',(4,12),(8,24),(20,24))
        poly('arm',(34,23),(28,24),(20,24));join('arm','laptop');join('arm','torso-upper');join('arm','torso-lower')


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

