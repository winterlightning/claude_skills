from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'd6f4580b-3c39-42da-abe7-0d859e33509b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tumbling-figure-with-raised-legs/20260929T090755Z-thuan-mac/reference/somersault_d6f4580b-3c39-42da-abe7-0d859e33509b.svg'
AUTHOR = "gpt-6"
# Plan: Draw an inverted figure with raised split legs, curved torso and two distinct supporting arms; exact head gap 4.
# Keyshape: SQUARE; preserve reference arrangement.
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
    icon_id = 'tumbling-figure-with-raised-legs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'head', 'M 32 30 A 5 5 1 42 30 A 5 5 1 32 30 Z')
        _draw(self, 'torso', 'M 24 30 C 20 30 18 25 18 22')
        _draw(self, 'leg-left', 'M 18 22 L 6 7')
        _draw(self, 'leg-right', 'M 18 22 L 24 6')
        _draw(self, 'arm-left', 'M 21 29 L 13 34 L 10 42')
        _draw(self, 'arm-right', 'M 24 30 L 26 41')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
        self.mark_human_figure('person', head='head', torso='torso-1', torso_junction='start')
