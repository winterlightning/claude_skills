'A stepped telescope tube angles upward to the right, ending in a broad flared rim. A round pivot beneath the tube connects it to three long splayed tripod legs.\nPlan: Telescope slants upwards right on a three-legged tripod. Tube steps simplified to one broad barrel; preserve eyepiece and pivot.\nConstruction reference: telescope: diagonal barrel and splayed tripod, with source-specific rim simplification.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a411b38b-0170-4301-bf5f-38c559aea73b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/astronomy telescope_a411b38b-0170-4301-bf5f-38c559aea73b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'long-telescope-on-a-jointed-tripod'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('long', 'telescope', 'on', 'a', 'jointed', 'tripod')

    # Repair: Removed circular pivot which collided with the barrel. Three legs attach at a shared lower barrel point; no false circle contact.
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

        poly('tube',(6,22),(34,6),(42,18),(30,25),(14,34),(6,22))
        poly('tripod',(18,42),(30,25),(30,42));line('right-leg',(30,25),(42,42))
        join('tube','tripod');join('tube','right-leg');join('tripod','right-leg')
