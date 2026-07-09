# R223S fixture data contract

## 1. Source fixtures

The sandbox route spec may use only R223Q fixture data.

| fixture | role | source artifact |
| --- | --- | --- |
| M_stationery | practice_creation / high | R223Q sample generation input and generated draft/ledger |
| N_paper_print | technique_preparation / medium | R223Q sample generation input and generated draft/ledger |
| O_color_collision | intro_understanding / medium | R223Q sample generation input and generated draft/ledger |

## 2. Required input fields

Each sample fixture must include:

- sample_id
- title
- unit_phase_role
- lesson_position_in_unit
- practice_intensity
- student_work_time_ratio
- teacher_support_density
- generation_focus
- must_show
- must_not_show

## 3. Required preview outputs

Each sample preview must provide:

- teacher_default_draft
- review_ledger_summary
- intensity_router_explanation
- v0_1_vs_v0_2_delta_summary
- component_trigger_status_summary
- screen_sheet_evidence_mapping_summary

## 4. Persistence rule

All preview state must be local and disposable.

```json
{
  "fixture_only": true,
  "non_persistent_preview": true,
  "database_written": false,
  "lesson_body_written": false,
  "teacher_confirmed": false,
  "formal_apply_allowed": false
}
```

## 5. Mutation bans

R223S and R223T must not mutate:

- R223M/P5 standard records
- R223M/N/O existing teacher drafts
- R223Q regression fixtures
- R222D component library
- R97B route or UI files

