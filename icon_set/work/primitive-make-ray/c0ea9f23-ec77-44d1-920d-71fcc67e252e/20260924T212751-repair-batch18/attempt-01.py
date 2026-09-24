"""Wedding celebration, preserving its complete supplied composition.
Symbol plan: coherent contours, nested identifying symbols and parameterized repeats.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='c0ea9f23-ec77-44d1-920d-71fcc67e252e'
SOURCE_PATH = 'pictographic-primitives/romance/wedding celebration_c0ea9f23-ec77-44d1-920d-71fcc67e252e.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='wedding-celebration'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('wedding', 'celebration')

    # Visible extrema (4, 4, 44, 44); centerline extremes (6, 6, 42, 42).
    # For CIRCLE the envelope is radial: center (24,24), centerline radius 20.
    def build(self):
        # Three bunting flags above two overlapping hearts.
        self.add_polyline('cord',(6,6),(10,7),(18,8),(21,9),(29,9),(32,9),(40,8),(42,8))
        for i,points in enumerate([((10,7),(13,14),(18,8)),((21,9),(25,14),(29,9)),((32,9),(36,15),(40,8))]):
            self.add_polyline(f'flag-{i}',*points)
            self.relate('connect','cord',f'flag-{i}')
        self.add_bezier('rear-heart',(32,29),((32,22),(24,20),(20,26)),
            ((16,20),(6,22),(6,29)),((6,33),(12,37),(18,39)))
        self.add_line('rear-heart-end',(18,39),(24,35))
        self.add_contour('heart-back','rear-heart','rear-heart-end')
        self.add_bezier('heart-front',(24,35),((23,34),(22,32),(22,30)),
            ((22,24),(29,24),(32,29)),((35,24),(42,24),(42,30)),
            ((42,35),(35,40),(32,42)),((29,40),(26,38),(24,35)))
        self.add_contour('heart-front-outline','heart-front',closed=True)
        self.relate('connect','heart-back','heart-front-outline')


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

