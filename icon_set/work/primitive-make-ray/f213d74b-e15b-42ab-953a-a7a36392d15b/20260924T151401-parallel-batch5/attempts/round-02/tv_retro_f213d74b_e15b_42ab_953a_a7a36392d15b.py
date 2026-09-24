"""Tv retro.
Symbol plan: Nested rounded screen and cabinet; two vertically repeated controls; centered rabbit ears. Extremes4,8 to44,40.
Omissions: Feet and outlined control rings removed to make space for screen and controls.
Construction references: Lucide tv: centered rabbit-ear junction and rounded cabinet.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='f213d74b-e15b-42ab-953a-a7a36392d15b'
SOURCE_PATH='pictographic-primitives/_uncategorized_39/tv retro_f213d74b-e15b-42ab-953a-a7a36392d15b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='tv-retro'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('tv', 'retro')

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
        self.rect('cabinet',4,12,44,40,4,top=(24,))
        self.add_polyline('antenna',(16,8),(24,12),(32,8));self.relate('connect','antenna','cabinet')
        self.rect('screen',13,21,26,31,3)
        for j,y in enumerate((22,31)):self.add_dot(f'button-{j}',(35,y))
