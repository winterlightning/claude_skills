"""Wheat awn circle exclamation, preserving its complete supplied composition.
Symbol plan: coherent contours, nested identifying symbols and parameterized repeats.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='1e6635a8-8173-444b-b047-ddcc2a5f1d19'
SOURCE_PATH='icon_set/work/todo-references/wheat awn circle exclamation_1e6635a8-8173-444b-b047-ddcc2a5f1d19.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='wheat-awn-circle-exclamation'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('wheat', 'awn', 'circle', 'exclamation')

    # Visible extrema (2, 2, 46, 46); centerline extremes (4, 4, 44, 44).
    # For CIRCLE the envelope is radial: center (24,24), centerline radius 20.
    def build(self):
        # Circular wheat emblem; the source contains no exclamation mark.
        self.circle('ring',24,24,20)
        self.add_bezier('terminal-grain',(24,13),((18,19),(21,23),(24,24)),((27,23),(30,19),(24,13)))
        self.add_contour('grain-top','terminal-grain',closed=True)
        self.add_polyline('stem',(24,24),(24,29),(24,35))
        self.relate('connect','stem','grain-top')
        for row,y in enumerate((23,29)):
            join_y=29+6*row
            for side in (-1,1):
                x=24+side*10; n=f'grain-{row}-{side}'
                self.add_bezier(n,(x,y),((x,y+5),(24+side*4,join_y),(24,join_y)),
                    ((24+side*3,y+1),(24+side*7,y),(x,y)))
                self.add_contour(n+'-outline',n,closed=True)
                self.relate('connect','stem',n+'-outline')


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

