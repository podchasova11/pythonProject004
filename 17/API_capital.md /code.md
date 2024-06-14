### Какие API у вас есть?
На Capital.com мы предлагаем как REST, так и WebSocket API. В случае WebSocket API цены обновляются в режиме реального времени максимум для 40 инструментов одновременно.

### Есть ли у вас какие-либо ограничения на ваш API?
Да, у нас есть ограничения в нашем API Capital.com. Вот список:

У вас есть максимум 100 попыток в 24 часа для успешной генерации ключей API.
Максимальная частота запросов составляет 10 запросов в секунду на одного пользователя.
Максимальная частота запросов составляет 1 на 0,1 секунды на пользователя при открытии позиций или создании ордеров. В противном случае запросы позиций/ордеров будут отклонены.
Продолжительность сеанса WebSocket — 10 минут . Чтобы поддерживать сеанс в реальном времени, используйте конечную точку ping.
Сеанс REST также активен в течение 10 минут . Если ваше бездействие превышает этот период, при следующем запросе произойдет ошибка.
POST /sessionОграничение конечной точки составляет 1 запрос в секунду на каждый ключ API.
POST /positionsи POST /workingordersлимит конечной точки составляет 1000 запросов в час в демо-счете.
POST /accounts/topUpОграничения на конечные точки: 10 запросов в секунду и 100 запросов на аккаунт в день .
Баланс демо-счета не может превышать 100000.
API WebSocket позволяет подписаться максимум на 40 инструментов .
Потоковая передача WebSocket прекращается при изменении финансового счета с помощью PUT​ /sessionконечной точки.
### Поддерживает ли ваш API все инструменты?
Да, Capital.com API поддерживает все инструменты, которые вы можете найти на платформе.

### Как начать использовать API Capital.com?
Чтобы начать использовать наш API Capital.com, вам необходимо сначала создать ключ API в разделе Settings> API integrationsна платформе. После этого вы сможете использовать этот ключ и учетные данные своей учетной записи для авторизации использования API с помощью этого POST /sessionметода.