"""Video game logo companion cube.
Symbol plan: Four identical8x8 corner blocks on shared axis24, outer connectors and central mirrored heart. Bounds6..42.
Omissions: Medallion ring and thick connector boxes removed; heart and four corner blocks retained.
Construction references: No useful Lucide exact companion-cube match; supplied reference defines four corners and heart.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='6e798969-b8c1-4108-aa25-07455cf19213'
SOURCE_PATH='pictographic-primitives/_uncategorized_39/video game logo companion cube_6e798969-b8c1-4108-aa25-07455cf19213.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='video-game-logo-companion-cube'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('video', 'game', 'logo', 'companion', 'cube')

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
        for j,(x,y) in enumerate(((6,6),(34,6),(6,34),(34,34))):
            self.add_polyline(f'corner-{j}',(x,y),(x+8,y),(x+8,y+8),(x,y+8),closed=True)
        for n,a,b,c1,c2 in [('top',(14,6),(34,6),0,1),('bottom',(14,42),(34,42),2,3),('left',(6,14),(6,34),0,2),('right',(42,14),(42,34),1,3)]:
            self.add_line(n,a,b);self.relate('connect',n,f'corner-{c1}');self.relate('connect',n,f'corner-{c2}')
        self.path('heart',(24,23),[('A',(18,23),3,3,False),('L',(24,34)),('L',(30,23)),('A',(24,23),3,3,False)],True)
