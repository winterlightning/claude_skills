"""A table column copied rightward, shown as two columns and arrows.

SOLO48 HRECT_L; Lucide reference: table-columns-split: column dividers.
Symbol plan: source composition reduced to named outlines and shared geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '90da22c6-273c-4d21-a1a8-a6cfb89b48b6'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/duplicate column_90da22c6-273c-4d21-a1a8-a6cfb89b48b6.svg'
AUTHOR = 'gpt-6'

class DuplicateTableColumn(Solo48):
    icon_id = 'duplicate-table-column'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'data/tables'
    aliases = ('Duplicate Table Column',)
    keywords = tuple('duplicate table column'.split())

    def ring(self, name, x, y, r):
        self.add_arc(name+'-ne',(x,y-r),(x+r,y),radius_x=r,sweep=True)
        self.add_arc(name+'-se',(x+r,y),(x,y+r),radius_x=r,sweep=True)
        self.add_arc(name+'-sw',(x,y+r),(x-r,y),radius_x=r,sweep=True)
        self.add_arc(name+'-nw',(x-r,y),(x,y-r),radius_x=r,sweep=True)
        self.add_contour(name,*(name+'-'+s for s in ('ne','se','sw','nw')),closed=True)

    def box(self, name, x1, y1, x2, y2):
        self.add_polyline(name,(x1,y1),(x2,y1),(x2,y2),(x1,y2),closed=True)

    def round_box(self, name, x1, y1, x2, y2, r):
        parts=[]
        def line(s,a,b):
            n=name+'-'+s; self.add_line(n,a,b); parts.append(n)
        def arc(s,a,b):
            n=name+'-'+s; self.add_arc(n,a,b,radius_x=r,sweep=True); parts.append(n)
        line('top',(x1+r,y1),(x2-r,y1))
        arc('ne',(x2-r,y1),(x2,y1+r))
        line('right',(x2,y1+r),(x2,y2-r))
        arc('se',(x2,y2-r),(x2-r,y2))
        line('bottom',(x2-r,y2),(x1+r,y2))
        arc('sw',(x1+r,y2),(x1,y2-r))
        line('left',(x1,y2-r),(x1,y1+r))
        arc('nw',(x1,y1+r),(x1+r,y1))
        self.add_contour(name,*parts,closed=True)

    def heart(self,name,x,y):
        self.add_arc(name+'-left',(x,y-2),(x-6,y-4),radius_x=4,radius_y=4,sweep=False)
        self.add_arc(name+'-left-side',(x-6,y-4),(x-6,y+2),radius_x=4,radius_y=4,sweep=False)
        self.add_line(name+'-left-tip',(x-6,y+2),(x,y+8))
        self.add_line(name+'-right-tip',(x,y+8),(x+6,y+2))
        self.add_arc(name+'-right-side',(x+6,y+2),(x+6,y-4),radius_x=4,radius_y=4,sweep=False)
        self.add_arc(name+'-right',(x+6,y-4),(x,y-2),radius_x=4,radius_y=4,sweep=False)
        self.add_contour(name,*(name+s for s in ('-left','-left-side','-left-tip','-right-tip','-right-side','-right')),closed=True)

    def build(self) -> None:
        self.box('source',4,8,14,40)
        self.box('copy',34,8,44,40)
        for y in (19,29):
         self.add_line('source-row-'+str(y),(4,y),(14,y)); self.relate('connect','source-row-'+str(y),'source')
         self.add_line('copy-row-'+str(y),(34,y),(44,y)); self.relate('connect','copy-row-'+str(y),'copy')
        self.add_line('arrow',(22,24),(26,24))
        self.add_polyline('arrow-head',(23,21),(26,24),(23,27))
