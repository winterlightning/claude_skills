"""Workflow data table increasing arrow, preserving its complete supplied composition.
Symbol plan: coherent contours, nested identifying symbols and parameterized repeats.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='bd44c072-c5cf-4191-b2b0-3681a58f3a3a'
SOURCE_PATH='icon_set/work/todo-references/workflow data table increasing arrow_bd44c072-c5cf-4191-b2b0-3681a58f3a3a.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='workflow-data-table-increasing-arrow'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('workflow', 'data', 'table', 'increasing', 'arrow')

    # Visible extrema (4, 4, 44, 44); centerline extremes (6, 6, 42, 42).
    # For CIRCLE the envelope is radial: center (24,24), centerline radius 20.
    def build(self):
        # Rising zigzag arrow above a stepped four-row data grid.
        self.add_polyline('growth',(6,26),(14,16),(20,20),(27,12),(32,16),(42,6))
        self.add_polyline('arrow-head',(34,6),(42,6),(42,14))
        self.relate('connect','growth','arrow-head')
        self.add_polyline('table',(14,27),(24,27),(24,22),(33,22),(42,22),(42,27),
            (42,32),(42,37),(42,42),(33,42),(24,42),(14,42),(14,37),(14,32),closed=True)
        for x in (24,33):
            ys=(27,32,37,42) if x==24 else (22,27,32,37,42)
            self.add_polyline(f'column-{x}',*((x,y) for y in ys))
            self.relate('connect','table',f'column-{x}')
        for y in (27,32,37):
            xs=(24,33,42) if y==27 else (14,24,33,42)
            self.add_polyline(f'row-{y}',*((x,y) for x in xs))
            self.relate('connect','table',f'row-{y}')
            for x in (24,33): self.relate('connect',f'column-{x}',f'row-{y}')


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

