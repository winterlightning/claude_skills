from author_batch import *
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
k='cupped-hands-share-component';sh,pl,b=DRAWINGS[k]
b=b.replace("(22,9),(16,17)","(24,10),(14,16)").replace("(26,9),(32,17)","(24,10),(34,16)")
b += "        join('link-left','link-right')\n"
DRAWINGS[k]=(sh,pl,b)
k='person-raising-megaphone-with-sound-rays';sh,pl,b=DRAWINGS[k]
b=b.replace('(26,24)','(28,24)').replace('(26,31)','(28,31)').replace('(25,39)','(28,39)').replace('(22,20)','(24,20)').replace('(23,24)','(25,24)').replace('(22,23)','(24,23)').replace('(26,14)','(28,14)').replace('(22,17)','(24,17)').replace('(23,16)','(25,16)')
DRAWINGS[k]=(sh,pl,b)
add('fairy-with-butterfly-wings','SQUARE','Fairy with circular head, dress and mirrored butterfly wings. Human full_body_ref.png owns head(24,10),r4 and torso(24,22):4 ink gap. Paired upper lobes and lower lobes use shared axis and continuous curves. No useful local Lucide fairy match.', '''
        circle('head',24,10,4)
        poly('torso',(24,22),(24,27),(24,32))
        poly('skirt',(16,42),(24,32),(32,42),closed=True);join('torso','skirt')
        for j,s in enumerate((-1,1)):
            def p(x,y):return(24+s*x,y)
            path(f'wing-{j}',(24,27),[('C',p(18,16),p(7,21),p(13,16)),('L',p(18,21)),('C',p(14,26),p(18,24),p(17,26)),('C',p(18,34),p(18,28),p(18,31))])
            join('torso',f'wing-{j}')
        join('wing-0','wing-1')
        self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
''')
add('finger-prick-blood-sample','HRECT_L','Extended index finger and thumb, with a blood drop below the fingertip. Lucide droplets informs tangent-continuous teardrop. Other folded fingers reduced to smooth palm edge. HRECT_L holds directional hand and detached drop.', '''
        path('hand',(4,16),[('L',(13,10)),('C',(17,8),(15,9),(16,8)),('C',(24,12),(21,8),(24,9)),('L',(40,12)),('A',(40,20),4,4,True),('L',(25,20))])
        path('palm',(4,28),[('C',(18,32),(10,30),(12,32)),('L',(24,32))])
        path('drop',(39,29),[('C',(44,35),(41,31),(44,33)),('A',(34,35),5,5,True),('C',(39,29),(34,33),(37,31))],True)
''')
add('finger-touching-smartphone','SQUARE','Finger touches a smartphone with a single tap arc. Lucide smartphone supplies equal-radius corners and hand supplies round fingertip. Reference diagonal pointing pose retained; secondary tap ring omitted for clearance.', '''
        path('phone',(38,14),[('L',(38,10)),('A',(34,6),4,4,False),('L',(10,6)),('A',(6,10),4,4,False),('L',(6,38)),('A',(10,42),4,4,False),('L',(17,42))])
        path('hand',(42,42),[('L',(42,36)),('C',(38,30),(42,33),(40,32)),('L',(34,26)),('C',(27,25),(32,24),(29,25)),('C',(24,28),(25,25),(24,26)),('C',(26,32),(24,30),(25,31)),('L',(36,42))])
        path('tap',(16,26),[('A',(26,16),10,10,True)])
''')
add('front-facing-unicorn-head','VRECT_L','Frontal unicorn: long curved muzzle, two symmetric ears, eyes and central horn. Lucide dog informs continuous animal face contour; pointed horn/ears intentionally angular. Outlined central horn and diagonal ears preserve the defining unicorn identity.', '''
        path('face',(11,24),[('L',(11,31)),('A',(24,44),13,13,False),('A',(37,31),13,13,False),('L',(37,24)),('C',(32,16),(37,20),(34,18)),('L',(24,16)),('L',(16,16)),('C',(11,24),(14,18),(11,20))],True)
        poly('horn',(20,16),(24,4),(28,16));join('face','horn')
        for s in (-1,1):
            line('ear'+str(s),(24+s*8,16),(24+s*16,10));join('face','ear'+str(s))
        for x in(20,28):self.add_dot('eye'+str(x),(x,27))
''')
add('hand-holding-smartphone-component','HRECT_L','Hand grips smartphone with inward squeeze arrows, retained from complete reference. Lucide smartphone owns matching corner radii, Lucide hand informs palm curve. Individual curled fingers reduced to one grip line.', '''
        box('phone',14,8,34,30,3)
        path('palm',(18,40),[('L',(34,40)),('A',(44,30),10,10,False),('L',(44,28)),('C',(34,24),(44,24),(38,24))]);join('palm','phone')
        line('grip',(14,22),(22,22));join('phone','grip')
        for j,s in enumerate((-1,1)):
            def p(x,y):return (24+s*x,y)
            poly(f'arrow-{j}',p(20,16),p(10,16))
            poly(f'chevron-{j}',p(14,12),p(10,16),p(14,20))
            join(f'arrow-{j}',f'chevron-{j}');join(f'arrow-{j}','phone');join(f'chevron-{j}','phone')
''')
add('hand-supporting-a-heart','SQUARE','Hand supports a symmetric heart. Lucide heart and hand-heart inform smooth lobes and curved thumb; reference keeps heart dominant. Shared heart axis and mirrored curves; palm has coherent rounded return.', '''
        path('thumb',(6,30),[('L',(12,26)),('C',(18,24),(14,24),(16,24)),('L',(20,24)),('L',(24,24)),('A',(24,32),4,4,True),('L',(18,32))])
        path('palm',(6,42),[('L',(24,42)),('C',(30,40),(27,42),(28,42)),('L',(36,35)),('C',(42,29),(40,35),(42,33)),('C',(36,23),(42,26),(39,23)),('L',(24,32))]);join('thumb','palm')
        path('heart',(20,24),[('C',(8,12),(15,19),(8,17)),('A',(14,6),6,6,True),('C',(20,9),(17,6),(19,7)),('C',(26,6),(21,7),(23,6)),('A',(32,12),6,6,True),('C',(20,24),(32,17),(25,19))],True);join('heart','thumb')
''')
add('handcuff-pair-with-separate-key','SQUARE','Two circular cuffs linked by smooth flexible chain, separate key at lower right. Lucide key-round informs circular bow and straight toothed shaft. Source asymmetric diagonal composition retained; cuff rings equal radius.', '''
        circle('cuff-left',14,34,8);circle('cuff-right',34,14,8)
        path('chain',(14,26),[('C',(8,12),(11,21),(8,17)),('C',(15,6),(8,7),(10,6)),('C',(26,14),(21,6),(26,8))]);join('chain','cuff-left');join('chain','cuff-right')
        circle('key-head',33,39,3)
        poly('key-shaft',(33,36),(42,30),(42,34));join('key-head','key-shaft')
''')
add('hand-under-running-water','SQUARE','An open horizontal hand beneath three equal streams of running water. Lucide hand informs rounded grouped fingers; droplets construction uses straight repeated marks. Tangent thumb/palm transitions replace sudden bends.', '''
        path('hand',(6,34),[('L',(16,34)),('C',(22,31),(19,34),(20,33)),('C',(27,28),(24,29),(25,28)),('C',(32,34),(31,28),(34,31)),('L',(36,34)),('A',(42,38),6,4,True),('A',(36,42),6,4,True),('L',(6,42))])
        for j,x in enumerate((16,28,40)):
            line(f'water-{j}',(x,6),(x,8));self.add_dot(f'drop-{j}',(x,17))
''')
add('hands-cupping-a-profile-head','SQUARE','A right-facing profile held above two mirrored cupped hands. Human reference guides simplified anatomy; Lucide hand informs continuous palms. Head is an open anatomical profile, not a detached stick figure, with deliberate nose corner.', '''
        for j,s in enumerate((-1,1)):
            def p(x,y):return(24+s*x,y)
            path(f'hand-{j}',p(7,42),[('C',p(18,34),p(7,38),p(18,40)),('L',p(18,24))])
            path(f'thumb-{j}',p(18,34),[('C',p(10,31),p(14,34),p(12,32))]);join(f'hand-{j}',f'thumb-{j}')
        path('profile',(17,23),[('C',(14,14),(17,19),(14,19)),('A',(22,6),8,8,True),('C',(30,12),(27,6),(29,8)),('L',(34,16)),('L',(30,16)),('L',(30,20)),('A',(27,23),3,3,True)])
''')
add('hand-with-round-wrist-ornament','HRECT_L','Upright hand with four rounded fingers, side thumb and round wrist ornament. Lucide hand informs equal-radius fingertips. Shared finger widths; smooth continuous palm sides. Wrist band attaches at circular ornament extrema.', '''
        path('hand',(12,40),[('L',(12,34)),('C',(4,26),(12,30),(4,30)),('L',(4,24)),('A',(12,24),4,4,True),('L',(12,14)),('A',(20,14),4,4,True),('L',(20,12)),('A',(28,12),4,4,True),('L',(28,14)),('A',(36,14),4,4,True),('L',(36,18)),('A',(44,18),4,4,True),('L',(44,26)),('C',(36,34),(44,30),(36,30)),('L',(36,40))])
        circle('ornament',24,36,3);line('bracelet-left',(12,36),(21,36));line('bracelet-right',(27,36),(36,36))
        for a,b in [('ornament','bracelet-left'),('ornament','bracelet-right'),('bracelet-left','hand'),('bracelet-right','hand')]:join(a,b)
''')
k='person-raising-megaphone-with-sound-rays'
sh,pl,b=DRAWINGS[k]
b=b.replace("circle('head',11,26,5)","path('head',(6,26),[('A',(16,26),5,5,True),('A',(6,26),5,5,True)],True)")
DRAWINGS[k]=(sh,pl,b)
if __name__=='__main__':generate()
