"""The rejected group has tiny heads and detached doorway-like bodies. Restore larger round heads and a broad foreground bust overlapping the smaller rear person.
Plan: HRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: human_ref/user.svg: circular heads and broad round shoulders; detached head gaps 4 ink.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b1111a7d-0e17-480b-bd48-42a1ccc6d651'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__two-person-group-batch-078/20260929T145934Z-thuan-mac/reference/users_b1111a7d-0e17-480b-bd48-42a1ccc6d651.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='two-person-group-batch-078'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('two', 'person', 'group', 'batch', '078')
    def build(self):

        def path(n,start,steps,closed=False):
            members=[];here=start
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L':self.add_line(m,here,end)
                elif kind=='A':self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(m,here,(args[0],args[1],end))
                members.append(m);here=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry):path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=0):
            if not rad:self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True);return
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        oval('head-front',16,13,5,5);oval('head-back',36,17,5,5)
        path('body-front',(4,40),[('L',(4,36)),('A',(16,26),12,10,True),('A',(28,36),12,10,True),('L',(28,40)),('L',(4,40))],True)
        path('body-back',(28,32),[('C',(36,30),(30,30),(34,30)),('A',(44,36),8,6,True),('L',(44,40)),('L',(28,40))]);join('body-front','body-back')
