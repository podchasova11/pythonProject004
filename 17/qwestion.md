

<h1>SQL, Python, Go</h1>
<h2>Coding interview preparation</h2>
<p>Бесплатный набор данных, который помогает подготовиться к практической части собеседования. Основная тематика — анализ метрик (экономические, маркетинговые, показания датчиков). Проект существует около 20 лет и регулярно обновляется. Если вы первый раз на этом сайте, то настоятельно рекомендуется прочитать список <a href="https://aik84from.github.io/faq.html" target="_blank">часто задаваемых вопросов</a>.</p>


<h2>SQL</h2>

<h3>Как узнать версию PostgreSQL?</h3>

<pre>SELECT VERSION();</pre>

<h3>Как создать таблицу?</h3>

<pre>CREATE TABLE example (
    id SERIAL PRIMARY KEY,
    visitors INT
);</pre>

<h3>Как добавить данные в таблицу?</h3>

<pre>INSERT INTO example (id, visitors) VALUES
(1, 709),
(2, 749),
(3, 180),
(4, 518),
(5, 964),
(6, 180),
(7, 997),
(8, 562);</pre>

<h3>Как обновить запись?</h3>

<pre>UPDATE example SET visitors = 100 WHERE id = 8;</pre>

<h3>Как удалить запись?</h3>

<pre>DELETE FROM example WHERE id = 8;</pre>

<h3>Как узнать количество?</h3>

<pre>SELECT COUNT(*) FROM example;</pre>

<h3>Как найти среднее значение?</h3>

<pre>SELECT AVG(visitors) FROM example;</pre>

<h3>Как найти максимальное и минимальное значение?</h3>

<pre>SELECT MAX(visitors), MIN(visitors) FROM example;</pre>

<h3>Как найти дисперсию?</h3>

<pre>SELECT VARIANCE(visitors) FROM example;</pre>

<h3>Как найти сумму?</h3>

<pre>SELECT SUM(visitors) FROM example;</pre>

<h3>Как найти ТОП-5 самых больших значений?</h3>

<pre>SELECT * FROM example ORDER BY visitors DESC LIMIT 5;</pre>

<h3>Как найти все значения, которые находятся в нужном интервале?</h3>

<pre>SELECT * FROM example WHERE visitors BETWEEN 190 AND 800;</pre>

<h3>Как найти дубликаты?</h3>

<pre>SELECT
    COUNT(visitors),
    visitors
FROM example
GROUP BY visitors
HAVING COUNT(visitors) &gt; 1;</pre>

<h3>Как узнать ранг?</h3>

<pre>SELECT
    id,
    visitors,
    dense_rank() OVER (ORDER BY visitors DESC) AS rank
FROM example;</pre>

<h3>Как написать обобщённое табличное выражение?</h3>

<pre>WITH data AS (
    SELECT ARRAY[1, 2, 3, 4] AS alpha
)

SELECT * FROM data;</pre>

<h3>Как сделать сочетание двух строк?</h3>

<pre>SELECT 26 AS age
UNION ALL
SELECT 40 AS age;</pre>

<h3>Как написать свою функцию?</h3>

<pre>CREATE FUNCTION example_f(n integer)
RETURNS integer AS $$
BEGIN
    RETURN factorial(n);
END; $$
LANGUAGE plpgsql;</pre>

<h3>Как узнать размер таблицы?</h3>

<pre>SELECT pg_size_pretty(pg_relation_size(&#x27;example&#x27;)) relation_size;</pre>

<h3>Как создать индекс?</h3>

<pre>CREATE INDEX idx_example_visitors ON example(visitors);</pre>

<h3>Как получить план выполнения запроса?</h3>

<pre>EXPLAIN (ANALYZE)
SELECT * FROM example WHERE id IN (1, 5, 7);</pre>

<h3>Как скопировать таблицу?</h3>

<pre>CREATE TABLE backup_example AS TABLE example;</pre>

<h3>Как использовать полнотекстовый поиск?</h3>

<pre>CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    title VARCHAR(256)
);

INSERT INTO documents (id, title) VALUES
(1, &#x27;Better late than never&#x27;),
(2, &#x27;A good man is hard to find&#x27;),
(3, &#x27;Worrying never did anyone any good&#x27;);

ALTER TABLE documents 
ADD COLUMN title_gin tsvector
GENERATED ALWAYS AS (to_tsvector(&#x27;english&#x27;, title)) STORED;

CREATE INDEX idx_title_gin ON documents USING GIN (title_gin);

SELECT *
FROM documents
WHERE title_gin @@ to_tsquery(&#x27;english&#x27;, &#x27;never&#x27;);</pre>

<h3>Как найти данные с помощью регулярного выражения?</h3>

<pre>SELECT title, REGEXP_MATCHES(title, &#x27;never&#x27;) result FROM documents;</pre>

<h3>Как найти длину строки и контрольную сумму?</h3>

<pre>SELECT title, LENGTH(title), MD5(title) FROM documents;</pre>

<h2>Python</h2>

<h3>Как загрузить данные из файла в формате CSV?</h3>

<pre>import pandas as pd


df = pd.read_csv(&quot;example.csv&quot;)</pre>

<h3>Как посмотреть общую информацию о данных?</h3>

<pre>df.info()</pre>

<h3>Как отобразить первые 10 строк?</h3>

<pre>df.head(10)</pre>

<h3>Как отобразить крайние 10 строк?</h3>

<pre>df.tail(10)</pre>

<h3>Как отобразить случайные 10 строк?</h3>

<pre>df.sample(10)</pre>

<h3>Как узнать описательную статистику?</h3>

<pre>df.describe()</pre>

<h3>Как посмотреть медиану с учётом группы?</h3>

<pre>df.groupby(by=&quot;target&quot;).median()</pre>

<h3>Как посмотреть линейную корреляцию?</h3>

<pre>df[[&quot;alpha&quot;, &quot;beta&quot;]].corr()</pre>

<h3>Как посмотреть гистограмму распределения?</h3>

<pre>import matplotlib.pyplot as plt


df[&quot;alpha&quot;].hist(bins=50)
plt.show()</pre>

<h3>Как отобразить график?</h3>

<pre>df[&quot;alpha&quot;].plot()
plt.title(&quot;title&quot;)
plt.xlabel(&quot;xlabel&quot;) 
plt.ylabel(&quot;ylabel&quot;) 
plt.grid(True) 
plt.show()</pre>

<h3>Как визуально отобразить зависимость двух переменных?</h3>

<pre>plt.scatter(df[&quot;alpha&quot;], df[&quot;beta&quot;])
plt.show()</pre>

<h3>Как выполнить сортировку по убыванию?</h3>

<pre>df.sort_values(by=[&quot;alpha&quot;], ascending=False).head(10)</pre>

<h3>Как применить формулу, например, найти кинетическую энергию? (1)</h3>

<pre>df[&quot;kinetic_energy&quot;] = (df[&quot;alpha&quot;] * (df[&quot;beta&quot;]**2)) / 2</pre>

<h3>Как применить формулу, например, найти кинетическую энергию? (2)</h3>

<pre>import numpy as np


mass = np.linspace(1.0, 10.0, num=100)
velocity = np.linspace(1.0, 10.0, num=100)

# Показанный вариант более быстрый
kinetic_energy = 0.5 * (mass * np.power(velocity, 2))</pre>

<h3>Как сохранить таблицу в файл?</h3>

<pre>result = df[[&quot;alpha&quot;, &quot;beta&quot;, &quot;kinetic_energy&quot;]]

result.to_csv(&quot;result.csv&quot;, index=False)
result.to_json(&quot;result.json&quot;, orient=&quot;records&quot;, indent=4)
result.to_excel(&quot;result.xlsx&quot;)</pre>

<h3>Как получить данные из внешних API? (1)</h3>

<pre>import requests


try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.exceptions.ConnectionError as e:
    print(e)
except requests.exceptions.HTTPError as e:
    print(e)
except requests.exceptions.RequestException as e:
    print(e)</pre>

<h3>Как получить данные из внешних API? (2)</h3>

<pre>import httpx


try:
    response = httpx.get(url)
    response.raise_for_status()
    data = response.json()
    print(data)
except httpx.RequestError as e:
    print(e)
except httpx.HTTPStatusError as e:
    print(e)
except Exception as e:
    print(e)</pre>

<h3>Как получить данные из внешних API? (3)</h3>

<pre># Возможно, единичные локальные запросы проще делать в bash
# wget -O example https://example.com</pre>

<h3>Как получить данные из внешних API? (4)</h3>

<pre># Возможно, единичные локальные запросы проще делать в bash
# curl -o example http://www.example.com</pre>

<h3>Как воспользоваться кластерным анализом?</h3>

<pre>from sklearn.cluster import KMeans


kmeans = KMeans(n_clusters=2).fit(df[[&quot;alpha&quot;, &quot;beta&quot;]])
print(kmeans.cluster_centers_)
print(kmeans.labels_)</pre>

<h3>Как воспользоваться классификатором?</h3>

<pre>from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score


X = df[[&quot;alpha&quot;, &quot;beta&quot;]]
target = df[&quot;target&quot;]

model = RandomForestClassifier(n_estimators=1500, max_depth=200)
print(cross_val_score(model, X, target, cv=5, scoring=&quot;f1&quot;))</pre>

<h3>Как применить формулу (на ваш выбор) с помощью Polars?</h3>

<pre>import polars as pl


df = pl.read_csv(&quot;example.csv&quot;).select(
    (pl.col(&quot;alpha&quot;) - pl.col(&quot;beta&quot;)).alias(&quot;diff&quot;),
    pl.col(&quot;target&quot;).alias(&quot;target&quot;)
)

ctx = pl.SQLContext(data=df, eager=True)
print(ctx.execute(&quot;SELECT * FROM data LIMIT 5;&quot;))</pre>

<h2>Golang</h2>

<h3>Как найти расстояние между двумя точками на карте?</h3>

<pre>package main

import (
    &quot;fmt&quot;
    &quot;math&quot;
)

type Point struct {
    x float64
    y float64
}

func (p Point) getEuclideanDistance(q Point) float64 {
    return math.Sqrt(math.Pow(q.x - p.x, 2) + math.Pow(q.y - p.y, 2))
}

func main() {
    result := Point{17, 22}.getEuclideanDistance(Point{36, 72})
    fmt.Println(math.Abs(result - 53.488) &lt; 0.001)
}</pre>

<h3>Как написать поиск элемента в HashMap со сложностью O(1)?</h3>

<pre>package main

import &quot;fmt&quot;

type Url struct {
    id uint64
    score uint64
    url string
    title string
}

func main() {
    urls := make(map[string]Url)
    urls[&quot;august&quot;] = Url{1, 5, &quot;http://url_1&quot;, &quot;August&quot;}
    urls[&quot;september&quot;] = Url{2, 8, &quot;http://url_2&quot;, &quot;September&quot;}
    urls[&quot;october&quot;] = Url{3, 9, &quot;http://url_3&quot;, &quot;October&quot;}

    if item, ok := urls[&quot;september&quot;]; ok {
        fmt.Println(item)
    } else {
        fmt.Println(&quot;Not found&quot;)
    }
}</pre>

<h3>Как написать поиск элемента в Slice со сложностью O(n)?</h3>

<pre>func linearSearch(items []int, target int) int {
    for i, val := range items {
        if val == target {
            return i
        }
    }
    return -1
}</pre>

<h3>Как написать поиск элемента в Slice со сложностью O(log n)?</h3>

<pre>func binarySearch(items []int, target int) int {
    // В отличии от линейного поиска items должен быть заранее отсортирован
    low, high := 0, len(items) - 1
    for low &lt;= high {
        mid := low + (high-low)/2
        if items[mid] == target {
            return mid
        } else if items[mid] &lt; target {
            low = mid + 1
        } else {
            high = mid - 1
        }
    }
    return -1
}</pre>

<h3>Как эффективно искать запись в гигантских наборах данных?</h3>

<pre>/*
Лучше всего сохранить нужные данные в отдельную таблицу.
Это можно сделать следующими способами:

+ На этапе обработки больших данных в Apache Spark.
+ Отслеживание очередей, например, Apache Kafka [1].
+ Фоновыми запросами в PostgreSQL, ClickHouse, Elasticsearch, Tarantool [2].
+ Забрать из кэша (Apache Ignite, Redis, Memcached) [3].

[1] — при гигантских потоках данных, которые сложно сразу направить в СУБД.
[2] — из нужного ДЦ (балансировка на уровне DNS).
[3] — если у вас есть кэширование, например, рейтинга лучших товаров.

Если нужен именно алгоритм поиска, то тут много вариантов.
Допустим, в качестве индекса создать матрицу вершин графа и обойти её.
Или выполнить простой линейный поиск по интервалам в матрице:
*/

package main

import (
    &quot;fmt&quot;
)

var matrix [4][2]int = [4][2]int{
    {7, 10},
    {4, 15},
    {1, 23},
    {20, 8},
}

func main() {
    x := 11
    for i := 0; i &lt; 4; i++ {
        if matrix[i][0] &lt;= x &amp;&amp; matrix[i][1] &gt;= x {
            fmt.Println(&quot;result&quot;, matrix[i])
        }
    }
}</pre>

<h3>Как написать формулу сигмоиды для логистической регрессии?</h3>

<pre>func sigmoid(x float64) float64 {
    return 1.0 / (1 + math.Exp(-x))
}</pre>

<h2>JavaScript</h2>

<h3>Как написать простую библиотеку для закона Ома?</h3>

<pre>const volts = (amperes, ohms) =&gt; amperes * ohms;

const amperes = (volts, ohms) =&gt; volts / ohms;

const ohms = (volts, amperes) =&gt; volts / amperes;

const watts = (volts, amperes) =&gt; volts * amperes;

const voltageDivider = (volts, r1, r2) =&gt; volts * (r2 / (r1 + r2));


module.exports = {
    volts: volts,
    amperes: amperes,
    ohms: ohms,
    watts: watts,
    voltageDivider: voltageDivider
};</pre>

<h2>Bash</h2>

<h3>Как создать директорию?</h3>

<pre>mkdir example</pre>

<h3>Как рекурсивно скопировать директорию?</h3>

<pre>cp -r ./example ./example_2</pre>

<h3>Как посмотреть содержимое директории?</h3>

<pre>ls -ltrah</pre>

<h3>Как записать текст в файл?</h3>

<pre>cat &lt;&lt; EOF &gt; example.txt
EXAMPLE
EOF</pre>

<h3>Как узнать свободное место на диске?</h3>

<pre>df -h</pre>

<h3>Как посмотреть память? (свободное место)</h3>

<pre>free -h</pre>

<h3>Как посмотреть процессы?</h3>

<pre>ps -A</pre>

<h3>Как загрузить файл?</h3>

<pre>curl -o example_1.html --user-agent &quot;Bot&quot; https://example.com/</pre>

<h3>Как загрузить файл?</h3>

<pre>wget -O example_2.html -U &quot;Bot&quot; https://example.com/</pre>

<h3>Как посмотреть содержимое файла?</h3>

<pre>cat example_1.html | less</pre>

<h3>Как увидеть первые 5 строк?</h3>

<pre>head 5 example_1.html</pre>

<h3>Как увидеть крайние 5 строк?</h3>

<pre>tail 5 example_1.html</pre>

<h3>Как посчитать количество строк, слов и байт?</h3>

<pre>wc example_1.html</pre>

<h3>Как определить контрольную сумму?</h3>

<pre>md5sum example_1.html</pre>

<h3>Как определить контрольную сумму?</h3>

<pre>sha1sum example_1.html</pre>

<h3>Как найти в файле подстроку?</h3>

<pre>grep -r &quot;&lt;title&gt;&quot; *</pre>

<h3>Как искать файлы по расширению?</h3>

<pre>find ./ -iname &quot;*.html&quot;</pre>

<h3>Как создать архив?</h3>

<pre>tar -cvzf example.tar.gz ./</pre>

<h3>Как извлечь файлы из архива?</h3>

<pre>tar -xvzf example.tar.gz -C ./</pre>

<h3>Как зашифровать файл?</h3>

<pre>gpg -c example.tar.gz</pre>

<h3>Как расшифровать файл?</h3>

<pre>gpg -d example.tar.gz.gpg &gt; example-copy.tar.gz</pre>

</div>
</div>
</body>
</html>
