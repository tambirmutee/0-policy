LANG = {
    "welcome": "🛡️  0-Policy – CSP Güvenlik Tarayıcısı 🕵️‍♂️",
    "choose_language": "Lütfen dil seçiniz:",
    "languages": {
        "1": "1) Türkçe",
        "2": "2) English"
    },
    "menu": {
        "title": "Ana Menü",
        "scan_single": "1) URL tara ve CSP analiz et",
        "scan_multi": "2) Dosyadan çoklu URL tara",
        "settings": "3) Ayarları değiştir",
        "exit": "4) Çıkış"
    },
    "prompt": "Seçiminizi girin: ",
    "invalid_choice": "Geçersiz seçim, tekrar deneyin.",
    "enter_url": "Lütfen analiz etmek istediğiniz URL'yi girin: ",
    "fetching": "URL'den CSP başlığı alınıyor...",
    "no_csp": "Bu sayfada CSP başlığı bulunamadı.",
    "found_csp": "CSP başlığı bulundu!",
    "analyzing": "Analiz ediliyor...",
    "done": "İşlem tamamlandı.",
    "parsed_header": "🧩 Ayrıştırılmış Direktifler:\n",
    "continue_prompt": "Devam etmek için Enter'a basın...",

    "file_prompt": "Lütfen URL listesinin bulunduğu dosyanın yolunu girin: ",
    "file_not_found": "Dosya bulunamadı!",
    "current_url": "İşleniyor: {}",

    "want_report": "Rapor oluşturmak ister misiniz? (e/h): ",
    "choose_format": "Rapor formatını seçin:\n1) JSON\n2) TXT",
    "json_filename_prompt": "JSON çıktısı için dosya adı girin (örnek: csp_rapor.json): ",
    "text_filename_prompt": "TXT çıktısı için dosya adı girin (örnek: csp_rapor.txt): ",
    "json_saved": "JSON çıktısı '{}' dosyasına kaydedildi.",
    "text_saved": "TXT çıktısı '{}' dosyasına kaydedildi.",

    "settings_menu": {
        "title": "⚙️  Mevcut Ayarlar:",
        "timeout": "timeout",
        "user_agent": "user-agent",
        "report_dir": "rapor dizini",
        "back": "Ana menüye dön",
        "prompt": "Değiştirmek istediğiniz ayarı seçin: ",
        "updated": "✅ Güncellendi!",
        "invalid_input": "❌ Geçersiz sayı.",
        "invalid_choice": "❌ Geçersiz seçim."
    },

    "bypass": {
        "title": "🚨 CSP Bypass Zayıflıkları Tespit Edildi:",
        "severity": {
            "low": "Düşük",
            "medium": "Orta",
            "high": "Yüksek",
            "critical": "Kritik"
        },
        "pattern": "Örüntü",
        "reference": "Kaynak"
    },

    "analyzer": {
        "no_issues": "✅ Herhangi bir belirgin zafiyet tespit edilmedi.",
        "missing_directive": "Eksik direktif: {}",
        "dangerous_source": "Tehlikeli kaynak '{}' kullanılıyor → {}",
        "no_reporting": "report-uri veya report-to direktifi yok. Olay kaydı yapılamaz."
    }
}
