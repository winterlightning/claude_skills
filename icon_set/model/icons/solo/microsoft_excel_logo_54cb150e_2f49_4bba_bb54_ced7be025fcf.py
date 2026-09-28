"""A small square with a bold X overlaps the left side of a larger spreadsheet grid with two columns of rows.

Symbol plan: X at left beside a two-column four-row spreadsheet graph. Extremes (4,8)-(44,40).
Review notes: Removes the redundant X tile border. Retains X and the two-column spreadsheet with four equal-height rows. Lucide square informs the grid; all graph intersections are true shared nodes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '54cb150e-2f49-4bba-bb54-ced7be025fcf'
SOURCE_PATH = 'pictographic-primitives/logos/microsoft excel logo_54cb150e-2f49-4bba-bb54-ced7be025fcf.svg'
AUTHOR = 'gpt-6'

class MicrosoftExcelLogo(Solo48):
    icon_id = 'microsoft-excel-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('microsoft-excel', 'excel', 'microsoft', 'spreadsheet', 'office', 'logo', 'brand')

    def build(self):

        def chain(name, *points):
            for i,(start,end) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{i}',start,end)
        def ring(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def rounded(name, left, top, right, bottom, r):
            points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
            members=[]
            for i,start in enumerate(points):
                end=points[(i+1)%8]; ident=f'{name}-{i}'
                if start==end: continue
                if i%2:self.add_arc(ident,start,end,radius_x=r)
                else:self.add_line(ident,start,end)
                members.append(ident)
            self.add_contour(name,*members,closed=True)
        j=(10,24)
        parts=[('x-ul',(4,14),j),('x-lr',j,(16,34)),('x-ll',(4,34),j),('x-ur',j,(16,14))]
        for name,a,b in parts:self.add_line(name,a,b)
        for i,(a,_,__) in enumerate(parts):
            for b,_,__ in parts[i+1:]:self.relate('connect',a,b)
        edges=[]
        xs=(24,34,44);ys=(8,16,24,32,40)
        for i,x in enumerate(xs):
            for j,(a,b) in enumerate(zip(ys,ys[1:])):edges.append((f'col-{i}-{j}',(x,a),(x,b)))
        for j,y in enumerate(ys):
            for i,(a,b) in enumerate(zip(xs,xs[1:])):edges.append((f'row-{j}-{i}',(a,y),(b,y)))
        for name,a,b in edges:self.add_line(name,a,b)
        for i,(a,p,q) in enumerate(edges):
            for b,r,s in edges[i+1:]:
                if {p,q}&{r,s}:self.relate('connect',a,b)
