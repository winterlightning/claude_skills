'Project Workflow Decision Diagram.\n\nSymbol plan: Two process boxes join a decision diamond. Preserve branching topology; omit the redundant left vertical tail.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7358a474-0177-454c-bd55-153e1f35b913'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/workflow gantt chart 6_7358a474-0177-454c-bd55-153e1f35b913.svg'
AUTHOR = 'gpt-6'

class WorkflowDecisionBranch(Solo48):
    icon_id = 'workflow-decision-branch'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'diagrams'
    categories = ('diagrams', 'primitive', 'primitives')
    aliases = ()
    keywords = ('workflow', 'decision', 'branch')

    def build(self):
        # Two process boxes join a decision diamond. Preserve branching topology; omit the redundant left vertical tail.
        axis_x = 24
        p_4_12 = (4, 12)
        p_4_36 = (4, 36)
        p_12_8 = (12, 8)
        p_12_12 = (12, 12)
        p_12_16 = (12, 16)
        p_12_32 = (12, 32)
        p_12_36 = (12, 36)
        p_12_40 = (12, 40)
        p_28_8 = (28, 8)
        p_28_12 = (28, 12)
        p_28_16 = (28, 16)
        p_28_32 = (28, 32)
        p_28_36 = (28, 36)
        p_28_40 = (28, 40)
        p_30_24 = (30, 24)
        p_37_12 = (37, 12)
        p_37_17 = (37, 17)
        p_37_31 = (37, 31)
        p_37_36 = (37, 36)
        p_44_24 = (44, 24)
        self.add_line('upper-1', p_12_8, p_28_8)
        self.add_line('upper-2', p_28_8, p_28_12)
        self.add_line('upper-2-join-1', p_28_12, p_28_16)
        self.add_line('upper-3', p_28_16, p_12_16)
        self.add_line('upper-4', p_12_16, p_12_12)
        self.add_line('upper-4-join-1', p_12_12, p_12_8)
        self.add_contour('upper', 'upper-1', 'upper-2', 'upper-2-join-1', 'upper-3', 'upper-4', 'upper-4-join-1', closed=True)
        self.add_line('lower-1', p_12_32, p_28_32)
        self.add_line('lower-2', p_28_32, p_28_36)
        self.add_line('lower-2-join-1', p_28_36, p_28_40)
        self.add_line('lower-3', p_28_40, p_12_40)
        self.add_line('lower-4', p_12_40, p_12_36)
        self.add_line('lower-4-join-1', p_12_36, p_12_32)
        self.add_contour('lower', 'lower-1', 'lower-2', 'lower-2-join-1', 'lower-3', 'lower-4', 'lower-4-join-1', closed=True)
        self.add_line('input-1', p_12_12, p_4_12)
        self.add_line('input-2', p_4_12, p_4_36)
        self.add_line('input-3', p_4_36, p_12_36)
        self.add_contour('input', 'input-1', 'input-2', 'input-3', closed=False)
        self.add_line('output-1', p_28_12, p_37_12)
        self.add_line('output-2', p_37_12, p_37_17)
        self.add_contour('output', 'output-1', 'output-2', closed=False)
        self.add_line('diamond-1', p_37_17, p_44_24)
        self.add_line('diamond-2', p_44_24, p_37_31)
        self.add_line('diamond-3', p_37_31, p_30_24)
        self.add_line('diamond-4', p_30_24, p_37_17)
        self.add_contour('diamond', 'diamond-1', 'diamond-2', 'diamond-3', 'diamond-4', closed=True)
        self.add_line('lower-output-1', p_28_36, p_37_36)
        self.add_line('lower-output-2', p_37_36, p_37_31)
        self.add_contour('lower-output', 'lower-output-1', 'lower-output-2', closed=False)
        self.relate("connect", 'input', 'upper')
        self.relate("connect", 'input', 'lower')
        self.relate("connect", 'output', 'upper')
        self.relate("connect", 'output', 'diamond')
        self.relate("connect", 'lower-output', 'lower')
        self.relate("connect", 'lower-output', 'diamond')
