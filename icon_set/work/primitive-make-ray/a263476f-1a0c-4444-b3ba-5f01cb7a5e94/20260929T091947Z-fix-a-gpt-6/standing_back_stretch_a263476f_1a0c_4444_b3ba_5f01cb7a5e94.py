from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'a263476f-1a0c-4444-b3ba-5f01cb7a5e94'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-back-stretch/20260929T091947Z-thuan-mac/reference/yoga back stretch_a263476f-1a0c-4444-b3ba-5f01cb7a5e94.svg'
AUTHOR = "gpt-6"
# Plan: Restore an arched back, hand on the lower back and upright legs, with a proportionate aligned head.
# Keyshape: VRECT_L; preserve reference arrangement.
# Construction reference: human_ref/full_body_ref.png.

def _draw(icon, name, description):
    tokens=description.split(); pos=0; part=0; count=0; members=[]; start=None; point=None
    def finish(closed=False):
        nonlocal members,part
        if members: icon.add_contour(name if part==0 else f"{name}-part{part}",*members,closed=closed)
        members=[];part+=1
    while pos<len(tokens):
        op=tokens[pos];pos+=1
        if op=='M':
            if members: finish()
            point=tuple(map(int,tokens[pos:pos+2]));pos+=2;start=point
        elif op=='Z':
            if point!=start:
                count+=1;eid=f"{name}-{count}";icon.add_line(eid,point,start);members.append(eid);point=start
            finish(True)
        else:
            count+=1;eid=f"{name}-{count}";members.append(eid)
            if op=='L':
                end=tuple(map(int,tokens[pos:pos+2]));pos+=2;icon.add_line(eid,point,end)
            elif op=='C':
                values=list(map(int,tokens[pos:pos+6]));pos+=6;c1=tuple(values[:2]);c2=tuple(values[2:4]);end=tuple(values[4:]);icon.add_bezier(eid,point,(c1,c2,end))
            elif op=='A':
                rx,ry,sweep,x,y=map(int,tokens[pos:pos+5]);pos+=5;end=(x,y);icon.add_arc(eid,point,end,radius_x=rx,radius_y=ry,sweep=bool(sweep))
            point=end
    if members: finish()

class Revision(Solo48):
    icon_id = 'standing-back-stretch'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'head', 'M 9 8 A 4 4 1 17 8 A 4 4 1 9 8 Z')
        _draw(self, 'torso', 'M 25 8 C 22 8 18 14 18 18 C 18 22 22 26 27 29')
        _draw(self, 'arm', 'M 25 8 L 35 8 C 42 8 41 14 35 14 L 28 14 L 23 19 L 29 25')
        _draw(self, 'hip-hand', 'M 29 25 L 33 23')
        _draw(self, 'legs', 'M 27 29 L 23 34 L 23 44')
        _draw(self, 'back-leg', 'M 27 29 L 30 35 L 30 44')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
        self.mark_human_figure('person', head='head', torso='torso-1', torso_junction='start')
