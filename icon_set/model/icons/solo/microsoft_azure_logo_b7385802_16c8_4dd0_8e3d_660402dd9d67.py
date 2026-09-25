"""A large open triangle outline with a rounded top holds a smaller inward-folding triangle, and its base line extends past the right corner.

Symbol plan: One open angular A ribbon with rounded apex and folded inner end. Extremes (4,8)-(44,40).
Review notes: Retains the open triangle, inner fold, and extending base. The inner base is lifted to leave ten units between parallel rails. Lucide rounded enclosure principles inform the few rounded turns; asymmetric ribbon shape follows the source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7385802-16c8-4dd0-8e3d-660402dd9d67'
SOURCE_PATH = 'pictographic-primitives/logos/microsoft azure logo_b7385802-16c8-4dd0-8e3d-660402dd9d67.svg'
AUTHOR = 'gpt-6'

class MicrosoftAzureLogo(Solo48):
    icon_id = 'microsoft-azure-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('azure', 'microsoft', 'cloud', 'triangle', 'logo', 'brand', 'platform')

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
        self.add_line('base',(14,40),(40,40))
        self.add_arc('lower-right',(40,40),(44,36),radius_x=4,sweep=False)
        self.add_line('right',(44,36),(26,10))
        self.add_arc('apex',(26,10),(22,10),radius_x=2,sweep=False)
        chain('fold',(22,10),(4,30),(22,30))
        self.add_arc('inner-turn',(22,30),(24,28),radius_x=2,sweep=False)
        self.add_line('inner',(24,28),(18,18))
        self.add_contour('ribbon','base','lower-right','right','apex','fold-1','fold-2','inner-turn','inner')
