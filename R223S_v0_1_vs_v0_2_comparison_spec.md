# R223S v0.1 vs v0.2 comparison spec

## 1. Purpose

The sandbox preview must compare v0.1 and v0.2 candidate without treating v0.2 as published.

## 2. Comparison rows

Each sample comparison must include:

| row | required question |
| --- | --- |
| teacher_default_readability | Is the teacher draft still a mature manuscript? |
| classroom_event_depth | Are student responses, teacher moves and evidence timing clearer? |
| unit_intensity_effect | Did unit_phase_role/practice_intensity change expansion density? |
| review_ledger_completeness | Are component/screen/sheet/evidence mappings preserved? |
| field_leakage_risk | Did backend fields appear in teacher default view? |
| component_safety | Did component triggers remain review-only? |
| sample_contamination | Did content from another sample leak in? |

## 3. Expected per-sample deltas

### M_stationery

v0.2 candidate should show heavier creative support, teacher巡看, process evidence and performance task connection.

### N_paper_print

v0.2 candidate should show material prediction, technique trial and evidence record without becoming a full heavy creation project.

### O_color_collision

v0.2 candidate should show color perception, experiment and expression without turning into a large making workshop.

## 4. Scoring

Allowed comparison result:

```text
v0_2_candidate_better
v0_2_candidate_equal
v0_2_candidate_worse_hold
```

If teacher default readability is worse, the sample must be marked hold even if ledger completeness improves.

