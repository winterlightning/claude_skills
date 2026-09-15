"""A cloud outline with two domed lobes is crossed inside by two diagonal lines that meet at the centre in a shallow X.

Symbol plan: Cloud with two crossed diagonal facet boundaries meeting at (24,27). Extremes (4,8)-(44,40).
Review notes: Keeps both internal diagonals and their real contacts with the cloud. The junction is adjusted to integer coordinates; the facets have a shallow intentional bend. Lucide cloud informs the outer silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9661d55e-fb7b-4ad4-a213-c9622acb0fc6'
SOURCE_PATH = 'pictographic-primitives/logos/microsoft onedrive logo 1_9661d55e-fb7b-4ad4-a213-c9622acb0fc6.svg'
AUTHOR = 'gpt-6'

class MicrosoftOnedriveLogo(Solo48):
    icon_id = 'microsoft-onedrive-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('onedrive', 'microsoft', 'cloud', 'storage', 'logo', 'brand', 'sync')

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
        self.add_arc('dome',(12,20),(36,20),radius_x=12)
        self.add_bezier('right-shoulder',(36,20),((40,20),(44,24),(44,30)))
        self.add_arc('right-upper',(44,30),(42,36),radius_x=10)
        self.add_arc('right-lower',(42,36),(34,40),radius_x=10)
        self.add_line('base',(34,40),(14,40))
        self.add_arc('left-lower',(14,40),(6,36),radius_x=10)
        self.add_arc('left-upper',(6,36),(4,30),radius_x=10)
        self.add_bezier('left-shoulder',(4,30),((4,24),(7,20),(12,20)))
        self.add_contour('cloud','dome','right-shoulder','right-upper','right-lower','base','left-lower','left-upper','left-shoulder',closed=True)
        j=(24,27)
        for name,a,b in [('facet-ul',(12,20),j),('facet-lr',j,(42,36)),('facet-ll',(6,36),j),('facet-ur',j,(36,20))]:self.add_line(name,a,b)
        parts=['facet-ul','facet-lr','facet-ll','facet-ur']
        for i,a in enumerate(parts):
            for b in parts[i+1:]:self.relate('connect',a,b)
        for a,bs in [('facet-ul',['dome','left-shoulder']),('facet-ur',['dome','right-shoulder']),('facet-lr',['right-upper','right-lower']),('facet-ll',['left-upper','left-lower'])]:
            for b in bs:self.relate('connect',a,b)
