import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = [
    "R223S_opt_in_sandbox_route_spec.md",
    "R223S_fixture_data_contract.md",
    "R223S_preview_surface_spec.md",
    "R223S_v0_1_vs_v0_2_comparison_spec.md",
    "R223S_review_ledger_preview_policy.md",
    "R223S_safety_flags_contract.json",
    "R223S_blocked_scope_and_hold_conditions.md",
    "R223S_acceptance_criteria.md",
    "R223S_decision_report.md",
    "README_FOR_GPT_REVIEW.md",
    "PACKAGE_MANIFEST.json",
]

FALSE_KEYS = [
    "schema_v0_2_published",
    "r97b_modified",
    "formal_route_added",
    "frontend_backend_modified",
    "runtime_connected",
    "provider_model_connected",
    "prompt_modified",
    "database_written",
    "lesson_body_written",
    "existing_teacher_drafts_modified",
    "r222d_component_library_modified",
    "formal_apply",
]

TRUE_KEYS = [
    "fixture_only",
    "non_persistent_preview",
]

REQUIRED_DECISIONS = [
    "PASS_CONTINUE_TO_R223T_FIXTURE_ONLY_SANDBOX_PREVIEW",
    "HOLD_FOR_SANDBOX_SPEC_REDUCTION",
    "HOLD_FORMAL_V0_2_NOT_READY",
]

REQUIRED_PHRASES = [
    "independent opt-in sandbox",
    "fixture-only",
    "non-persistent preview",
    "teacher_confirmed=false",
    "formal_apply_allowed=false",
    "no lesson body writeback",
    "teacher default draft preview",
    "review ledger summary",
    "v0.1 / v0.2",
    "component trigger status",
    "screen / learning sheet / evidence",
    "R223M_STANDARD_V0_2 = NOT_PUBLISHED",
    "R97B_ROUTE = BLOCKED",
    "RUNTIME_PROVIDER_MODEL_PROMPT_DB = BLOCKED",
]

BANNED_PHRASES = [
    "R223M_STANDARD_V0_2 = PUBLISHED",
    "FORMAL_UI = ALLOWED",
    "R97B_ROUTE = ALLOWED",
    "teacher_confirmed=true",
    "formal_apply_allowed=true",
    "database_written=true",
    "lesson_body_written=true",
]

def read_text(name):
    return (ROOT / name).read_text(encoding="utf-8")

def main():
    failures = []
    checks = 0

    for name in REQUIRED_FILES:
        checks += 1
        if not (ROOT / name).exists():
            failures.append(f"missing required file: {name}")

    combined = "\n".join(read_text(name) for name in REQUIRED_FILES if (ROOT / name).exists() and name.endswith((".md", ".json")))

    for decision in REQUIRED_DECISIONS:
        checks += 1
        if decision not in combined:
            failures.append(f"missing decision output: {decision}")

    for phrase in REQUIRED_PHRASES:
        checks += 1
        if phrase not in combined:
            failures.append(f"missing required phrase: {phrase}")

    for phrase in BANNED_PHRASES:
        checks += 1
        if phrase in combined:
            failures.append(f"forbidden phrase present: {phrase}")

    safety_path = ROOT / "R223S_safety_flags_contract.json"
    if safety_path.exists():
        safety = json.loads(safety_path.read_text(encoding="utf-8"))
        for key in FALSE_KEYS:
            checks += 1
            if safety.get(key) is not False:
                failures.append(f"safety flag must be false: {key}")
        for key in TRUE_KEYS:
            checks += 1
            if safety.get(key) is not True:
                failures.append(f"safety flag must be true: {key}")
        checks += 1
        if safety.get("teacher_confirmed") is not False:
            failures.append("teacher_confirmed must be false")
        checks += 1
        if safety.get("formal_apply_allowed") is not False:
            failures.append("formal_apply_allowed must be false")
        checks += 1
        if safety.get("pilot_route_type") != "opt_in_sandbox_spec_only":
            failures.append("pilot_route_type mismatch")

    manifest_path = ROOT / "PACKAGE_MANIFEST.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        checks += 1
        if manifest.get("stage_id") != "1013R_R223S_OPT_IN_SANDBOX_ROUTE_SPEC":
            failures.append("manifest stage_id mismatch")
        checks += 1
        if manifest.get("decision") != "PASS_CONTINUE_TO_R223T_FIXTURE_ONLY_SANDBOX_PREVIEW":
            failures.append("manifest decision mismatch")
        for key in [
            "schema_v0_2_published",
            "formal_ui",
            "r97b_modified",
            "formal_route_added",
            "frontend_backend_modified",
            "runtime_connected",
            "provider_model_connected",
            "prompt_modified",
            "database_written",
            "lesson_body_written",
            "existing_teacher_drafts_modified",
            "r222d_component_library_modified",
            "formal_apply",
        ]:
            checks += 1
            if manifest.get("boundaries", {}).get(key) is not False:
                failures.append(f"manifest boundary must be false: {key}")

    result = {
        "passed": not failures,
        "check_count": checks,
        "failed": len(failures),
        "failures": failures,
        "decision": "PASS_CONTINUE_TO_R223T_FIXTURE_ONLY_SANDBOX_PREVIEW",
    }
    (ROOT / "validate_1013R_R223S_opt_in_sandbox_route_spec_result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if not failures else 1)

if __name__ == "__main__":
    main()

