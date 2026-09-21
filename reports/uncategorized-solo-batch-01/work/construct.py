"""Batch authoring recipes; source identities are loaded without alteration."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BATCH = ROOT / 'reports/uncategorized-solo-batch-01'
ENTRIES = json.loads((BATCH / 'manifest.json').read_text())['entries']
SOURCE_ICON_ID = tuple(e['source_uuid'] for e in ENTRIES)
SOURCE_PATH = tuple(e['source_path'] for e in ENTRIES)
AUTHOR = 'gpt-6-astra'

HELPERS = '''
    def circle(self, name, x, y, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r, radius_y=ry)
        self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r, radius_y=ry)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def path(self, name, points, closed=False):
        self.add_polyline(name, *points, closed=closed)

    def arc(self, name, a, b, r, ry=None, sweep=True):
        self.add_arc(name, a, b, radius_x=r, radius_y=r if ry is None else ry, sweep=sweep)

    def rect(self, name, x, y, w, h, r=4):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f'{name}-{i}'; ids.append(part)
            if i%2: self.arc(part,a,b,r)
            elif a != b: self.add_line(part,a,b)
            else: ids.pop()
        self.add_contour(name,*ids,closed=True)
'''

# Each recipe owns one independently authored SOLO48 subject. Parameters in
# repeated motifs (bubbles, paired limbs, seams) share an axis or series.
RECIPES = {}
def recipe(n,key,plan,code,ref='No useful exact Lucide match; geometric arc construction.'):
    RECIPES[n]=(key,plan,code,ref)

recipe(1,'HRECT_L','Crowned visitor and companion tent; preserve the natural scene; omit neckline.', '''
        self.path('crown',[(26,8),(30,12),(34,8),(38,12),(42,8),(40,20),(28,20)],True)
        self.arc('face',(28,20),(40,20),6,sweep=False)
        self.relate('connect','crown','face')
        self.arc('shoulders',(24,40),(44,40),10,6)
        self.path('tent',[(4,24),(12,12),(20,24),(4,24),(6,40),(18,40),(20,24)])
''','human_ref/user.svg: circular face and curved shoulders; tent is a companion object.')
recipe(7,'SQUARE','Thrower with round head, bent throwing arm and diagonal javelin; exact detached gap 4.', '''
        self.circle('head',26,16,4)
        self.add_line('torso',(26,28),(26,34))
        self.path('arm',[(26,28),(14,28),(12,16)])
        self.add_line('javelin',(6,18),(42,6))
        self.relate('connect','arm','javelin')
        self.add_line('forward-arm',(26,28),(42,28))
        self.path('legs',[(12,42),(26,34),(36,42)])
        for p in ['arm','forward-arm','legs']: self.relate('connect','torso',p)
        self.relate('connect','arm','forward-arm')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''','human_ref/full_body_ref.png: round head and coherent limbs; directional throwing pose.')
recipe(8,'SQUARE','Front car with paired tires and three wash bubbles; reduce seven bubbles to three.', '''
        for i,x in enumerate((10,24,38)): self.circle(f'bubble-{i}',x,9,3)
        self.path('windshield',[(8,30),(14,22),(34,22),(40,30)])
        self.rect('body',6,30,36,8,2)
        self.relate('connect','windshield','body')
        for i,x in enumerate((12,36)):
            self.add_line(f'tire-{i}',(x,38),(x,42)); self.relate('connect','body',f'tire-{i}')
''','Lucide car-front: rounded body, trapezoidal windshield and paired wheels.')
recipe(11,'VRECT_L','Loop ribbon with diagonal crossing and two broad tails; remove redundant fold lines.', '''
        self.arc('loop',(14,18),(34,18),10,14)
        self.path('left-strand',[(14,18),(40,38),(32,44),(8,24)])
        self.path('right-strand',[(34,18),(8,38),(16,44),(40,24)])
        self.relate('connect','loop','left-strand'); self.relate('connect','loop','right-strand')
        self.relate('connect','left-strand','right-strand')
''','Lucide ribbon: top loop with crossed flat-cut tails.')
recipe(12,'VRECT_L','Baboon face with long central muzzle and symmetric ears; omit mouth and small eyes if crowded.', '''
        self.circle('head',24,24,12,20)
        self.circle('muzzle',24,30,4,8)
        for side,x in [('left',8),('right',40)]: self.add_dot('ear-'+side,(x,16))
''')
recipe(13,'SQUARE','Side bonnet with an open face band and tied ribbons; asymmetry preserves side view.', '''
        self.arc('dome',(6,24),(42,24),18)
        self.arc('back',(42,24),(26,34),16,10)
        self.arc('opening',(26,34),(6,24),20,14)
        self.add_contour('bonnet','dome','back','opening',closed=True)
        self.path('tie',[(26,34),(18,42),(34,42),(26,34)])
        self.relate('connect','bonnet','tie')
''')
recipe(14,'HRECT_L','Blank round baby head and integrated curl; omit ear micro-lobes to protect round silhouette.', '''
        self.arc('face',(40,24),(8,24),16,sweep=True)
        self.arc('forehead',(8,24),(24,8),16)
        self.arc('curl',(24,8),(24,20),6)
        self.add_contour('head','face','forehead','curl')
        self.add_line('ear-left',(4,24),(8,24)); self.relate('connect','head','ear-left')
        self.add_line('ear-right',(40,24),(44,24)); self.relate('connect','head','ear-right')
''','Lucide baby: integrated forehead curl and round open face outline.')
recipe(15,'SQUARE','Cradle with baby head above a broad front panel and rocking base; omit post decoration.', '''
        self.circle('head',24,10,4)
        self.rect('cradle',8,22,32,12,4)
        self.arc('rocker',(6,38),(42,38),30,10,sweep=False)
        for i,x in enumerate((14,34)):
            self.add_line(f'support-{i}',(x,34),(x,40));self.relate('connect','cradle',f'support-{i}');self.relate('connect','rocker',f'support-{i}')
''','human_ref/user.svg: round baby head; cradle is a physical supporting object.')
recipe(16,'VRECT_M','Backbone logo: rectangular structural loop crossed by diagonals; deliberate sharp geometry.', '''
        self.path('frame',[(10,4),(38,4),(38,14),(38,34),(38,44),(10,44),(10,34),(10,14)],True)
        self.add_line('diagonal-a',(10,14),(38,34));self.add_line('diagonal-b',(38,14),(10,34))
        for p in ['diagonal-a','diagonal-b']: self.relate('connect','frame',p)
        self.relate('connect','diagonal-a','diagonal-b')
''')
recipe(17,'HRECT_M','Seated badger in profile: broad back, long muzzle, ear and forefoot; omit tiny eye.', '''
        self.arc('back',(4,30),(24,10),20)
        self.path('snout',[(24,10),(30,10),(44,22),(34,26)])
        self.arc('chest',(34,26),(30,38),12,sweep=False)
        self.add_line('base',(30,38),(12,38))
        self.arc('rump',(12,38),(4,30),8)
        self.add_contour('animal','back','snout-1','snout-2','snout-3','chest','base','rump',closed=True)
        self.add_line('hind-leg',(16,28),(14,38));self.relate('connect','animal','hind-leg')
''')
recipe(18,'SQUARE','Racket with a small companion shuttlecock; reduce string mesh to two crossed runs.', '''
        self.circle('racket',30,18,12)
        self.add_line('handle',(6,42),(21,27)); self.relate('connect','racket','handle')
        self.add_line('string-v',(30,6),(30,30));self.add_line('string-h',(18,18),(42,18))
        for p in ['string-v','string-h']: self.relate('connect','racket',p)
        self.relate('connect','string-v','string-h')
        self.path('shuttle',[(6,6),(6,18),(14,14)],True)
''')
for n in [19,20]:
    recipe(n,'SQUARE','Diagonal shuttlecock with a rounded cork and three feather rays; fan shares the cork junction.', '''
        self.arc('cork',(6,30),(18,42),9,sweep=False)
        self.add_line('join',(18,42),(6,30))
        self.add_contour('base','cork','join',closed=True)
        self.path('feathers',[(6,30),(18,6),(26,10),(34,14),(42,22),(18,42)])
        self.relate('connect','base','feathers')
        self.add_line('feather-a',(10,34),(26,10));self.add_line('feather-b',(14,38),(34,14))
        for p in ['feather-a','feather-b']:
            self.relate('connect','base',p);self.relate('connect','feathers',p)
''')
recipe(21,'SQUARE','Suitcase on a platform beside a dial scale; retain handle and dial, omit tag and suitcase bands.', '''
        self.rect('case',6,22,20,16,3)
        self.path('handle',[(10,22),(10,14),(22,14),(22,22)])
        self.relate('connect','case','handle')
        self.circle('dial',36,12,6)
        self.add_line('post',(36,18),(36,42));self.relate('connect','dial','post')
        self.add_line('platform',(6,42),(42,42));self.relate('connect','post','platform')
''')
recipe(22,'SQUARE','Bread basket with tall baguette and round loaf; omit scoring lines in the small loaves.', '''
        self.path('baguette',[(10,28),(10,10)])
        self.arc('bread-top',(10,10),(22,10),6)
        self.add_line('bread-side',(22,10),(22,28))
        self.add_contour('long-loaf','baguette-1','bread-top','bread-side')
        self.arc('round-loaf',(26,28),(42,28),8)
        self.add_line('rim',(6,28),(42,28))
        self.arc('basket',(42,28),(6,28),18,14)
        self.add_contour('basket-body','rim','basket',closed=True)
        self.relate('connect','basket-body','long-loaf');self.relate('connect','basket-body','round-loaf')
''')
recipe(23,'SQUARE','Muffin: three broad domed lobes over a tapered cup; remove tiny scallops.', '''
        self.arc('left',(6,22),(14,14),8)
        self.arc('dome',(14,14),(34,14),10,8)
        self.arc('right',(34,14),(42,22),8)
        self.arc('right-bottom',(42,22),(34,30),8)
        self.add_line('base',(34,30),(14,30))
        self.arc('left-bottom',(14,30),(6,22),8)
        self.add_contour('top','left','dome','right','right-bottom','base','left-bottom',closed=True)
        self.path('cup',[(10,29),(14,42),(34,42),(38,29)])
        self.relate('connect','top','cup')
''','Lucide soup: coherent bowl outline; source supplies the three-lobed muffin silhouette.')
recipe(24,'HRECT_L','Semicircular flour sifter and handle, with a centered row of falling grains.', '''
        self.add_line('rim',(4,8),(32,8))
        self.arc('sieve',(32,8),(4,8),14,16)
        self.add_contour('bowl','rim','sieve',closed=True)
        self.add_line('handle',(32,8),(44,8));self.relate('connect','bowl','handle')
        for i,x in enumerate((8,20,32)): self.add_line(f'grain-{i}',(x,34),(x,40))
''','Lucide soup: semicircular bowl attached to a horizontal rim; repeated grains share spacing.')
recipe(25,'VRECT_L','Balaclava with broad eye slot and round mouth; simplify flared neck to straight lower edge.', '''
        self.arc('crown',(8,20),(40,20),16)
        self.path('sides',[(40,20),(40,44),(8,44),(8,20)])
        self.add_contour('mask','crown','sides-1','sides-2','sides-3',closed=True)
        self.rect('eye-slot',17,16,14,8,4)
        self.circle('mouth',24,35,2)
''')
recipe(26,'VRECT_M','Oval balloon with a short curving string; omit tiny knot polygon.', '''
        self.arc('balloon-right',(24,4),(24,32),14)
        self.arc('balloon-left',(24,32),(24,4),14)
        self.add_contour('balloon','balloon-right','balloon-left',closed=True)
        self.arc('string-a',(24,32),(28,38),6,sweep=False)
        self.arc('string-b',(28,38),(24,44),6)
        self.add_contour('string','string-a','string-b')
        self.relate('connect','balloon','string')
''','Lucide balloon: coherent curved outline and short flowing attached string.')
recipe(27,'VRECT_L','Lower leg in a cast with broad ankle and left-facing toes; two wrap lines define bandages.', '''
        self.path('leg',[(24,4),(40,4),(40,36)])
        self.arc('heel',(40,36),(32,44),8)
        self.add_line('sole',(32,44),(16,44))
        self.arc('toe',(16,44),(16,28),8)
        self.path('ankle',[(16,28),(24,28),(24,4)])
        self.add_contour('outline','leg-1','leg-2','heel','sole','toe','ankle-1','ankle-2',closed=True)
        self.add_line('wrap',(24,12),(40,20));self.relate('connect','outline','wrap')
        self.add_line('foot-wrap',(24,28),(24,44));self.relate('connect','outline','foot-wrap')
''')
recipe(28,'CIRCLE','Neptune sphere with two vertical bands and spot; simplify interrupted outline to whole sphere.', '''
        self.circle('planet',24,24,20)
        self.add_line('band-left',(16,6),(16,42))
        self.add_line('band-right',(26,4),(26,44))
        for p in ['band-left','band-right']:self.relate('connect','planet',p)
        self.circle('spot',36,24,2)
''')
recipe(29,'HRECT_L','Rounded soap bar beneath three rising bubbles; reduce bubbles to two sizes.', '''
        self.rect('bar',4,26,40,14,6)
        self.circle('bubble-large',13,12,4)
        self.circle('bubble-small',32,12,3)
''')
recipe(30,'SQUARE','Bow-tied server with companion wine glass; round head and curved shoulders.', '''
        self.circle('head',18,12,6)
        self.arc('shoulders',(6,42),(30,42),12,16)
        self.path('bow',[(10,26),(26,34),(26,26),(10,34)],True)
        self.relate('connect','shoulders','bow')
        self.path('glass',[(34,18),(42,18),(42,26),(34,26)],True)
        self.add_line('stem',(38,26),(38,42));self.relate('connect','glass','stem')
''','human_ref/user.svg: circular head and broad curved shoulders; glass is a physical held object.')
recipe(31,'SQUARE','Batter with an upright torso, round head and raised diagonal bat; exact 4-unit detached head gap.', '''
        self.circle('head',30,14,4)
        self.add_line('torso',(30,26),(30,34))
        self.path('arms',[(30,26),(18,28),(10,22)])
        self.add_line('bat',(10,22),(18,6));self.relate('connect','arms','bat')
        self.path('legs',[(18,42),(30,34),(42,42)])
        self.relate('connect','torso','arms');self.relate('connect','torso','legs')
        self.add_line('grip',(6,24),(10,22));self.relate('connect','arms','grip');self.relate('connect','bat','grip')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''','human_ref/full_body_ref.png: outlined head, coherent limbs, angled held bat.')
recipe(32,'HRECT_L','Batting helmet in profile with broad ear guard and a circular ear opening.', '''
        self.arc('dome',(4,24),(36,24),16)
        self.path('brim',[(36,24),(44,24),(28,24)])
        self.arc('face-cut',(28,24),(28,32),4,sweep=False)
        self.arc('guard',(28,32),(12,32),8)
        self.arc('back',(12,32),(4,24),8)
        self.add_contour('helmet','dome','brim-1','brim-2','face-cut','guard','back',closed=True)
        self.circle('ear',19,29,2)
''')
recipe(33,'HRECT_L','Backward cap and sunglasses as a natural outfit; remove button and rear opening.', '''
        self.arc('cap',(4,24),(44,24),20,16)
        self.add_line('cap-base',(44,24),(4,24));self.add_contour('hat','cap','cap-base',closed=True)
        for i,x in enumerate((14,34)): self.circle(f'lens-{i}',x,36,6,4)
        self.add_line('bridge',(20,36),(28,36))
        for i in range(2): self.relate('connect','bridge',f'lens-{i}')
''','Lucide hat-glasses: separate headwear and paired lenses; source requires a baseball cap.')
recipe(34,'SQUARE','Catcher mitt with rounded finger lobes, deep thumb gap and a single web band.', '''
        self.path('thumb',[(6,24),(6,18)])
        self.arc('thumb-top',(6,18),(14,18),4)
        self.add_line('thumb-inner',(14,18),(14,26))
        self.arc('gap',(14,26),(22,26),4,sweep=False)
        self.add_line('finger-left',(22,26),(22,10))
        self.arc('finger-top',(22,10),(30,10),4)
        self.arc('finger-next',(30,10),(38,10),4)
        self.arc('outer-corner',(38,10),(42,14),4)
        self.add_line('outer',(42,14),(42,24))
        self.arc('palm',(42,24),(6,24),18)
        self.add_contour('mitt','thumb-1','thumb-top','thumb-inner','gap','finger-left','finger-top','finger-next','outer-corner','outer','palm',closed=True)
        self.add_line('web',(14,18),(22,18));self.relate('connect','mitt','web')
''','Lucide hand: rounded finger caps and one smooth palm arc.')
recipe(35,'HRECT_L','Open stadium with diamond infield; remove fine seating ticks and mound.', '''
        self.arc('upper',(4,16),(44,16),20,8)
        self.path('walls',[(44,16),(44,32)])
        self.arc('lower',(44,32),(4,32),20,8)
        self.add_line('left',(4,32),(4,16))
        self.add_contour('stadium','upper','walls-1','lower','left',closed=True)
        self.path('diamond',[(24,17),(34,26),(24,35),(14,26)],True)
''')
recipe(36,'SQUARE','Scoreboard above fan-shaped field; omit pennants and scoreboard text.', '''
        self.rect('scoreboard',14,6,20,12,2)
        self.add_line('post',(24,18),(24,26));self.relate('connect','scoreboard','post')
        self.arc('field',(6,34),(42,34),24,12)
        self.path('foul-lines',[(42,34),(24,42),(6,34)])
        self.add_contour('ground','field','foul-lines-1','foul-lines-2',closed=True)
''')
recipe(37,'CIRCLE','Basketball sphere with a horizontal seam and two curved panel seams; remove one crowded seam.', '''
        self.arc('outline-top',(4,24),(44,24),20)
        self.arc('outline-bottom',(44,24),(4,24),20)
        self.add_contour('ball','outline-top','outline-bottom',closed=True)
        self.add_line('equator',(4,24),(44,24));self.relate('connect','ball','equator')
        self.arc('seam-left',(12,8),(12,40),26,sweep=True)
        self.arc('seam-right',(36,8),(36,40),26,sweep=False)
        for p in ['seam-left','seam-right']:
            self.relate('connect','ball',p);self.relate('connect','equator',p)
''')
recipe(38,'HRECT_L','Reclining sun lounger with angled backrest, long seat and two feet.', '''
        self.path('seat',[(4,8),(16,30),(44,30)])
        self.path('legs',[(12,40),(18,30),(38,30),(44,40)])
        self.relate('connect','seat','legs')
''','Lucide bed: coherent furniture frame with structural legs; preserve side-view recline.')
recipe(39,'SQUARE','Lounger under parasol, a physical beach scene; simplify canopy to a semicircle.', '''
        self.arc('canopy',(6,22),(38,22),16)
        self.add_line('canopy-base',(38,22),(6,22));self.add_contour('parasol','canopy','canopy-base',closed=True)
        self.add_line('pole',(22,22),(22,34));self.relate('connect','parasol','pole')
        self.path('seat',[(6,34),(34,34),(42,26)])
        self.relate('connect','seat','pole')
        for i,x in enumerate((12,32)):
            self.add_line(f'leg-{i}',(x,34),(x-4,42));self.relate('connect','seat',f'leg-{i}')
''','Lucide umbrella: semicircular canopy; physical lounger and parasol remain one scene.')
recipe(40,'HRECT_L','Beach parasol beside a low sun; retain shoreline, simplify canopy ribs.', '''
        self.circle('sun',12,16,8)
        self.arc('canopy',(24,24),(44,24),10)
        self.add_line('base',(44,24),(24,24));self.add_contour('parasol','canopy','base',closed=True)
        self.add_line('pole',(34,24),(30,40));self.relate('connect','parasol','pole')
        self.add_line('shore',(4,40),(44,40));self.relate('connect','shore','pole')
''','Lucide umbrella: clean canopy construction; source supplies the sun and shoreline.')
recipe(41,'HRECT_L','Bear in right profile with open mouth and two heavy legs; omit tiny face detail.', '''
        self.arc('back',(4,26),(24,8),20,18)
        self.path('face',[(24,8),(34,8),(44,12),(36,22),(44,22)])
        self.arc('jaw',(44,22),(32,30),12,8)
        self.path('front-leg',[(32,30),(34,40),(26,40),(22,30)])
        self.path('belly',[(22,30),(16,30),(14,40),(6,40),(4,26)])
        self.add_contour('bear','back','face-1','face-2','face-3','face-4','jaw','front-leg-1','front-leg-2','front-leg-3','belly-1','belly-2','belly-3','belly-4',closed=True)
''')
recipe(42,'VRECT_L','Explorer portrait: hat, round face and curved shoulders; omit backpack straps and beard inner line.', '''
        self.path('hat',[(14,14),(16,4),(32,4),(34,14)])
        self.add_line('brim',(8,14),(40,14));self.relate('connect','hat','brim')
        self.arc('jaw',(14,14),(34,14),10,sweep=False)
        self.relate('connect','jaw','brim')
        self.arc('shoulders',(8,44),(40,44),16,16)
        self.relate('connect','jaw','shoulders')
''','human_ref/user.svg: circular jaw and broad curved shoulders; touching ink avatar construction.')
recipe(43,'VRECT_L','Bearded worker portrait with curved shoulders and apron; circular jaw and swept hair.', '''
        self.arc('hair',(14,14),(34,14),10)
        self.arc('jaw',(34,14),(14,14),10)
        self.add_contour('head','hair','jaw',closed=True)
        self.arc('shoulders',(8,44),(40,44),16)
        self.relate('connect','head','shoulders')
        self.path('apron',[(16,32),(16,44),(32,44),(32,32)])
        self.relate('connect','shoulders','apron')
''','human_ref/user.svg: circular face and broad curved shoulders; touching ink avatar construction.')
recipe(44,'SQUARE','Bed beneath four-pane window; reduce pillow to an open rounded rise.', '''
        self.path('bed',[(6,24),(6,42),(6,34),(42,34),(42,42)])
        self.rect('window',26,6,16,16,2)
        self.add_line('mullion-v',(34,6),(34,22));self.add_line('mullion-h',(26,14),(42,14))
        for p in ['mullion-v','mullion-h']:self.relate('connect','window',p)
        self.relate('connect','mullion-v','mullion-h')
        self.arc('pillow',(6,34),(18,34),6,8);self.relate('connect','bed','pillow')
''','Lucide bed: side-view frame and curved pillow; window is a physical scene detail.')
recipe(45,'HRECT_L','Single bed with tall rounded headboard and raised pillow.', '''
        self.path('frame',[(4,40),(4,8),(4,30),(44,30),(44,40)])
        self.arc('pillow',(4,30),(24,30),10)
        self.relate('connect','frame','pillow')
        self.add_line('rail',(4,38),(44,38));self.relate('connect','frame','rail')
''','Lucide bed: long rails, upright posts and rounded pillow.')
recipe(46,'SQUARE','Nightstand with one knob, upper drawer and plain lower compartment; shared cabinet width.', '''
        self.rect('cabinet',6,6,36,28,4)
        self.add_line('divider',(6,24),(42,24));self.relate('connect','cabinet','divider')
        self.add_dot('knob',(24,15))
        for i,x in enumerate((12,36)):
            self.add_line(f'leg-{i}',(x,34),(x,42));self.relate('connect','cabinet',f'leg-{i}')
''')
recipe(47,'VRECT_M','Tall pint glass with a broad rim band and tapered body; straight symmetric taper.', '''
        self.path('glass',[(10,4),(38,4),(38,12),(32,44),(16,44),(10,12)],True)
        self.add_line('rim',(10,12),(38,12));self.relate('connect','glass','rim')
''','Lucide glass-water: symmetric tapered vessel and broad internal horizontal band.')
recipe(48,'SQUARE','Three party cups below a flying ball; remove flight trails to preserve space.', '''
        self.circle('ball',24,10,4)
        self.path('front',[(16,26),(32,26),(30,42),(18,42)],True)
        self.path('left',[(6,18),(14,18),(12,34),(6,34)],True)
        self.path('right',[(34,18),(42,18),(42,34),(36,34)],True)
''','Lucide glass-water: tapered cups; repeated pair is mirrored about the center cup.')
for n in [49,50]:
    recipe(n,'SQUARE','Beetle with divided wing cases, rounded head, paired antennae and three mirrored legs.', '''
        self.rect('shell',14,18,20,24,10)
        self.arc('head',(16,18),(32,18),8)
        self.relate('connect','shell','head')
        self.add_line('seam',(24,18),(24,42));self.relate('connect','shell','seam');self.relate('connect','head','seam')
        for side,sgn in [('left',-1),('right',1)]:
            self.add_line('antenna-'+side,(24+sgn*5,12),(24+sgn*10,6))
            self.relate('connect','head','antenna-'+side)
            for i,y in enumerate((20,30,40)):
                self.add_line(f'{side}-leg-{i}',(24+sgn*10,y),(24+sgn*18,y))
                self.relate('connect','shell',f'{side}-leg-{i}')
''','Lucide bug: shared shell, central seam and three mirrored leg attachments.')

if __name__ == '__main__':
    import sys
    for n in map(int,sys.argv[1:]):
        e=ENTRIES[n-1]; key,plan,code,ref=RECIPES[n]
        path=ROOT/'icon_set/model/icons/solo'/((e['icon_id']+'_'+e['source_uuid']).replace('-','_')+'.py')
        text=f'''"""{e['concept']}.

Plan: {plan}
Construction reference: {ref}
Keyshape {key}: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = {e['source_uuid']!r}
SOURCE_PATH = {e['source_path']!r}
AUTHOR = {AUTHOR!r}

class Drawing(Solo48):
    icon_id = {e['icon_id']!r}
    keyshape = Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = {'avatars' if n in (42,43) else 'objects/misc'!r}
    aliases = ()
    keywords = {tuple(e['concept'].lower().split())!r}
'''
        if n in (42,43):text+='    human_construction = "bust"\n'
        text+='\n    def build(self):\n'+code+HELPERS
        if path.exists(): raise RuntimeError(f'Refusing to replace {path}')
        path.write_text(text)
        print(path.relative_to(ROOT))
