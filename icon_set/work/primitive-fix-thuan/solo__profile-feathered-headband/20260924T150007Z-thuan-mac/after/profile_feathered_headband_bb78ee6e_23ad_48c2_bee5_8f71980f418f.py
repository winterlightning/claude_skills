"""native. Revision: Smooth circular crown and curved jaw, replace stepped nose with a sloping profile, and shape the hanging feather. Retain one band seam; omit facial marks.
Construction: Shared human_ref/user.svg and full_body_ref.png: round head vocabulary; source has continuous profile neck, no detached head gap. Preserve source-facing direction and arrangement.
Keyshape VRECT_L; exact contract extremes, stroke four. No validation exceptions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='bb78ee6e-23ad-48c2-bee5-8f71980f418f'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__profile-feathered-headband/20260924T150007Z-thuan-mac/reference/native_bb78ee6e-23ad-48c2-bee5-8f71980f418f.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='profile-feathered-headband'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('native',)

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

        path('head',(18,44),[('L',(18,34)),('C',(16,26),(18,31),(16,30)),('L',(16,14)),('A',(36,14),10,10,True),('L',(36,20)),('L',(40,25)),('L',(35,26)),('L',(35,31)),('A',(29,37),6,6,True),('L',(27,37)),('L',(27,44))])
        line('band',(16,14),(36,14))
        path('feather',(16,14),[('C',(8,36),(8,21),(8,29)),('C',(16,26),(14,35),(16,31)),('L',(16,14))],True)

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)
