Grafana Stack, включая Grafana, Prometheus и Loki, представляет собой мощное решение для мониторинга и анализа данных в реальном времени. Рассмотрим основные компоненты и шаги по установке и настройке Grafana Stack.

### Основные компоненты Grafana Stack

1. **Grafana**: Это визуализация и интерфейс для анализа данных. Grafana позволяет создавать дашборды на основе различных источников данных.

2. **Prometheus**: Это система мониторинга и оповещения, которая собирает и хранит метрики в формате временных рядов. Prometheus отлично подходит для мониторинга приложений и серверов.

3. **Loki**: Это система для сбора, хранения и поиска логов. Loki интегрируется с Grafana, позволяя комбинировать логи и метрики на одном дашборде.

### Установка Grafana Stack

#### 1. Установка Docker (опционально)

Если вы хотите использовать Docker, сначала установите его:

```bash
sudo apt update
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker
```

#### 2. Установка Prometheus

Создайте конфигурационный файл `prometheus.yml`:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']
```

Запустите Prometheus с помощью Docker:

```bash
docker run -d --name=prometheus -p 9090:9090 -v $PWD/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
```

#### 3. Установка Grafana

Запустите Grafana с помощью Docker:

```bash
docker run -d --name=grafana -p 3000:3000 grafana/grafana
```

После этого вы можете получить доступ к Grafana через браузер по адресу `http://localhost:3000`. Стандартные учетные данные: `admin/admin`.

#### 4. Установка Loki

Создайте конфигурационный файл `loki-config.yaml`:

```yaml
auth_enabled: false
server:
  http_listen_port: 3100
  http_compress_response: true
  grpc_listen_port: 9095
  
ingester:
  chunk_idle_period: 5m
  max_chunk_age: 1h
```

Запустите Loki с помощью Docker:

```bash
docker run -d --name=loki -p 3100:3100 -v $PWD/loki-config.yaml:/etc/loki/loki.yaml grafana/loki:latest -config.file=/etc/loki/loki.yaml
```

### Настройка Grafana

1. **Подключение источников данных**:
   - Перейдите в раздел **Configuration > Data Sources**.
   - Добавьте Prometheus (URL: `http://prometheus:9090`) и Loki (URL: `http://loki:3100`).

2. **Создание дашборда**:
   - Перейдите в **Dashboard > New Dashboard**.
   - Добавьте панели, выбрав запрашиваемые метрики из Prometheus или логи из Loki.

3. **Персонализация дашбордов**:
   - Настройте отображение панелей, изменяйте их типы, устанавливайте алерты и используйте переменные для общего управления.

### Заключение

Grafana Stack предоставляет мощные инструменты для мониторинга и анализа данных в реальном времени. Следуя вышеописанным шагам, вы сможете настроить Grafana Stack для ваших нужд. Вы также можете расширить функциональность системы, интегрируя другие источники данных и системы оповещения, такие как Alertmanager для Prometheus.

