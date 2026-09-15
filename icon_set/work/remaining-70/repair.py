from pathlib import Path
import json,re,ast,textwrap
AUTHOR='gpt-6';SOURCE_ICON_ID=None;SOURCE_PATH='icon_set/work/remaining-70/plan.json'
W=Path(__file__).parent;P={g['number']:g for g in json.loads((W/'plan.json').read_text())};CHANGED={}
def edit(i,changes,note):
 g=P[i];p=Path(g['target_file']);s=ast.unparse(ast.parse((W/'before'/(g['root']+'.py')).read_text()))+'\n'
 for a,b in changes:
  assert a in s,(i,a);s=s.replace(a,b)
 s=re.sub(r"AUTHOR\s*=\s*['\"][^'\"]*['\"]", "AUTHOR = 'gpt-6'",s)
 s='# Repair: '+note+'\n'+s;p.write_text(s);CHANGED[i]=note

def redraw(i,body,note,key=None):
 g=P[i];p=Path(g['target_file']);s=(W/'before'/(g['root']+'.py')).read_text();t=ast.parse(s);c=next(c for c in t.body if isinstance(c,ast.ClassDef));b=next(x for x in c.body if isinstance(x,ast.FunctionDef) and x.name=='build');lines=s.splitlines();lines[b.lineno-1:b.end_lineno]=['    def build(self):',*textwrap.indent(textwrap.dedent(body).strip(),'        ').splitlines()];s='\n'.join(lines)+'\n';s=re.sub(r"AUTHOR\s*=\s*['\"][^'\"]*['\"]", "AUTHOR = 'gpt-6'",s)
 if key:s=re.sub(r'keyshape\s*=\s*Keyshape\.\w+',f'keyshape = Keyshape.{key}',s)
 p.write_text('# Repair: '+note+'\n'+s);CHANGED[i]=note

edit(3,[('(25, 25)','(25, 24)')],'Level the paddling forearm 8 units above the gunwale; keep actual paddle contact.')
edit(4,[('(22, 10)','(26, 10)'),('(19, 18)','(23, 18)'),('(30, 10)','(31, 10)')],'Widen the rear index finger without thinning the front hand.')
edit(6,[('(28, 16)','(27, 18)'),('(36, 24)','(35, 27)')],'Open the gap between the clasped thumb and the outer knuckles.')
edit(7,[('(12, 29)','(11, 27)')],'Raise the holding elbow away from the rear thigh, retaining the circular discus.')
edit(8,[('(18, 26)','(18, 24)'),('(28, 28)','(29, 25)'),('(28, 34)','(29, 34)')],'Give the lower jaw and the supporting hand a 9-unit separation.')
edit(9,[('(14, 30)','(10, 29)'),('(16, 26)','(12, 20)'),('(24, 32)','(24, 27)')],'Broaden the bent thumb while retaining the fingertip and board.')
edit(10,[('(10, 28)','(8, 26)')],'Move the backward hand clear of the back leg; preserve the approved head placement.')
edit(13,[('(14, 20)','(12, 22)')],'Move the fist knuckle away from the axe blade, preserving the shaft grip.')
edit(14,[('(38, 22)','(38, 26)'),('(44, 28)','(44, 30)')],'Lower the supporting fingertips away from the heart lobe.')
edit(15,[('(6, 16)','(6, 18)'),('(16, 24)','(16, 26)'),('(24, 24)','(24, 26)'),('(34, 16)','(34, 18)'),('(26, 14)','(26, 12)'),('(14, 14)','(14, 12)'),('(28, 24)','(28, 26)')],'Widen the wrench jaw opening and preserve its attachment to the grip.')
edit(16,[('(16, 30)','(16, 24)'),('(8, 24)','(8, 16)')],'Give the raised thumb a full-width diagonal outline instead of a pinched wedge.')
edit(18,[('p(13, 38)','p(15, 38)'),('p(13, 42)','p(15, 42)'),('p(5, 36)','p(5, 35)')],'Widen both palms symmetrically while keeping the open cradling gesture.')
edit(19,[('(18, 8)','(15, 8)'),('(18, 18)','(20, 18)')],'Open the clasp counter between the thumb and upper left knuckles.')
edit(21,[('(34, 16)','(32, 16)'),('(38, 12)','(36, 12)'),('(36, 22)','(38, 22)'),('(36, 36)','(38, 36)'),('(36, 42)','(38, 42)')],'Broaden the horse head and neck without changing the skier-to-horse tether.')
edit(22,[("self.add_line('tail-1', (9, 30), (8, 37))","self.add_line('tail-1', (9, 30), (8, 22))"),('(26, 22)','(26, 20)')],'Lift the tail clear of the hind leg and level the reins above the saddle.')
edit(23,[('(6, 24)','(6, 16)'),('(14, 28)','(14, 22)')],'Widen the extended thumb while preserving the I-love-you finger arrangement.')
edit(24,[('(30, 30)','(30, 32)'),('(21, 27)','(21, 29)')],'Lower the skating hip and knee away from the forward arm.')
edit(26,[('(14, 25)','(14, 24)'),('(33, 34)','(33, 35)')],'Level the guard and open the arm-to-thigh gap while preserving the fighting stance.')
edit(27,[('(15, 35)','(15, 33)'),('(23, 34)','(23, 33)')],'Raise both ski knees to leave more than 8 units above the ski.')
edit(35,[('(8, 25)','(8, 23)')],'Lift the rear shoulder edge to open clearance above the diagonal seatbelt.')
edit(36,[('(6, 22)','(6, 18)'),('(14, 28)','(14, 24)')],'Broaden the front thumb while retaining the two overlapping palms.')
edit(37,[('(42, 34)','(42, 29)')],'Shorten the free forearm so it clears the right thigh.')
edit(38,[('(26, 34)','(28, 35)')],'Open the bend of the kicking knee away from the planted thigh.')
edit(39,[('(38, 29)','(38, 28)')],'Lift the free hand one unit clear of the bent knee.')
edit(40,[('(6, 25)','(6, 23)')],'Lift the outstretched leg to separate it from the lower leg.')
edit(41,[('(12, 32)','(10, 31)')],'Move the backward knee away from the descending front leg.')
edit(42,[('(12, 27)','(10, 23)')],'Lift the rear hand clear of the rear thigh during the tripping action.')
edit(44,[('(14, 44)','(22, 44)'),('(34, 44)','(26, 44)')],'Widen both wrist openings equally; retain the joined prayer palms.')
edit(45,[('(20, 39)','(20, 40)')],'Lower the rear knee one unit to clear the carrying arm.')
edit(48,[('(24, 35)','(24, 39)'),('(34, 35)','(36, 31)')],'Lengthen the torso and lift the free hand clear of the dancing legs.')
edit(49,[('(10, 32)','(10, 30)'),('(18, 32)','(15, 30)'),('(38, 32)','(38, 30)'),('(30, 32)','(33, 30)'),('(6, 34)','(6, 38)'),('(42, 34)','(42, 38)')],'Raise the resting hands and lower the crossed thighs to open both elbow gaps.')
edit(51,[('(8, 8)','(13, 8)'),('(20, 20)','(23, 20)'),('(32, 20)','(35, 20)')],'Broaden the little finger while retaining the thumb and folded knuckles.')
edit(52,[('(33, 38)','(35, 40)'),('(42, 35)','(42, 37)')],'Lower the skis away from the seated thigh and keep the boot on the ski.')
edit(53,[('(24, 27)','(24, 30)'),('(30, 28)','(30, 31)'),('(28, 32)','(28, 33)'),('(20, 32)','(20, 34)')],'Lengthen the torso so the raised knees clear the rope handles.')
edit(54,[('(18, 22)','(21, 22)'),('(16, 30)','(19, 30)')],'Widen the folded thumb within the snapping gesture.')
edit(57,[('(30, 14)','(34, 14)'),('(30, 6)','(34, 6)'),('(34, 18)','(38, 18)'),('(34, 26)','(38, 26)')],'Move the upper wrist outward to clear the central knuckles.')
edit(59,[('(26, 29)','(29, 26)'),('(34, 32)','(35, 29)'),('(40, 32)','(40, 29)')],'Raise the bent forearm away from the thigh while keeping the stooped torso.')
edit(60,[('(6, 28)','(6, 24)'),('(42, 28)','(42, 24)')],'Lift both outstretched hands away from the squat thighs symmetrically.')
edit(61,[('(13, 27)','(13, 30)'),('(6, 29)','(6, 33)'),('(20, 31)','(20, 33)'),('(29, 33)','(29, 33)')],'Lower the surfboard and lengthen the crouched body below the balancing arms.')
edit(63,[('(18, 29)','(17, 27)')],'Raise the racket elbow away from the forward knee.')
edit(64,[('(22, 34)','(23, 28)')],'Shorten the left figure free arm so it no longer crowds either leg.')
edit(66,[('(30, 27)','(31, 25)'),('(40, 29)','(40, 26)')],'Lift the forward forearm away from the raised knee.')
edit(67,[('(14, 31)','(14, 32)'),('(22, 32)','(22, 33)')],'Lower the ski knee away from the towing arm.')
edit(68,[('(9, 29)','(9, 32)'),('(21, 32)','(21, 33)')],'Lengthen the seated torso to open the arm-to-thigh gap.')
edit(69,[('(26, 24)','(28, 24)'),('(38, 24)','(40, 24)'),('(28, 16)','(30, 16)'),('(32, 16)','(34, 16)'),('(36, 16)','(38, 16)'),("('bride', 32)","('bride', 34)")],'Move the bride rightward as one figure to separate the couple bodies.')
edit(70,[('(20, 22)','(23, 24)'),('(30, 22)','(31, 24)')],'Move the car roof away from the heart balloon without altering either subject.')
(W/'changes.json').write_text(json.dumps(CHANGED,indent=2))
