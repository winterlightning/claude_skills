from author import make
make(3,'VRECT_L','Rejected reader had a tiny book and artificial shoulder loop. Enlarge the open newspaper and replace the loop with a short central torso behind the fold. Text omitted for clean spacing.','''
circle('head',24,10,6)
line('torso',(24,24),(24,28))
poly('paper',(8,24),(24,28),(40,24),(40,40),(24,44),(8,40),closed=True)
line('fold',(24,28),(24,44));join('fold','paper');join('torso','paper');join('torso','fold')
self.mark_human_figure('reader',head='head',torso='torso',torso_junction='start')
''','human_ref/full_body_ref.png and Lucide newspaper original/atoms; head bottom16 to torso24 exact4 ink gap; shared central paper fold.')
