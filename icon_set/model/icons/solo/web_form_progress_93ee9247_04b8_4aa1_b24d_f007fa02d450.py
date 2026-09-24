"""Web form progress, preserving its complete supplied composition.
Symbol plan: coherent contours, nested identifying symbols and parameterized repeats.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='93ee9247-04b8-4aa1-b24d-f007fa02d450'
SOURCE_PATH='icon_set/work/todo-references/web form progress_93ee9247-04b8-4aa1-b24d-f007fa02d450.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='web-form-progress'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('web', 'form', 'progress')

    # Visible extrema (2, 8, 46, 40); centerline extremes (4, 10, 44, 38).
    # For CIRCLE the envelope is radial: center (24,24), centerline radius 20.
    def build(self):
        # Two circular nodes, connecting line and central X; preserve the thin-row aspect.
        # This aspect cannot fill the minimum-height SOLO48 horizontal keyshape.
        self.circle('left-node',10,24,6)
        self.circle('right-node',38,24,6)
        self.add_polyline('connector',(16,24),(24,24),(32,24))
        self.add_polyline('cross-a',(20,20),(24,24),(28,28))
        self.add_polyline('cross-b',(20,28),(24,24),(28,20))
        self.relate('connect','left-node','connector')
        self.relate('connect','right-node','connector')
        self.relate('connect','connector','cross-a','cross-b')


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

