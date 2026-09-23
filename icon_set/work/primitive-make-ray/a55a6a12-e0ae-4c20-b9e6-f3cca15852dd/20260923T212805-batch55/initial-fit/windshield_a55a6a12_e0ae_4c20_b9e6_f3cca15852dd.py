"""Windshield, preserving its complete supplied composition.
Symbol plan: coherent contours, nested identifying symbols and parameterized repeats.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='a55a6a12-e0ae-4c20-b9e6-f3cca15852dd'
SOURCE_PATH='icon_set/work/todo-references/windshield_a55a6a12-e0ae-4c20-b9e6-f3cca15852dd.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='windshield'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('windshield',)

    # Visible extrema (2, 8, 46, 40); centerline extremes (4, 10, 44, 38).
    # For CIRCLE the envelope is radial: center (24,24), centerline radius 20.
    def build(self):
        # Curved windshield: arched top, leaning sides and concave lower edge.
        self.add_bezier('upper-left',(8,12),((12,11),(18,10),(24,10)))
        self.add_bezier('upper-right',(24,10),((30,10),(36,11),(40,12)),((43,13),(44,14),(44,16)))
        self.add_line('right',(44,16),(40,35))
        self.add_bezier('lower-right',(40,35),((40,37),(39,38),(38,38)),((34,38),(30,36),(24,36)))
        self.add_bezier('lower-left',(24,36),((18,36),(14,38),(10,38)),((9,38),(8,37),(8,35)))
        self.add_line('left',(8,35),(4,16))
        self.add_bezier('upper-corner',(4,16),((4,14),(5,13),(8,12)))
        self.add_contour('windshield','upper-left','upper-right','right','lower-right','lower-left','left','upper-corner',closed=True)


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

