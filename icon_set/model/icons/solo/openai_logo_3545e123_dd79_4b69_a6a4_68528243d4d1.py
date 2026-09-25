"""A hexagonal knot of six interlocking rounded loops woven around an open hexagon at its centre.

Symbol plan: Six-lobed woven knot surrounding an open hexagon; extremes (6,6)-(42,42).
Review notes: No useful local Lucide match for this six-loop knot. Preserves central hexagon, six clockwise arms and rounded lobe flow. Shared outer joins and six axial extrema are explicit; the integer-grid approximation retains its turning direction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3545e123-dd79-4b69-a6a4-68528243d4d1'
SOURCE_PATH = 'pictographic-primitives/logos/openai logo_3545e123-dd79-4b69-a6a4-68528243d4d1.svg'
AUTHOR = 'gpt-6'

class OpenaiLogo(Solo48):
    icon_id = 'openai-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('openai', 'ai', 'knot', 'logo', 'brand', 'chatgpt', 'research')

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
        vertices=[(24,14),(33,19),(33,29),(24,34),(15,29),(15,19)]
        self.add_polyline('center',*vertices,closed=True)
        outer=[(34,8),(40,23),(33,40),(14,40),(8,25),(15,8)]
        apices=[(24,6),(42,16),(42,32),(24,42),(6,32),(6,16)]
        controls=[[(30,6),(28,6),(20,6),(17,6)],[(42,21),(42,19),(42,12),(38,8)],[(38,40),(42,38),(42,29),(42,26)],[(18,42),(20,42),(28,42),(31,42)],[(6,27),(6,29),(6,36),(10,40)],[(10,8),(6,10),(6,19),(6,22)]]
        for i,a in enumerate(vertices):
         b=outer[i];end=outer[(i-1)%6];apex=apices[i];c=controls[i]
         self.add_line(f'arm-{i}',a,b)
         self.add_bezier(f'lobe-{i}-a',b,(c[0],c[1],apex))
         self.add_bezier(f'lobe-{i}-b',apex,(c[2],c[3],end))
         self.add_contour(f'weave-{i}',f'arm-{i}',f'lobe-{i}-a',f'lobe-{i}-b')
         for edge in [i+1,6 if i==0 else i]:self.relate('connect',f'arm-{i}',f'center-{edge}')
        for i in range(6):
         previous=(i-1)%6
         for member in [f'arm-{previous}',f'lobe-{previous}-a']:self.relate('connect',f'lobe-{i}-b',member)
