import sys
import os
import json

from zeropolicy.fetcher import get_csp_header
from zeropolicy.parser import parse_csp
from zeropolicy.analyzer import analyze_csp
from zeropolicy.config import load_config, update_setting
from zeropolicy.bypass_checker import check_bypass_weaknesses


def dil_secimi():
    print("🛡️  0-Policy – CSP Güvenlik Tarayıcısı 🕵️‍♂️")
    print("Lütfen dil seçiniz:")
    print("1) Türkçe")
    print("2) English")
    secim = input("Seçiminiz: ")

    if secim == "1":
        from zeropolicy.langs.tr import LANG
    elif secim == "2":
        from zeropolicy.langs.en import LANG
    else:
        print("Geçersiz seçim. Varsayılan olarak Türkçe seçildi.")
        from zeropolicy.langs.tr import LANG

    os.system("clear")
    return LANG


def menu_goster(lang):
    os.system("clear")
    print("\n" + lang["menu"]["title"])
    print(lang["menu"]["scan_single"])
    print(lang["menu"]["scan_multi"])
    print(lang["menu"]["settings"])
    print(lang["menu"]["exit"])
    secim = input(lang["prompt"])
    return secim


def rapor_olustur(output, lang, is_multiple=False, bypass_findings=None):
    cevap = input(lang["want_report"]).strip().lower()
    if cevap in ["e", "y"]:
        print(lang["choose_format"])
        secim = input(">> ").strip()
        config = load_config()
        report_dir = config.get("report_dir", ".")

        if secim == "1":
            filename = input(lang["json_filename_prompt"])
            full_path = os.path.join(report_dir, filename)
            try:
                if not is_multiple and bypass_findings:
                    output["bypass_findings"] = bypass_findings
                with open(full_path, "w", encoding="utf-8") as f:
                    json.dump(output, f, indent=4, ensure_ascii=False)
                print(lang["json_saved"].format(full_path))
            except Exception as e:
                print(f"❌ JSON yazım hatası: {e}")

        elif secim == "2":
            filename = input(lang["text_filename_prompt"])
            full_path = os.path.join(report_dir, filename)
            try:
                with open(full_path, "w", encoding="utf-8") as f:
                    if is_multiple:
                        for item in output:
                            f.write(f"URL: {item['url']}\n")
                            f.write(f"CSP Header: {item['csp_header']}\n")
                            f.write("Findings:\n")
                            for finding in item["findings"]:
                                f.write(f"  - {finding}\n")
                            f.write("\n" + "-" * 40 + "\n\n")
                    else:
                        f.write(f"URL: {output['url']}\n")
                        f.write(f"CSP Header: {output['csp_header']}\n")
                        f.write("Findings:\n")
                        for finding in output["findings"]:
                            f.write(f"  - {finding}\n")
                        if bypass_findings:
                            f.write("\n" + lang["bypass"]["title"] + "\n")
                            for fnd in bypass_findings:
                                sev = lang["bypass"]["severity"].get(fnd["severity"], fnd["severity"])
                                f.write(f"[{sev.upper()}] {fnd['directive']} → {fnd['description']}\n")
                                f.write(f" ↪️  {lang['bypass']['pattern']}: {fnd['pattern']}\n")
                                f.write(f" 🔗  {lang['bypass']['reference']}: {fnd['reference']}\n\n")
                print(lang["text_saved"].format(full_path))
            except Exception as e:
                print(f"❌ TXT yazım hatası: {e}")


def main():
    lang = dil_secimi()
    while True:
        secim = menu_goster(lang)

        if secim == "1":
            url = input(lang["enter_url"])
            print(lang["fetching"])
            csp = get_csp_header(url)
            if csp:
                print(lang["found_csp"])
                print("\n" + csp + "\n")
                parsed = parse_csp(csp)
                print(lang["parsed_header"])
                for directive, sources in parsed.items():
                    print(f"  {directive}: {', '.join(sources)}")
                print("\n" + lang["analyzing"])
                findings = analyze_csp(parsed, lang)
                for finding in findings:
                    print(f"  {finding}")
                bypass_findings = check_bypass_weaknesses(parsed)
                if bypass_findings:
                    print("\n" + lang["bypass"]["title"] + "\n")
                    for f in bypass_findings:
                        sev = lang["bypass"]["severity"].get(f["severity"], f["severity"])
                        print(f"[{sev.upper()}] {f['directive']} → {f['description']}")
                        print(f" ↪️  {lang['bypass']['pattern']}: {f['pattern']}")
                        print(f" 🔗  {lang['bypass']['reference']}: {f['reference']}\n")
                output = {
                    "url": url,
                    "csp_header": csp,
                    "directives": parsed,
                    "findings": findings
                }
                rapor_olustur(output, lang, bypass_findings=bypass_findings)
            else:
                print(lang["no_csp"])
            input("\n" + lang["continue_prompt"])

        elif secim == "2":
            file_path = input(lang["file_prompt"])
            try:
                with open(file_path, "r") as file:
                    urls = [line.strip() for line in file if line.strip()]
                all_results = []
                for url in urls:
                    print("\n🔗 " + lang["current_url"].format(url))
                    print(lang["fetching"])
                    csp = get_csp_header(url)
                    if csp:
                        print(lang["found_csp"])
                        print("\n" + csp + "\n")
                        parsed = parse_csp(csp)
                        print(lang["parsed_header"])
                        for directive, sources in parsed.items():
                            print(f"  {directive}: {', '.join(sources)}")
                        print("\n" + lang["analyzing"])
                        findings = analyze_csp(parsed, lang)
                        for finding in findings:
                            print(f"  {finding}")
                        bypass_findings = check_bypass_weaknesses(parsed)
                        if bypass_findings:
                            print("\n" + lang["bypass"]["title"] + "\n")
                            for f in bypass_findings:
                                sev = lang["bypass"]["severity"].get(f["severity"], f["severity"])
                                print(f"[{sev.upper()}] {f['directive']} → {f['description']}")
                                print(f" ↪️  {lang['bypass']['pattern']}: {f['pattern']}")
                                print(f" 🔗  {lang['bypass']['reference']}: {f['reference']}\n")
                    else:
                        parsed = {}
                        findings = [lang["no_csp"]]
                        print(lang["no_csp"])
                    all_results.append({
                        "url": url,
                        "csp_header": csp if csp else "",
                        "directives": parsed,
                        "findings": findings
                    })
                rapor_olustur(all_results, lang, is_multiple=True)
                input("\n" + lang["continue_prompt"])
            except FileNotFoundError:
                print(lang["file_not_found"])
                input("\n" + lang["continue_prompt"])

        elif secim == "3":
            while True:
                config = load_config()
                os.system("clear")
                print(lang["settings_menu"]["title"])
                print(f"1) {lang['settings_menu']['timeout']}: {config['timeout']} saniye")
                print(f"2) {lang['settings_menu']['user_agent']}: {config['user_agent']}")
                print(f"3) {lang['settings_menu']['report_dir']}: {config['report_dir']}")
                print(f"4) {lang['settings_menu']['back']}\n")

                secim = input(lang["settings_menu"]["prompt"]).strip()
                if secim == "1":
                    yeni_timeout = input("Yeni timeout (saniye): ").strip()
                    if yeni_timeout.isdigit():
                        update_setting("timeout", int(yeni_timeout))
                        print(lang["settings_menu"]["updated"])
                    else:
                        print(lang["settings_menu"]["invalid_input"])
                    input(lang["continue_prompt"])
                elif secim == "2":
                    yeni_ua = input("Yeni User-Agent: ").strip()
                    update_setting("user_agent", yeni_ua)
                    print(lang["settings_menu"]["updated"])
                    input(lang["continue_prompt"])
                elif secim == "3":
                    yeni_dir = input("Yeni rapor dizini (örnek: ./raporlar): ").strip()
                    update_setting("report_dir", yeni_dir)
                    print(lang["settings_menu"]["updated"])
                    input(lang["continue_prompt"])
                elif secim == "4":
                    break
                else:
                    print(lang["settings_menu"]["invalid_choice"])
                    input(lang["continue_prompt"])

        elif secim == "4":
            print(lang["done"])
            sys.exit()

        else:
            print(lang["invalid_choice"])
            input("\n" + lang["continue_prompt"])
