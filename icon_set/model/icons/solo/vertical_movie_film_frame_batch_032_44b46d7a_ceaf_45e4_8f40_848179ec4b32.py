"""A vertical filmstrip has a rounded outer frame, narrow perforated side bands, and a broad horizontal gap dividing two image areas. One short perforation mark appears in each side of each frame."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '44b46d7a-ceaf-45e4-8f40-848179ec4b32'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/video edit_44b46d7a-ceaf-45e4-8f40-848179ec4b32.svg'
AUTHOR = 'gpt-6'


class Batch032Icon(Solo48):
    icon_id = 'vertical-movie-film-frame-batch-032'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ('vertical-movie-film-frame',)
    keywords = ('batch-032',)

    def build(self):
        # Symbol plan: film frame, two equal 8-unit side bands, three repeated rung levels.
        # Each physical grid junction shares an endpoint; corner arcs have radius 4.
        edges=[]
        def line(name,a,b):
            self.add_line(name,a,b); edges.append((name,a,b))
        for x in (8,16,32,40):
            ys=(8,14,24,34,40) if x in (8,40) else (4,14,24,34,44)
            for i,(a,b) in enumerate(zip(ys,ys[1:])): line(f'rail-{x}-{i}',(x,a),(x,b))
        for y in (4,44):
            for i,(a,b) in enumerate(((12,16),(16,32),(32,36))): line(f'end-{y}-{i}',(a,y),(b,y))
        for y in (14,24,34):
            for a,b in ((8,16),(32,40)): line(f'rung-{a}-{y}',(a,y),(b,y))
        line('image-divider',(16,24),(32,24))
        for name,a,b in [('tl',(8,8),(12,4)),('tr',(36,4),(40,8)),('br',(40,40),(36,44)),('bl',(12,44),(8,40))]:
            self.add_arc(name,a,b,radius_x=4);edges.append((name,a,b))
        for i,(name,a,b) in enumerate(edges):
            for other,c,d in edges[i+1:]:
                if a in (c,d) or b in (c,d): self.relate('connect',name,other)
