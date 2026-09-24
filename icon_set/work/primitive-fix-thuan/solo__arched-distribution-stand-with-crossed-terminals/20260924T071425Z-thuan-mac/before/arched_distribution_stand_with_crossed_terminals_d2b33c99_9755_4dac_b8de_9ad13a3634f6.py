"""Electrical Power Distribution Stand.

Symbol plan: Open-bottom distribution housing with two bent crossed terminals. Repeated stems and crosses retain their visible structural interpretation. Reduce inset from three sections to two to preserve spacing. No useful exact Lucide match.
Keyshape VRECT_L; exact visible bounds (6, 2, 42, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd2b33c99-9755-4dac-b8de-9ad13a3634f6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/devices/distribution stand_d2b33c99-9755-4dac-b8de-9ad13a3634f6.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'arched-distribution-stand-with-crossed-terminals'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/devices'
    aliases = ()
    keywords = ('electrical', 'power', 'distribution', 'stand')

    def build(self):
        self.add_line('left',(8,44),(8,21));self.add_arc('corner-left',(8,21),(12,17),radius_x=4)
        self.run('top',(12,17),(14,17),(30,17),(36,17))
        self.add_arc('corner-right',(36,17),(40,21),radius_x=4);self.add_line('right',(40,21),(40,44))
        self.add_contour('housing','left','corner-left','top-1','top-2','top-3','corner-right','right')
        for i,x in enumerate((18,34)):
            self.add_line(f'stem-{i}',(x-4,17),(x-4,10))
            self.add_arc(f'bend-{i}',(x-4,10),(x,6),radius_x=4)
            self.add_contour(f'terminal-{i}',f'stem-{i}',f'bend-{i}')
            self.graph([(f'cross-up-{i}',(x,4),(x,6)),(f'cross-down-{i}',(x,6),(x,8)),(f'cross-left-{i}',(x-4,6),(x,6)),(f'cross-right-{i}',(x,6),(x+4,6))])
            for arm in ('up','down','left','right'):self.relate('connect',f'terminal-{i}',f'cross-{arm}-{i}')
            self.relate('connect',f'terminal-{i}','housing')
        self.add_polyline('panel',(17,35),(17,26),(31,26),(31,35),(31,44),(17,44),closed=True)
        self.add_line('division',(17,35),(31,35));self.relate('connect','division','panel')

    def graph(self,edges):
        for name,a,b in edges:self.add_line(name,a,b)
        for i,(name,a,b) in enumerate(edges):
            for other,c,d in edges[i+1:]:
                if {a,b}&{c,d}:self.relate('connect',name,other)

    def run(self,name,*points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(f"{name}-{i}",a,b)
