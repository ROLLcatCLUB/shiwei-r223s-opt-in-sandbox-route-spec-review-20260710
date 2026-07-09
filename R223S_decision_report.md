# R223S decision report

stage_id: 1013R_R223S_OPT_IN_SANDBOX_ROUTE_SPEC  
status: PASS_LOCAL_ROUTE_SPEC  
decision: PASS_CONTINUE_TO_R223T_FIXTURE_ONLY_SANDBOX_PREVIEW

## Decision

R223S passes as an opt-in sandbox route specification.

It defines how v0.2 candidate may be previewed in a future fixture-only sandbox without publishing v0.2, modifying R97B, connecting runtime/model/prompt/db, or writing back to lesson body.

## What R223T may do

R223T may create a fixture-only sandbox preview that follows this spec:

- independent local/static preview
- fixture-only data
- non-persistent state
- safety banner
- teacher default draft preview
- review ledger summary preview
- v0.1 / v0.2 candidate comparison
- no apply/save/runtime controls

## What remains blocked

```text
R223M_STANDARD_V0_2 = NOT_PUBLISHED
FORMAL_UI = BLOCKED
R97B_ROUTE = BLOCKED
FRONTEND_BACKEND = BLOCKED
RUNTIME_PROVIDER_MODEL_PROMPT_DB = BLOCKED
LESSON_BODY_WRITEBACK = BLOCKED
R222D_COMPONENT_LIBRARY_CHANGE = BLOCKED
FORMAL_APPLY = BLOCKED
```

## Next allowed stage

```text
1013R_R223T_FIXTURE_ONLY_SANDBOX_PREVIEW
```

R223T is allowed only as fixture-only preview, not formal route implementation.

