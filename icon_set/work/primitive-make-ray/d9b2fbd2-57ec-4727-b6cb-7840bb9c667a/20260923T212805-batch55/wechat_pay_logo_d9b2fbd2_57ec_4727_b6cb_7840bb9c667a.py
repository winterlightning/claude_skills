"""Wechat pay logo, preserving its complete supplied composition.
Symbol plan: coherent contours, nested identifying symbols and parameterized repeats.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d9b2fbd2-57ec-4727-b6cb-7840bb9c667a'
SOURCE_PATH='icon_set/work/todo-references/wechat pay logo_d9b2fbd2-57ec-4727-b6cb-7840bb9c667a.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='wechat-pay-logo'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('wechat', 'pay', 'logo')

    # Visible extrema (2, 6, 46, 42); centerline extremes (4, 8, 44, 40).
    # For CIRCLE the envelope is radial: center (24,24), centerline radius 20.
    def build(self):
        # One broad speech bubble with a checkmark and a lower-left tail.
        self.add_bezier('crown',(4,22),((4,14),(13,8),(24,8)),((35,8),(44,14),(44,22)))
        self.add_bezier('lower',(44,22),((44,30),(35,36),(24,36)),((20,36),(16,35),(13,34)))
        self.add_line('tail-1',(13,34),(4,40))
        self.add_line('tail-2',(4,40),(6,30))
        self.add_bezier('left',(6,30),((5,28),(4,25),(4,22)))
        self.add_contour('bubble','crown','lower','tail-1','tail-2','left',closed=True)
        self.add_polyline('check',(14,21),(21,27),(33,19))


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

