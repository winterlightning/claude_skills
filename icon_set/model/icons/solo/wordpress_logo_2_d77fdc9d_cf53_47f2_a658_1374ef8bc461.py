"""Wordpress logo 2, preserving its complete supplied composition.
Symbol plan: coherent contours, nested identifying symbols and parameterized repeats.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='d77fdc9d-cf53-47f2-a658-1374ef8bc461'
SOURCE_PATH='icon_set/work/todo-references/wordpress logo 2_d77fdc9d-cf53-47f2-a658-1374ef8bc461.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='wordpress-logo-2'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('wordpress', 'logo', '2')

    # Visible extrema (2, 6, 46, 42); centerline extremes (4, 8, 44, 40).
    # For CIRCLE the envelope is radial: center (24,24), centerline radius 20.
    def build(self):
        # Hand-authored serif W, preserving the standalone WordPress letterform.
        self.add_polyline('w',(8,8),(16,40),(24,8),(32,38),(40,8))
        for i,x in enumerate((8,24,40)):
            self.add_polyline(f'serif-{i}',(x-4,8),(x,8),(x+4,8))
            self.relate('connect','w',f'serif-{i}')


    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def path(self,n,start,segments,closed=False):
        at=start; members=[]
        for i,s in enumerate(segments):
            eid=f'{n}-{i}'; kind,end,*args=s
            if end==at: continue
            if kind=='L': self.add_line(eid,at,end)
            else: self.add_arc(eid,at,end,radius_x=args[0],sweep=args[1] if len(args)>1 else True)
            at=end; members.append(eid)
        self.add_contour(n,*members,closed=closed)

    def rect(self,n,l,t,r,b,k=4,top=(),right=(),bottom=(),left=()):
        # Shared rectangle parameters own radii, symmetry and attachment nodes.
        seg=[('L',(x,t)) for x in sorted(set(top)) if l+k<x<r-k]
        seg += [('L',(r-k,t)),('A',(r,t+k),k)]
        seg += [('L',(r,y)) for y in sorted(set(right)) if t+k<y<b-k]
        seg += [('L',(r,b-k)),('A',(r-k,b),k)]
        seg += [('L',(x,b)) for x in sorted(set(bottom),reverse=True) if l+k<x<r-k]
        seg += [('L',(l+k,b)),('A',(l,b-k),k)]
        seg += [('L',(l,y)) for y in sorted(set(left),reverse=True) if t+k<y<b-k]
        seg += [('L',(l,t+k)),('A',(l+k,t),k)]
        self.path(n,(l+k,t),seg,True)

    def shoulders(self,n,l,x,r,top,bottom):
        self.add_arc(n+'-left',(l,bottom),(x,top),radius_x=x-l,radius_y=bottom-top)
        self.add_arc(n+'-right',(x,top),(r,bottom),radius_x=r-x,radius_y=bottom-top)
        self.add_contour(n,n+'-left',n+'-right')

