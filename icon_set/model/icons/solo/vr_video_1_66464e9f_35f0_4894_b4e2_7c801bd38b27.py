"""Vr video 1.
Symbol plan: Upper-left stylus and cube meet foreground goggles at explicit occlusion endpoints; paired lens dots. Bounds6,6..42,42.
Omissions: Stylus double outline, headset extra rim and nose notch removed; lens rings reduced to dots.
Construction references: Lucide box original/atomic-debug: three-dimensional faces with shared vertices; source establishes headset foreground.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='66464e9f-35f0-4894-b4e2-7c801bd38b27'
SOURCE_PATH='pictographic-primitives/_uncategorized_39/vr video 1_66464e9f-35f0-4894-b4e2-7c801bd38b27.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='vr-video-1'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('vr', 'video', '1')

    def path(self,n,start,ops,closed=False):
        at=start; members=[]
        for i,op in enumerate(ops):
            kind,end,*args=op
            if at==end: continue
            m=f'{n}-{i}'
            if kind=='L': self.add_line(m,at,end)
            elif kind=='A': self.add_arc(m,at,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            else: self.add_bezier(m,at,(args[0],args[1],end))
            members.append(m);at=end
        if closed and at!=start:
            self.add_line(n+'-close',at,start);members.append(n+'-close')
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def rect(self,n,l,t,r,b,k=4,top=(),right=(),bottom=(),left=()):
        ops=[('L',(x,t)) for x in sorted(top) if l+k<x<r-k]
        ops += [('L',(r-k,t)),('A',(r,t+k),k,k,True)]
        ops += [('L',(r,y)) for y in sorted(right) if t+k<y<b-k]
        ops += [('L',(r,b-k)),('A',(r-k,b),k,k,True)]
        ops += [('L',(x,b)) for x in sorted(bottom,reverse=True) if l+k<x<r-k]
        ops += [('L',(l+k,b)),('A',(l,b-k),k,k,True)]
        ops += [('L',(l,y)) for y in sorted(left,reverse=True) if t+k<y<b-k]
        ops += [('L',(l,t+k)),('A',(l+k,t),k,k,True)]
        self.path(n,(l+k,t),ops,True)

    def build(self):
        # Cube is behind the goggles; visible edges terminate at actual frame nodes.
        self.add_polyline('cube-top',(6,16),(12,12),(18,8),(30,16),(18,24),closed=True)
        self.add_polyline('cube-left',(6,16),(6,32),(14,36));self.relate('connect','cube-top','cube-left')
        self.add_line('stylus',(6,6),(12,12));self.relate('connect','stylus','cube-top')
        self.rect('headset',14,24,42,42,4,top=(18,),left=(36,))
        self.relate('connect','cube-top','headset');self.relate('connect','cube-left','headset')
        for j,x in enumerate((23,33)):self.add_dot(f'lens-{j}',(x,33))
