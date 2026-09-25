"""head eye. Revision: Use a circular crown and a wider almond eye, smooth nose and jaw. Omit pupil to preserve eye opening.
Construction: Shared human_ref/user.svg: circular head construction; continuous profile neck, no detached body. Preserve source-facing direction and arrangement.
Keyshape VRECT_L; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6c300321-ec3d-4d40-b58f-a6b8a1dcd2dc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-020/references/49-6c300321-ec3d-4d40-b58f-a6b8a1dcd2dc.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='profile-head-almond-eye'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'symbol'
    aliases=()
    keywords=('head', 'eye')

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

        path('head',(14,42),[('L',(14,34)),('C',(6,22),(14,30),(6,29)),('A',(38,22),16,16,True),('L',(42,30)),('L',(34,30)),('L',(34,34)),('A',(28,40),6,6,True),('L',(28,42))])
        path('eye',(16,21),[('C',(28,21),(20,15),(24,15)),('C',(16,21),(24,27),(20,27))],True)

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)
