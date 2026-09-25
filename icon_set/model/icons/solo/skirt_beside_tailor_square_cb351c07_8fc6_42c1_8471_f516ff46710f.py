'Fashion Skirt and Measuring Ruler.\nPlan and review: Retained flared skirt beneath and to the right of a tailor square, including waistband and one ruler tick. Omitted pleats and extra graduations. These functional objects form a tailoring scene, with no independent status glyph.\nKeyshape: SQUARE, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cb351c07-8fc6-42c1-8471-f516ff46710f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/fashion design measuring_cb351c07-8fc6-42c1-8471-f516ff46710f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'skirt-beside-tailor-square'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('skirt', 'beside', 'tailor', 'square')

    def build(self):

        def path(name, start, steps, closed=False):
            members=[]; point=start
            for index, step in enumerate(steps):
                member=f"{name}-{index}"
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep); point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def curve(name,start,*segments):
            self.add_bezier(name,start,*segments)

        path('ruler',(6,42),[(6,6),(42,6)])
        self.add_line('tick',(18,6),(18,10));self.relate('connect','ruler','tick')
        path('skirt',(22,20),[(36,20),(42,42),(16,42),(22,20)],True)
        self.add_line('waist',(20,28),(38,28));self.relate('connect','skirt','waist')
