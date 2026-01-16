# Pentaas OneClick - Güvenlik Tarama ve Analiz Platformu

Pentaas OneClick, web uygulama ve ağ güvenliği testlerini otomatize eden, **mikroservis mimarisine** dayalı, Docker tabanlı, modüler bir ZA (Zafiyet Analizi) ve Pentest (Sızma Testi) orkestrasyon platformudur.

## 1. Yazılım Gereksinim Spesifikasyonu (SRS)

### 1.1 Amaç ve Kapsam
Bu sistem, güvenlik profesyonellerinin ve sistem yöneticilerinin tek bir arayüz üzerinden farklı derinliklerde (White, Gray, Black Box) otomatik taramalar yapmasını sağlar. Her güvenlik aracı bağımsız bir mikroservis olarak çalışır ve merkezi bir orkestratör tarafından yönetilir.

### 1.2 Fonksiyonel Gereksinimler
- **F1: Mikroservis Mimarisi:** Her güvenlik aracı bağımsız bir FastAPI servisi olarak çalışır
- **F2: Çoklu Tarama Profilleri:** White Box (Bilgi Toplama), Gray Box (Kimlik Doğrulama Odaklı) ve Black Box (Kapsamlı Saldırı) profillerini destekler
- **F3: Paralel Tarama:** Tüm araçlar eşzamanlı olarak çalışabilir
- **F4: Servis Sağlık Kontrolü:** Her servisin durumu `/health` endpoint'i ile kontrol edilebilir
- **F5: Veri Sürekliliği:** Tarama raporları ve ham veriler, benzersiz UUID'ler altında disk üzerinde kalıcı olarak saklanır

### 1.3 Sistem Gereksinimleri
- **İşletim Sistemi:** Linux (Ubuntu 20.04+ önerilir) veya Docker Desktop destekli Windows/macOS
- **Teknoloji Yığını:** Docker, Docker Compose (v2.x), Python 3.11, FastAPI, React 18, Nginx
- **Bağımlılıklar:** Docker ve Docker Compose kurulu olmalıdır

---

## 2. Mikroservis Mimarisi

### 2.1 Sistem Mimarisi

```
┌─────────────┐
│   Frontend  │
│  (React)    │
└──────┬──────┘
       │
       ▼
┌─────────────────┐      ┌─────────────┐
│    Backend      │◄────►│    Redis    │
│  Orchestrator   │      │   (Queue)   │
└────────┬────────┘      └─────────────┘
         │
         ├──────────────┬──────────────┬──────────────┐
         ▼              ▼              ▼              ▼
    ┌────────┐    ┌────────┐    ┌────────┐    ┌────────┐
    │  Nmap  │    │ Nuclei │    │TestSSL │    │  ...   │
    │ :8001  │    │ :8002  │    │ :8003  │    │ :8013  │
    └────────┘    └────────┘    └────────┘    └────────┘
```

### 2.2 Servis Listesi

Her araç bağımsız bir FastAPI servisi olarak çalışır:

| Servis | Port | Endpoint | Araç |
|--------|------|----------|------|
| nmap-service | 8001 | http://localhost:8001 | Nmap Port Scanner |
| nuclei-service | 8002 | http://localhost:8002 | Nuclei Vulnerability Scanner |
| testssl-service | 8003 | http://localhost:8003 | TestSSL SSL/TLS Analyzer |
| dirsearch-service | 8004 | http://localhost:8004 | Dirsearch Directory Scanner |
| nikto-service | 8005 | http://localhost:8005 | Nikto Web Server Scanner |
| whatweb-service | 8006 | http://localhost:8006 | WhatWeb Technology Detector |
| arjun-service | 8007 | http://localhost:8007 | Arjun Parameter Discovery |
| dalfox-service | 8008 | http://localhost:8008 | Dalfox XSS Scanner |
| wafw00f-service | 8009 | http://localhost:8009 | Wafw00f WAF Detector |
| dnsrecon-service | 8010 | http://localhost:8010 | DNSRecon DNS Enumeration |
| wpscan-service | 8011 | http://localhost:8011 | WPScan WordPress Scanner |
| zap-service | 8012 | http://localhost:8012 | OWASP ZAP Proxy |
| sslyze-service | 8013 | http://localhost:8013 | SSLyze SSL/TLS Scanner |

### 2.3 Servis API Endpoint'leri

Her servis aşağıdaki endpoint'leri sunar:

- `GET /health` - Servis sağlık kontrolü
- `GET /ready` - Servis hazır mı kontrolü
- `POST /scan` - Tarama başlat
- `GET /status/{scan_id}` - Tarama durumu
- `GET /results/{scan_id}` - Tarama sonuçları

**Örnek Kullanım:**
```bash
# Servis sağlık kontrolü
curl http://localhost:8001/health

# Tarama başlat
curl -X POST http://localhost:8001/scan \
  -H "Content-Type: application/json" \
  -d '{"target": "zaferkaraca.net", "options": {"scan_type": "white"}}'

# Sonuçları al
curl http://localhost:8001/results/{scan_id}
```

---

## 3. Tarama Profilleri ve Araç Seti

| Kategori | Strateji | Entegre Araçlar |
| :--- | :--- | :--- |
| **White Box** | Bilgi toplama ve hızlı yüzey taraması | Nmap, Nuclei, TestSSL, Dirsearch, Nikto, WhatWeb, Arjun, Dalfox, Wafw00f, DNSRecon |
| **Gray Box** | Uygulama mantığı ve yapılandırma analizi | Nmap, WPScan, ZAP Baseline, SSLyze |
| **Black Box** | Derinlemesine zafiyet tespiti ve exploit analizi | Nmap (Full), Nuclei (Full), Nikto |

---

## 4. Kurulum ve Dağıtım

### 4.1 Hızlı Başlangıç

```bash
# Projeyi klonlayın
git clone <repository-url>
cd pentaas-oneclick

# Tüm servisleri başlatın
docker compose up --build -d

# Servislerin durumunu kontrol edin
docker compose ps

# Logları izleyin
docker compose logs -f
```

### 4.2 Bireysel Servis Yönetimi

```bash
# Sadece belirli servisleri başlat
docker compose up -d nmap-service nuclei-service

# Bir servisi yeniden başlat
docker compose restart nmap-service

# Servis loglarını görüntüle
docker compose logs -f nmap-service

# Tüm servisleri durdur
docker compose down
```

---

## 5. Kullanım (Usage)

### 5.1 Web Arayüzü

1. Arayüzü açın: `http://localhost` (veya sunucu IP adresiniz)
2. **Target** kısmına hedef IP veya alan adını girin (Örn: `zaferkaraca.net` veya `192.168.1.1`)
3. **Profile** kısmından (White, Gray, Black) birini seçin
4. **Start Scan** butonuna basın
5. Tarama tamamlandığında **Reports** sekmesinden zafiyet detaylarını inceleyin

### 5.2 API Kullanımı

```bash
# Backend orchestrator üzerinden tarama başlat
curl -X POST http://localhost:8000/api/scan \
  -H "Content-Type: application/json" \
  -d '{"ip": "zaferkaraca.net", "category": "white"}'

# Tüm servislerin sağlık durumunu kontrol et
for port in {8001..8013}; do
  echo "Port $port:"
  curl -s http://localhost:$port/health | jq
done
```

---

## 6. Proje Yapısı

```text
pentaas-oneclick/
├── backend/
│   ├── main.py              # Backend Orchestrator
│   ├── engine.py            # Scan Engine (Legacy)
│   ├── worker.py            # RQ Worker
│   └── services/            # Mikroservisler
│       ├── base/
│       │   ├── tool_service.py    # Base Service Class
│       │   └── models.py          # Shared Models
│       ├── nmap/
│       │   ├── Dockerfile
│       │   ├── service.py
│       │   └── requirements.txt
│       ├── nuclei/
│       │   ├── Dockerfile
│       │   ├── service.py
│       │   └── requirements.txt
│       └── ... (11 more services)
├── frontend/
│   ├── src/                 # UI Components
│   └── public/              # Static Assets
├── nginx/
│   └── nginx.conf           # Reverse Proxy
├── docker-compose.yml       # 13 Tool Services + Infrastructure
└── README.md
```

---

## 7. Geliştirme ve Katkı

### 7.1 Yeni Araç Ekleme

1. `backend/services/` altında yeni klasör oluşturun
2. `service.py` dosyasını `BaseToolService` sınıfından türeterek oluşturun
3. `Dockerfile` ve `requirements.txt` ekleyin
4. `docker-compose.yml` dosyasına yeni servisi ekleyin

### 7.2 Servis Geliştirme

Her servis `BaseToolService` sınıfını extend eder:

```python
from services.base.tool_service import BaseToolService

class MyToolService(BaseToolService):
    def __init__(self):
        super().__init__(service_name="mytool", version="1.0.0")
    
    async def scan(self, target: str, options: dict) -> dict:
        # Tool execution logic
        return {
            "findings": [...],
            "raw_output": "...",
            "metadata": {...}
        }
```

---

## 8. Sorun Giderme

### Servis Başlatma Sorunları

```bash
# Servislerin durumunu kontrol et
docker compose ps

# Belirli bir servisin loglarını incele
docker compose logs nmap-service

# Servisi yeniden build et
docker compose build --no-cache nmap-service
docker compose up -d nmap-service
```

### Port Çakışmaları

Eğer 8001-8013 portları kullanımdaysa, `docker-compose.yml` dosyasında port numaralarını değiştirin.

---

*Bu doküman, mikroservis mimarisine geçişle birlikte güncellenmiştir. Her araç artık bağımsız bir FastAPI servisi olarak çalışmaktadır.*

