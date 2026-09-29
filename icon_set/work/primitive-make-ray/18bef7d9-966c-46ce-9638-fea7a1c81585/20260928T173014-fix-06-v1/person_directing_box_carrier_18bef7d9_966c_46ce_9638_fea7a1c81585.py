"""Rejected people collapse into a tangled angular shape. Restore two distinct full-body figures, a visible carried box and a separate pointing arm.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: human_ref/full_body_ref.png; person-standing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='18bef7d9-966c-46ce-9638-fea7a1c81585'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-directing-box-carrier/20260928T173014Z-thuan-mac/reference/worker lay off fired user finger box_18bef7d9-966c-46ce-9638-fea7a1c81585.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='person-directing-box-carrier'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('worker', 'lay', 'off', 'fired', 'user', 'finger', 'box')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        circle('carrier-head',18,8,3);circle('director-head',36,6,3)
        line('carrier-upper',(18,19),(18,21));line('carrier-lower',(18,21),(18,30));join('carrier-upper','carrier-lower')
        poly('carrier-arm',(18,21),(12,24));join('carrier-arm','carrier-upper');join('carrier-arm','carrier-lower')
        poly('box',(4,24),(12,24),(12,32),(4,32),closed=True);join('box','carrier-arm')
        poly('carrier-legs',(13,44),(18,30),(23,44));join('carrier-legs','carrier-lower')
        line('director-upper',(36,17),(36,19));line('director-middle',(36,19),(36,21));line('director-lower',(36,21),(36,30));join('director-upper','director-middle');join('director-middle','director-lower')
        line('point',(36,19),(25,19));join('point','director-upper');join('point','director-middle')
        line('director-arm',(36,21),(44,28));join('director-arm','director-middle');join('director-arm','director-lower')
        poly('director-legs',(31,44),(36,30),(43,44));join('director-legs','director-lower')
        self.mark_human_figure('carrier',head='carrier-head',torso='carrier-upper',torso_junction='start')
        self.mark_human_figure('director',head='director-head',torso='director-upper',torso_junction='start')
        # 19-(8+3)-4=4 and 17-(6+3)-4=4 visible head/body gaps.


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

