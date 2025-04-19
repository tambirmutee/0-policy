LANG = {
    "welcome": "🛡️  0-Policy – CSP Security Scanner 🕵️‍♂️",
    "choose_language": "Please select language:",
    "languages": {
        "1": "1) Turkish",
        "2": "2) English"
    },
    "menu": {
        "title": "Main Menu",
        "scan_single": "1) Scan a URL and analyze CSP",
        "scan_multi": "2) Scan multiple URLs from file",
        "settings": "3) Change settings",
        "exit": "4) Exit"
    },
    "prompt": "Enter your choice: ",
    "invalid_choice": "Invalid selection, please try again.",
    "enter_url": "Enter the URL to analyze: ",
    "fetching": "Fetching CSP header from URL...",
    "no_csp": "No CSP header found on this page.",
    "found_csp": "CSP header detected!",
    "analyzing": "Analyzing...",
    "done": "Operation completed.",
    "parsed_header": "🧩 Parsed Directives:\n",
    "continue_prompt": "Press Enter to continue...",

    "file_prompt": "Please enter the path to the file containing the URL list: ",
    "file_not_found": "File not found!",
    "current_url": "Processing: {}",

    "want_report": "Do you want to generate a report? (y/n): ",
    "choose_format": "Select report format:\n1) JSON\n2) TXT",
    "json_filename_prompt": "Enter JSON output filename (e.g., csp_report.json): ",
    "text_filename_prompt": "Enter TXT output filename (e.g., csp_report.txt): ",
    "json_saved": "JSON output saved to '{}'.",
    "text_saved": "TXT output saved to '{}'.",

    "settings_menu": {
        "title": "⚙️  Current Settings:",
        "timeout": "timeout",
        "user_agent": "user-agent",
        "report_dir": "report directory",
        "back": "Return to main menu",
        "prompt": "Select the setting you want to change: ",
        "updated": "✅ Updated!",
        "invalid_input": "❌ Invalid number.",
        "invalid_choice": "❌ Invalid choice."
    },

    "bypass": {
        "title": "🚨 CSP Bypass Weaknesses Detected:",
        "severity": {
            "low": "Low",
            "medium": "Medium",
            "high": "High",
            "critical": "Critical"
        },
        "pattern": "Pattern",
        "reference": "Reference"
    },

    "analyzer": {
        "no_issues": "✅ No obvious CSP vulnerabilities found.",
        "missing_directive": "Missing directive: {}",
        "dangerous_source": "Dangerous source '{}' used in → {}",
        "no_reporting": "Missing 'report-uri' or 'report-to' directive. No incident reporting possible."
    }
}
