"""dramaturge. Revision: Smooth the profile jaw, sloped beret and broad shoulders; retain continuous neck. Omit tiny hat stem and facial detail.
Construction: Shared human_ref/user.svg: broad smooth shoulders; source profile uses continuous neck rather than detached avatar construction. Preserve source-facing direction and arrangement.
Keyshape VRECT_L; exact contract extremes, stroke four. No validation exceptions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='a8991616-b410-40cd-bdbc-7c97585a5607'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__profile-person-wearing-slanted-beret/20260924T150007Z-thuan-mac/reference/dramaturge_a8991616-b410-40cd-bdbc-7c97585a5607.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='profile-person-wearing-slanted-beret'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('dramaturge',)

    def build(self):
        # Each contour owns its shape. Repeated parts share dimensions and axes.
        def path(n,start,steps,closed=False):
            p=start; members=[]
            for j,s in enumerate(steps):
                k=f'{n}-{j}';kind,q,*v=s
                if kind=='L': self.add_line(k,p,q)
                elif kind=='A': self.add_arc(k,p,q,radius_x=v[0],radius_y=v[1],sweep=v[2])
                elif kind=='C': self.add_bezier(k,p,(v[0],v[1],q))
                members.append(k);p=q
            self.add_contour(n,*members,closed=closed)
        def line(n,a,b):self.add_line(n,a,b)
        def poly(n,*p):self.add_polyline(n,*p)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def join(a,b):self.relate('connect',a,b)

        path('hat',(10,16),[('C',(29,4),(10,7),(23,4)),('C',(36,12),(37,4),(40,8)),('L',(10,16))],True)
        path('face',(36,12),[('L',(36,21)),('L',(40,27)),('L',(34,28)),('L',(34,30)),('A',(28,36),6,6,True),('L',(27,36)),('L',(27,38)),('C',(40,44),(34,38),(40,40))])
        path('back',(10,16),[('L',(10,23)),('C',(18,34),(10,28),(14,32)),('L',(18,38)),('C',(8,44),(12,38),(8,40))])

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)
