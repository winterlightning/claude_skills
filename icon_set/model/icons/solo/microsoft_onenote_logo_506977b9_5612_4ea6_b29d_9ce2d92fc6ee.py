"""A tall rounded notebook with three short ring tabs projecting from its left edge.

Symbol plan: Rounded notebook with three equally spaced short binding marks. Extremes (8,4)-(40,44).
Review notes: Lucide notebook informs the rounded cover and attached binding marks. All three marks remain, with exactly eight units between them. Their position follows the rendered source, on the inside of the left edge.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '506977b9-5612-4ea6-b29d-9ce2d92fc6ee'
SOURCE_PATH = 'pictographic-primitives/logos/microsoft onenote logo_506977b9-5612-4ea6-b29d-9ce2d92fc6ee.svg'
AUTHOR = 'gpt-6'

class MicrosoftOnenoteLogo(Solo48):
    icon_id = 'microsoft-onenote-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('onenote', 'microsoft', 'notebook', 'notes', 'office', 'logo', 'brand')

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
        self.add_line('top',(14,4),(34,4))
        self.add_arc('tr',(34,4),(40,10),radius_x=6)
        self.add_line('right',(40,10),(40,38))
        self.add_arc('br',(40,38),(34,44),radius_x=6)
        self.add_line('bottom',(34,44),(14,44))
        self.add_arc('bl',(14,44),(8,38),radius_x=6)
        ys=(38,32,24,16,10)
        for i,(a,b) in enumerate(zip(ys,ys[1:])):self.add_line(f'left-{i}',(8,a),(8,b))
        self.add_arc('tl',(8,10),(14,4),radius_x=6)
        self.add_contour('book','top','tr','right','br','bottom','bl',*[f'left-{i}' for i in range(4)],'tl',closed=True)
        for i,y in enumerate((32,24,16)):
            name=f'binding-{i}';self.add_line(name,(8,y),(14,y))
            for edge in [i,i+1]:self.relate('connect',name,f'left-{edge}')
