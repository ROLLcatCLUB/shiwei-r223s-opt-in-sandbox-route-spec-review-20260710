# R223S opt-in sandbox route spec

stage_id: 1013R_R223S_OPT_IN_SANDBOX_ROUTE_SPEC  
status: route_spec_only  
source: R223R_V0_2_CANDIDATE_PILOT_ROUTE_PLANNING  
decision_target: PASS_CONTINUE_TO_R223T_FIXTURE_ONLY_SANDBOX_PREVIEW

## 1. Route identity

R223S defines a possible sandbox route shape for R223M classroom_event_standard v0.2 candidate.

This is not a formal product route and not an R97B route.

Recommended route identity:

```text
route_kind = independent_opt_in_sandbox
route_purpose = v0_1_vs_v0_2_candidate_preview
data_mode = fixture_only
state_mode = non_persistent_preview
teacher_confirmed = false
formal_apply_allowed = false
lesson_body_writeback = false
```

## 2. Route entry rule

The sandbox route may be entered only by explicit review action, not by normal teacher workflow.

Allowed entry examples:

- direct local sandbox preview URL
- review package HTML preview in future R223T
- internal reviewer link

Disallowed entry examples:

- R97B primary route
- prep room navigation tab
- production lesson generation entry
- teacher-facing formal "use this draft" action

## 3. Route data rule

The route must load only R223Q fixture data:

- M_stationery
- N_paper_print
- O_color_collision

No provider/model/runtime/prompt/database is allowed.

## 4. Route preview rule

The route may show:

- teacher default draft preview
- review ledger summary preview
- unit_phase_role / practice_intensity explanation
- v0.1 / v0.2 candidate side-by-side comparison
- component trigger status as review-only metadata
- screen / learning sheet / evidence mapping as review-only metadata

The route must not show:

- formal publish control
- save to lesson body
- run model button
- apply to R97B button
- component execution button
- database persistence status

## 5. Required visible warning

Every R223T preview derived from this spec must display:

```text
Preview only. v0.2 candidate is not published. No lesson body writeback.
```

## 6. Current decision

R223S allows only the next step:

```text
R223T_FIXTURE_ONLY_SANDBOX_PREVIEW
```

R223S does not authorize implementation in formal UI.

