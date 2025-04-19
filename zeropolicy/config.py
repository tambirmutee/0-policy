import json
import os

# config.json dosyasının path'i (data klasörü içinde)
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "config.json")

def load_config():
    """config.json dosyasını yükler ve sözlük olarak döner."""
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def update_setting(key, value):
    """Belirli bir ayarı günceller ve config.json dosyasını yazar."""
    config = load_config()
    config[key] = value
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
