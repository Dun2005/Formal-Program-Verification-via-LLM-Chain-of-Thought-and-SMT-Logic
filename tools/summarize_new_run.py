import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

print("=" * 80)
print("1. KẾT QUẢ TRÊN 10 BÀI TOÁN MBPP VỚI PIPELINE MỚI")
print("=" * 80)

with open("results/mbpp_experiment/all_results.json", "r", encoding="utf-8") as f:
    mbpp_data = json.load(f)

for item in mbpp_data:
    t_id = item["task_id"]
    name = item["name"]
    ast_res = item["anchored"]
    un_res = item["unanchored"]
    rej = ast_res.get("rejected_by_subset", False)
    reason = ast_res.get("subset_rejection_reason", "")
    if rej:
        print(f"Task {t_id:3d} ({name:25s}) | SUBSET_REJECT: {reason}")
    else:
        v_a = ast_res["n_verified"]
        ce_a = ast_res["n_counterexample"]
        un_a = ast_res["n_unreachable"]
        v_u = un_res["n_verified"]
        ce_u = un_res["n_counterexample"]
        print(f"Task {t_id:3d} ({name:25s}) | AST: V={v_a}, CE={ce_a}, UN={un_a} | UN: V={v_u}, CE={ce_u}")

print("\n" + "=" * 80)
print("2. KẾT QUẢ TRÊN BỘ PHỨC TẠP (COMPLEX SUITE) VỚI PIPELINE MỚI")
print("=" * 80)

with open("results/complex_experiment/all_complex_results.json", "r", encoding="utf-8") as f:
    complex_data = json.load(f)

for item in complex_data:
    p_id = item["id"]
    cat = item["category"]
    ast_res = item["ast_anchored"]
    un_res = item["unanchored"]
    rej = ast_res.get("rejected_by_subset", False)
    reason = ast_res.get("subset_rejection_reason", "")
    if rej:
        print(f"[{p_id:<28}] ({cat}) | SUBSET_REJECT: {reason}")
    else:
        v_a = ast_res["n_verified"]
        ce_a = ast_res["n_counterexample"]
        un_a = ast_res["n_unreachable"]
        unsup_a = ast_res["n_unsupported"] + ast_res["n_translation_error"]
        v_u = un_res["n_verified"]
        ce_u = un_res["n_counterexample"]
        unsup_u = un_res["n_unsupported"] + un_res["n_translation_error"]
        print(f"[{p_id:<28}] ({cat}) | AST: V={v_a}, CE={ce_a}, UN={un_a}, UNSUP={unsup_a} | UN: V={v_u}, CE={ce_u}, UNSUP={unsup_u}")
