import json
import os

def load_bypass_patterns():
    # data klasöründen göreli olarak dosyayı al
    pattern_path = os.path.join(os.path.dirname(__file__), "..", "data", "bypass_patterns.json")
    with open(pattern_path, "r", encoding="utf-8") as f:
        return json.load(f)

def check_bypass_weaknesses(parsed_csp):
    patterns = load_bypass_patterns()
    findings = []

    for pattern in patterns:
        for directive, sources in parsed_csp.items():
            if directive in pattern["applies_to"]:
                for src in sources:
                    if pattern["pattern"] in src:
                        findings.append({
                            "directive": directive,
                            "pattern": pattern["pattern"],
                            "severity": pattern["severity"],
                            "description": pattern["description"],
                            "reference": pattern["reference"]
                        })

    return findings
