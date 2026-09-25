"""Workflow data table increasing arrow.
Symbol plan: Rising zigzag arrow above a stepped table; rows have pitch8 and columns9/10. Bounds6..42.
Omissions: Four source rows reduced to two; stepped upper-left table corner retained.
Construction references: Lucide chart-no-axes-combined: one rising stroke and clear data geometry; source table and arrow arrangement retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='bd44c072-c5cf-4191-b2b0-3681a58f3a3a'
SOURCE_PATH='pictographic-primitives/_uncategorized_40/workflow data table increasing arrow_bd44c072-c5cf-4191-b2b0-3681a58f3a3a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='workflow-data-table-increasing-arrow'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('workflow', 'data', 'table', 'increasing', 'arrow')

    def path(self,n,start,ops,closed=False):
        at=start; members=[]
        for i,op in enumerate(ops):
            kind,end,*args=op
            if at==end: continue
            m=f'{n}-{i}'
            if kind=='L': self.add_line(m,at,end)
            elif kind=='A': self.add_arc(m,at,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            else: self.add_bezier(m,at,(args[0],args[1],end))
            members.append(m);at=end
        if closed and at!=start:
            self.add_line(n+'-close',at,start);members.append(n+'-close')
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def rect(self,n,l,t,r,b,k=4,top=(),right=(),bottom=(),left=()):
        ops=[('L',(x,t)) for x in sorted(top) if l+k<x<r-k]
        ops += [('L',(r-k,t)),('A',(r,t+k),k,k,True)]
        ops += [('L',(r,y)) for y in sorted(right) if t+k<y<b-k]
        ops += [('L',(r,b-k)),('A',(r-k,b),k,k,True)]
        ops += [('L',(x,b)) for x in sorted(bottom,reverse=True) if l+k<x<r-k]
        ops += [('L',(l+k,b)),('A',(l,b-k),k,k,True)]
        ops += [('L',(l,y)) for y in sorted(left,reverse=True) if t+k<y<b-k]
        ops += [('L',(l,t+k)),('A',(l+k,t),k,k,True)]
        self.path(n,(l+k,t),ops,True)

    def build(self):
        self.add_polyline('growth',(6,26),(14,14),(22,18),(30,10),(34,14),(42,6))
        self.add_polyline('arrow-head',(34,6),(42,6),(42,14));self.relate('connect','growth','arrow-head')
        self.add_polyline('table',(14,34),(24,34),(24,26),(33,26),(42,26),(42,34),(42,42),(33,42),(24,42),(14,42),closed=True)
        self.add_line('column-left',(24,34),(24,42));self.relate('connect','column-left','table')
        self.add_polyline('column-right',(33,26),(33,34),(33,42));self.relate('connect','column-right','table')
        self.add_polyline('row',(24,34),(33,34),(42,34));self.relate('connect','row','column-right');self.relate('connect','row','table');self.relate('connect','row','column-left')
