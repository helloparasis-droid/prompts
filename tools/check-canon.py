#!/usr/bin/env python3
"""
اعتبارسنجی سازگاری فایل‌های کانال What If Prism با CANON.md

بررسی می‌کند:
  ۱. STYLE LOCK در همه جا با CANON یکی است (به‌جز SHEET VARIANT مجاز)
  ۲. متن PRISM TRANSITION در همه جا یکسان است
  ۳. علامت ممنوع `|` در اسکریپت‌های TTS نیست
  ۴. هر پلان فایل ویدیو در بازه‌ی سرعت مجاز است
  ۵. مدت کل در بازه‌ی ۵۵ تا ۵۹ ثانیه است
  ۶. افشای AI به‌عنوان «اجباری» معرفی نشده
  ۷. قرارداد نام‌گذاری شماره‌ی قسمت را دارد

اجرا:  python3 tools/check-canon.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANON = ROOT / "CANON.md"
FILES = {
    "01": ROOT / "01-what-if-prism-MASTER-PROMPT-v4.md",
    "02": ROOT / "02-VIDEO-01-FULL-PACKAGE-v2.md",
    "03": ROOT / "03-ONE-SHOT-AGENT-PROMPT-v2.md",
}

MIN_WPS, MAX_WPS = 2.2, 2.7
MIN_TOTAL, MAX_TOTAL = 55.0, 59.0

results = []


def norm(s: str) -> str:
    """فاصله‌ها را یکدست می‌کند تا شکستن خط باعث اختلاف کاذب نشود."""
    return re.sub(r"\s+", " ", s).strip()


def check(name: str, passed: bool, detail: str = "") -> bool:
    results.append((passed, name, detail))
    return passed


def load(p: Path) -> str:
    if not p.exists():
        check(f"فایل موجود است: {p.name}", False, "پیدا نشد")
        return ""
    return p.read_text(encoding="utf-8")


def main() -> int:
    canon = load(CANON)
    if not canon:
        print("CANON.md پیدا نشد — بررسی متوقف شد.")
        return 1

    texts = {k: load(v) for k, v in FILES.items()}

    # ── ۱. STYLE LOCK ──────────────────────────────────────────────
    m = re.search(r"```\n(Modern flat-cartoon illustration.*?)\n```", canon, re.S)
    if not m:
        check("STYLE LOCK در CANON پیدا شد", False)
        return report()
    canon_style = norm(m.group(1))
    check("STYLE LOCK در CANON پیدا شد", True, f"{len(canon_style)} کاراکتر")

    safe_tail = "free of faces, eyes and any critical detail."
    check(
        "STYLE LOCK شامل قانون سیف‌زون است",
        canon_style.endswith(safe_tail),
    )
    check(
        "قانون غلط «upper two-thirds» حذف شده",
        "upper two-thirds" not in canon_style,
    )

    # هر وقوع کامل STYLE LOCK در سه فایل باید با CANON یکی باشد.
    # تا پایان پاراگراف می‌خوانیم، نه تا اولین «no logo.» — وگرنه
    # بلوک بریده می‌شود و اختلاف کاذب گزارش می‌شود.
    sheet_tail = "Flat even neutral lighting on the reference sheet itself. No lettering, no numbers, no watermark, no borders."
    canon_sheet = canon_style.rsplit("Vertical 9:16 frame.", 1)[0].strip() + " " + sheet_tail

    for key, txt in texts.items():
        if not txt:
            continue
        occs = [
            norm(x)
            for x in re.findall(
                r"Modern flat-cartoon illustration.*?(?=\n\s*\n|\n```)", txt, re.S
            )
        ]
        occs = [o.rstrip('"') for o in occs]
        if not occs:
            continue
        bad = []
        for i, o in enumerate(occs, 1):
            if o == canon_style:
                continue                      # نسخه‌ی کامل
            if o == canon_sheet:
                continue                      # SHEET VARIANT مجاز
            bad.append(f"#{i} ({len(o)} کاراکتر)")
        check(
            f"STYLE LOCK در فایل {key} با CANON یکی است",
            not bad,
            f"{len(occs)} وقوع" + (f" — ناسازگار: {', '.join(bad)}" if bad else ""),
        )

    # ── ۲. PRISM TRANSITION ────────────────────────────────────────
    pm = re.search(r"```\n(PRISM TRANSITION: .*?)\n```", canon, re.S)
    if pm:
        canon_prism = norm(pm.group(1))
        check("PRISM TRANSITION در CANON پیدا شد", True)
        check(
            "PRISM از املای بریتانیایی centre استفاده می‌کند",
            "center" not in canon_prism.lower(),
        )
        for key, txt in texts.items():
            if not txt:
                continue
            occs = [
                norm(x)
                for x in re.findall(
                    r"PRISM TRANSITION: A single beam.*?against the light\.", txt, re.S
                )
            ]
            if not occs:
                continue
            mismatched = [i for i, o in enumerate(occs, 1) if o != canon_prism]
            check(
                f"PRISM در فایل {key} با CANON یکی است",
                not mismatched,
                f"{len(occs)} وقوع"
                + (f" — ناسازگار: {mismatched}" if mismatched else ""),
            )
    else:
        check("PRISM TRANSITION در CANON پیدا شد", False)

    # ── ۳. علامت ممنوع در TTS ──────────────────────────────────────
    vo = re.search(r"### نسخه‌ی A.*?```\n(.*?)\n```", texts.get("02", ""), re.S)
    if vo:
        body = vo.group(1)
        check("اسکریپت TTS علامت ممنوع `|` ندارد", "|" not in body)
        n_breaks = body.count("<break")
        check(
            "تعداد تگ break در حد مجاز است (≤۶)",
            n_breaks <= 6,
            f"{n_breaks} تگ",
        )
    else:
        check("اسکریپت VO نسخه‌ی A پیدا شد", False)

    check(
        "نسخه‌ی v3 بدون SSML ارائه شده",
        "[long pause]" in texts.get("02", ""),
    )

    # ── ۴ و ۵. زمان‌بندی پلان‌ها ────────────────────────────────────
    rows = re.findall(
        r"^\| (\d{2}) \| ([\d:.]+)–([\d:.]+) \| ([\d.]+)s \| .*? \| .*? \| (\d+) \| ([\d.]+) \|",
        texts.get("02", ""),
        re.M,
    )
    if rows:
        total = 0.0
        bad = []
        for num, _, _, dur, words, wps in rows:
            d, w, r = float(dur), int(words), float(wps)
            total += d
            calc = w / d
            if not (MIN_WPS <= calc <= MAX_WPS):
                bad.append(f"پلان {num}: {calc:.2f} w/s")
            elif abs(calc - r) > 0.02:
                bad.append(f"پلان {num}: عدد جدول {r} ≠ محاسبه {calc:.2f}")
        check(
            f"هر {len(rows)} پلان در بازه‌ی {MIN_WPS}–{MAX_WPS} w/s است",
            not bad,
            "; ".join(bad) if bad else "همه پاس",
        )
        check(
            f"مدت کل بین {MIN_TOTAL} و {MAX_TOTAL} ثانیه است",
            MIN_TOTAL <= total <= MAX_TOTAL,
            f"{total:.1f}s",
        )
        check(
            "تعداد پلان‌ها بین ۹ و ۱۳ است",
            9 <= len(rows) <= 13,
            f"{len(rows)} پلان",
        )
    else:
        check("جدول پلان‌بندی در فایل ۰۲ پیدا شد", False)

    # ── ۶. افشای AI ────────────────────────────────────────────────
    for key, txt in texts.items():
        if not txt:
            continue
        bad = re.search(r"افشای AI\s*(اجباری|الزامی)", txt) or re.search(
            r"(حتماً|حتما).{0,40}altered or synthetic", txt
        )
        check(f"افشای AI در فایل {key} «اجباری» معرفی نشده", not bad)

    # ── ۷. نام‌گذاری ───────────────────────────────────────────────
    # خطوطی که عمداً درباره‌ی نام غلط هشدار می‌دهند استثنا می‌شوند.
    for key, txt in texts.items():
        if not txt:
            continue
        bare = [
            ln
            for ln in txt.splitlines()
            if re.search(r"(?<![_\w\[])charsheet\.png", ln)
            and not re.search(r"bare|غلط|هشدار|overwrite", ln, re.I)
        ]
        check(
            f"نام‌گذاری فایل در {key} شماره‌ی قسمت دارد",
            not bare,
            bare[0].strip()[:60] if bare else "",
        )

    # ── ۸. تاریخ سیاست یوتیوب ──────────────────────────────────────
    for key, txt in texts.items():
        if not txt:
            continue
        wrong = re.search(r"یوتیوب از ۲۰۲۶", txt)
        check(f"تاریخ سیاست یوتیوب در {key} درست است", not wrong)

    return report()


def report() -> int:
    width = max(len(n) for _, n, _ in results) + 2
    failed = 0
    print("\n" + "═" * 72)
    print("  بررسی سازگاری با CANON")
    print("═" * 72)
    for ok, name, detail in results:
        mark = "✅" if ok else "❌"
        if not ok:
            failed += 1
        line = f"{mark}  {name.ljust(width)}"
        if detail:
            line += f" — {detail}"
        print(line)
    print("─" * 72)
    total = len(results)
    if failed:
        print(f"  {total - failed}/{total} پاس — {failed} مورد نیاز به اصلاح دارد")
    else:
        print(f"  همه‌ی {total} بررسی پاس شد")
    print("═" * 72 + "\n")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
