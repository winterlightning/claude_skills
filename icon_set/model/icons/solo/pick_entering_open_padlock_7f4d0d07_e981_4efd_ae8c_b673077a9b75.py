"""crime tools loackpick unlock. Revision: Straighten pick toward lock, lengthen keyhole mark and smooth grip. Preserve open shackle and partially occluded housing.
Construction: Lucide lock-open: arched shackle and rounded housing. Preserve source-facing direction and arrangement.
Keyshape SQUARE; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7f4d0d07-e981-4efd-ae8c-b673077a9b75'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_13/crime tools loackpick unlock_7f4d0d07-e981-4efd-ae8c-b673077a9b75.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='pick-entering-open-padlock'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('crime', 'tools', 'loackpick', 'unlock')

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

        path('lock',(24,24),[('L',(38,24)),('A',(42,28),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(31,42))])
        path('shackle',(24,24),[('L',(24,15)),('A',(42,15),9,9,True)])
        path('handle',(8,33),[('L',(12,30)),('A',(19,31),5,5,True),('A',(18,38),5,5,True),('L',(14,41)),('A',(8,33),5,5,True)],True)
        poly('pick',(19,31),(25,33),(31,33))

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)
