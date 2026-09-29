"""Rejected worker loses furniture outlines and has an oversized ring head. Restore standing pose and pen and two document marks over a complete desk. Keep aligned circular head and exactly 4px detached head/body gap.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: human_ref/full_body_ref.png; pen-line.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='6b40dc1d-d719-46f6-87c3-95cd2d0dd7ee'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__standing-person-writing-at-desk/20260928T173014Z-thuan-mac/reference/desk document base work standing user_6b40dc1d-d719-46f6-87c3-95cd2d0dd7ee.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'Preserve the pen, two document marks, complete desk and standing worker. Pen contact is intentional; the separate arm passes about 1px above the desk edge and remains visibly clear in both themes. The head/body ink gap is exactly 4px. Natural envelope remains inside the canvas. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'b638df53cb4ac547ebbc1eaf15134f5eb9fd209a733afae7a454cb8da8db8f51'}
    icon_id='standing-person-writing-at-desk'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('desk', 'document', 'base', 'work', 'standing', 'user')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        circle('head',36,8,4)
        line('torso-upper',(36,20),(36,23));line('torso-lower',(36,23),(36,32));join('torso-upper','torso-lower')
        self.mark_human_figure('worker',head='head',torso='torso-upper',torso_junction='start')
        # 20-(8+4)-4=4px visible head-to-body gap, head and upper torso aligned.

        poly('legs',(32,44),(36,32),(42,44));join('legs','torso-lower')

        poly('desk',(4,30),(6,30),(18,30),(24,30),(24,44),(4,44),closed=True)

        poly('arm',(36,23),(28,26),(20,24));join('arm','torso-upper');join('arm','torso-lower')
        poly('pen',(22,18),(20,24),(18,30));join('pen','arm');join('pen','desk')
        line('text-one',(4,8),(12,8));line('text-two',(4,16),(12,16))


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

