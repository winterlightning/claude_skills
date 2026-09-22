"""Spreadsheet with an unbroken header and three-column, four-row grid.
VRECT_L: x8..40 y4..44. Shared grid nodes own actual joins.
Reference preserves header and cells; Lucide table supplies rounded boundary
and connected rules. Repeated rows have 8-unit pitch; columns mirror x24.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '98aa08f5-1496-43e2-8294-a02bf0a05cd3'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_35/spreadsheet_98aa08f5-1496-43e2-8294-a02bf0a05cd3.svg'
AUTHOR = 'gpt-6-astra'
class SpreadsheetGridWithBlankHeader(Solo48):
    icon_id = 'spreadsheet-grid-with-blank-header'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ('Data Table Grid Layout', 'spreadsheet', 'table')
    keywords = ('grid', 'cells', 'rows', 'columns')
    def build(self):
        nodes = {}
        def line(name,a,b):
            self.add_line(name,a,b)
            for point in (a,b): nodes.setdefault(point,[]).append(name)
        def arc(name,a,b):
            self.add_arc(name,a,b,radius_x=4)
            for point in (a,b): nodes.setdefault(point,[]).append(name)
        line('top',(12,4),(36,4))
        arc('tr',(36,4),(40,8))
        ys=[8,12,20,28,36,40]
        for i,(a,b) in enumerate(zip(ys,ys[1:])):line(f'right-{i}',(40,a),(40,b))
        arc('br',(40,40),(36,44))
        xs=[36,30,18,12]
        for i,(a,b) in enumerate(zip(xs,xs[1:])):line(f'bottom-{i}',(a,44),(b,44))
        arc('bl',(12,44),(8,40))
        for i,(a,b) in enumerate(zip(ys[::-1],ys[-2::-1])):line(f'left-{i}',(8,a),(8,b))
        arc('tl',(8,8),(12,4))
        self.add_contour('border','top','tr',*[f'right-{i}' for i in range(5)],'br',*[f'bottom-{i}' for i in range(3)],'bl',*[f'left-{i}' for i in range(5)],'tl',closed=True)
        for j,y in enumerate(range(12,37,8)):
            for k,(a,b) in enumerate(zip([8,18,30],[18,30,40])):line(f'row-{j}-{k}',(a,y),(b,y))
        for k,x in enumerate((18,30)):
            for j,y in enumerate(range(12,37,8)):line(f'col-{k}-{j}',(x,y),(x,y+8))
        from itertools import combinations
        for members in nodes.values():
            for a,b in combinations(members,2):self.relate('connect',a,b)
