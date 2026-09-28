"""Whole Hazelnut Fruit.

Plan: A pointed hazelnut shell with a single curved inner seam.
Reduction / construction: Nut: clear shell silhouette; replace nested pointed form with a spacious curved seam.
Envelope: VRECT_L, exact SOLO48 contract extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab041675-7743-4e6a-aafd-e70defe745eb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hazelnut_ab041675-7743-4e6a-aafd-e70defe745eb.svg'
AUTHOR = 'gpt-6'


class Batch064Icon8(Solo48):
    icon_id = 'pointed-hazelnut-form-batch-064'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('pointed', 'hazelnut', 'form')

    def build(self):

        def path(name, start, commands, closed=False):
            members=[]
            point=start
            for i,command in enumerate(commands):
                kind,end,*args=command
                member=f"{name}-{i}"
                if kind=='L':
                    self.add_line(member,point,end)
                else:
                    rx,ry,sweep=args
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep)
                members.append(member)
                point=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx,cy-ry),rx,ry,True),('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        axis = 24

        path('shell',(axis,4),[('A',(axis+16,24),26,26,True),('A',(axis-16,24),16,20,True),('A',(axis,4),26,26,True)],True)
        self.add_arc('seam',(axis,15),(axis,34),radius_x=14,radius_y=14)
