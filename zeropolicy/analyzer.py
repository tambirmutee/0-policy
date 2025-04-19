def analyze_csp(parsed_csp, lang):
    findings = []

    # Eksik temel direktifler
    required_directives = ["default-src", "script-src", "object-src"]
    for directive in required_directives:
        if directive not in parsed_csp:
            findings.append(lang["analyzer"]["missing_directive"].format(directive))

    # Tehlikeli kaynaklar
    dangerous_sources = [
        ("*", "critical"),
        ("data:", "medium"),
        ("blob:", "medium"),
        ("'unsafe-inline'", "high"),
        ("'unsafe-eval'", "high")
    ]

    for directive, sources in parsed_csp.items():
        for src in sources:
            for danger, _ in dangerous_sources:
                if danger in src:
                    findings.append(lang["analyzer"]["dangerous_source"].format(src, directive))

    # Raporlama eksikliği
    if "report-uri" not in parsed_csp and "report-to" not in parsed_csp:
        findings.append(lang["analyzer"]["no_reporting"])

    if not findings:
        findings.append(lang["analyzer"]["no_issues"])

    return findings
