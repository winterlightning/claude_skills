"""An angled five-point star on a diagonal wand. The star is intentionally rotated as in the source, with an open central counter. SQUARE centerlines (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ab312eb6-0227-4cb6-98e2-21e3c1f7afe5'
SOURCE_PATH = 'pictographic-primitives/design/magic wand_ab312eb6-0227-4cb6-98e2-21e3c1f7afe5.svg'
AUTHOR='gpt-6'
CONSTRUCTION_REFERENCE='wand: one diagonal shaft with a dominant magical head; supplied source owns five-point star'
DESIGN_PLAN='An angled five-point star on a diagonal wand. The star is intentionally rotated as in the source, with an open central counter. SQUARE centerlines (6,6)-(42,42).'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='magic-wand'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'design'
    categories = ('design', 'state')
    aliases=()
    keywords=('magic', 'wand')
    def path(self, name, start, commands, closed=False):
        members=[]
        for i,(kind,end,*args) in enumerate(commands):
            member=f'{name}-{i}'
            if kind=='L': self.add_line(member,start,end)
            elif kind=='A': self.add_arc(member,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(member,start,(args[0],args[1],end))
            members.append(member); start=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,cx,cy,r):
        self.path(name,(cx-r,cy),[('A',(cx,cy-r),r,r,True),('A',(cx+r,cy),r,r,True),('A',(cx,cy+r),r,r,True),('A',(cx-r,cy),r,r,True)],True)


    def build(self):
        self.add_polyline('star',(23,6),(30,12),(39,8),(36,18),(42,25),(32,25),(27,34),(24,24),(14,22),(23,17),closed=True)
        self.add_line('wand',(6,42),(24,24));self.relate('connect','star','wand')
