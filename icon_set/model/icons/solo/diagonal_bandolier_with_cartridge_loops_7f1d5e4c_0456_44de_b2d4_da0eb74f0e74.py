'A broad rounded belt runs diagonally from lower left to upper right. Four adjacent cartridge-loop shapes project along one side, separated by short angled seams across the strap.\nPlan: Diagonal ammunition strap with four cartridge divisions. Shared seam endpoints follow a single band.\nConstruction reference: No useful exact Lucide match; source-specific construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f1d5e4c-0456-44de-b2d4-da0eb74f0e74'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/bandolier_7f1d5e4c-0456-44de-b2d4-da0eb74f0e74.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-bandolier-with-cartridge-loops'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('diagonal', 'bandolier', 'with', 'cartridge', 'loops')

    # Repair: Equal diagonal cartridge pitch preserves all four compartments.
    # Repair: Restore four projecting cartridge loops instead of a ladder-like plain strip; diagonal symmetry derives paired bulges.
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L':self.add_line(member,here,end)
                elif kind=='A':self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(member,here,(args[0],args[1],end))
                here=end;members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*points):self.add_polyline(name,*points,closed=points[0]==points[-1])
        def join(a,b):self.relate('connect',a,b)

        poly('back',(6,34),(13,27),(20,20),(27,13),(34,6))
        path('loops',(34,6),[('L',(40,12)),('C',(42,18),(42,14),(42,16)),('C',(33,19),(42,22),(37,23)),('C',(35,25),(35,21),(35,23)),('C',(26,26),(35,29),(30,30)),('C',(25,35),(30,30),(29,35)),('C',(19,33),(23,35),(21,35)),('C',(18,42),(23,37),(22,42)),('C',(12,40),(16,42),(14,42)),('L',(6,34))]);join('back','loops')
        for j,(a,b) in enumerate([((27,13),(33,19)),((20,20),(26,26)),((13,27),(19,33))]):line(f'loop-seam-{j}',a,b);join('back',f'loop-seam-{j}');join('loops',f'loop-seam-{j}')
