Инструкция:
 - обновить список пакетов
sudo apt-get update
- добавить ключ GPG для Docker
Добавьте официальный GPG ключ Docker:
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
- добавьте Docker репозиторий
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
- установить Docker
Теперь обновите индекс пакетов и установите последнюю версию Docker Engine, Docker CLI и Containerd:
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
- проверить установку
sudo docker run hello-world
- добавить пользователя в группу Docker
Чтобы запускать Docker без использования sudo, добавьте текущего пользователя в группу Docker:
sudo usermod -aG docker $USER
После этого перезагрузите систему sudo systemctl reboot
Теперь вы можете использовать Docker без необходимости вводить sudo.
- скачиваем имедж с докерхаба
docker pull nginx
посмотреть что образ скачался
docker image ls
- запуск контейнера
docker run nginx
- смотрим запущенные контейнеры
docker ps
- запуск в фоновом режиме
docker run -d nginx
- проброс портов
docker run -p 8080:80 -d nginx
- запуск с именем 
docker run -p 8080:80 -d --name myNginx nginx
- вход в контейнер
docker exec -it 310500c2e6ce bash
создать файл 
- информация по контейнеру
docker inspect 310500c2e6ce
- остановка контейнера
docker stop myNginx
- удаление контейнера
docker rm myNginx
- запуск и удаление после остановки
docker run --rm
- просмотр всех контейнеров
docker ps -a

Скачать докер-компоуз
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
- даем права
sudo chmod +x /usr/local/bin/docker-compose
- проверяем, что докер установлен
docker-compose --version
- запустим контейнер через докер-компоуз
docker-compose up
docker-compose up -d запуск в фоне
- основные команды докер-компоуз
логи 
docker compose logs -f
смотрим логи
docker logs mysql_db
- запускаем нашу бд
docker-compose up -d
- проверяем что запущена
docker ps
- подключаемся к БД
mysql -h hostname -u username -p

