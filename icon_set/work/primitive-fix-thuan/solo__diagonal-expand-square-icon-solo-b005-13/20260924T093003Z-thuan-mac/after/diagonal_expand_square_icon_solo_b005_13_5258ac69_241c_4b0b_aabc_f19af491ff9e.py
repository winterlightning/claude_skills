"""Bad-stroke revision. Lucide maximize-2: clear diagonal shaft and open right-angle arrowhead.
Omissions: Lower corner reduced to a compact rounded corner to preserve spacing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5258ac69-241c-4b0b-aabc-f19af491ff9e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-expand-square-icon-solo-b005-13/20260924T093003Z-thuan-mac/reference/resize expand corner_5258ac69-241c-4b0b-aabc-f19af491ff9e.svg'
AUTHOR = 'gpt-6'
class Revision(Solo48):
    icon_id = 'diagonal-expand-square-icon-solo-b005-13'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('resize', 'expand', 'corner')
    def build(self):

        # Typed continuous paths own their junctions. Repeated parts share parameters.
        def path(name, start, commands, closed=False):
            ids=[]; here=start
            for i, (kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                ids.append(ident);here=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        # Outer rounded square; separated lower corner and upper-right arrow.
        path('frame',(10,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)
        poly('arrow',(25,15),(33,15),(33,23))
        line('shaft',(25,23),(33,15));join('arrow','shaft')
        path('corner',(15,29),[('L',(17,29)),('A',(19,31),2,2,True),('L',(19,33))])
