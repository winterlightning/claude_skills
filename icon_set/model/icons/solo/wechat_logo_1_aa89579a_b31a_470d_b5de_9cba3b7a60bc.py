"""Wechat logo 1, preserving its complete supplied composition.
Symbol plan: coherent contours, nested identifying symbols and parameterized repeats.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='aa89579a-b31a-470d-b5de-9cba3b7a60bc'
SOURCE_PATH='icon_set/work/todo-references/wechat logo 1_aa89579a-b31a-470d-b5de-9cba3b7a60bc.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='wechat-logo-1'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'logos'
    aliases=()
    keywords=('wechat', 'logo', '1')

    # Visible extrema (2, 6, 46, 42); centerline extremes (4, 8, 44, 40).
    # For CIRCLE the envelope is radial: center (24,24), centerline radius 20.
    def build(self):
        # Two overlapping speech bubbles, exactly as the eye-free supplied logo shows.
        self.add_bezier('rear-lower',(16,30),((14,30),(13,29),(11,29)))
        self.add_line('rear-tail-1',(11,29),(6,33))
        self.add_line('rear-tail-2',(6,33),(7,27))
        self.add_bezier('rear-left',(7,27),((5,25),(4,22),(4,19)))
        self.add_bezier('rear-crown',(4,19),((4,13),(10,8),(18,8)),((26,8),(32,13),(32,18)))
        self.add_contour('rear','rear-lower','rear-tail-1','rear-tail-2','rear-left','rear-crown')
        self.add_bezier('front-crown',(32,18),((39,18),(44,22),(44,28)),((44,31),(42,34),(41,35)))
        self.add_line('front-tail-1',(41,35),(44,40))
        self.add_line('front-tail-2',(44,40),(36,37))
        self.add_bezier('front-base',(36,37),((26,40),(16,36),(16,30)))
        self.add_line('front-left',(16,30),(16,28))
        self.add_bezier('front-upper',(16,28),((16,22),(23,18),(32,18)))
        self.add_contour('front','front-crown','front-tail-1','front-tail-2','front-base','front-left','front-upper',closed=True)
        self.relate('connect','rear','front')


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

