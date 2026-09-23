"""Zcool logo, preserving its complete supplied composition.
Symbol plan: coherent contours, nested identifying symbols and parameterized repeats.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='14555301-7f11-43db-978e-a383d12a3b27'
SOURCE_PATH='icon_set/work/todo-references/zcool logo_14555301-7f11-43db-978e-a383d12a3b27.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='zcool-logo'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('zcool', 'logo')

    # Visible extrema (4, 4, 44, 44); centerline extremes (6, 6, 42, 42).
    # For CIRCLE the envelope is radial: center (24,24), centerline radius 20.
    def build(self):
        # Three flame tips over a round lower bowl with an independently drawn Z.
        self.add_bezier('flame-upper',(30,6),((30,11),(29,14),(28,17)),
            ((34,17),(38,14),(40,12)),((40,18),(38,23),(36,26)),((38,27),(40,27),(42,26)),
            ((41,30),(39,33),(37,34)),((36,40),(30,42),(24,42)))
        self.add_bezier('flame-lower',(24,42),((12,42),(6,38),(6,26)),
            ((6,18),(12,12),(21,11)),((25,10),(28,8),(30,6)))
        self.add_contour('flame','flame-upper','flame-lower',closed=True)
        self.add_polyline('z',(17,25),(25,25),(17,33),(25,33))


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

