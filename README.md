## Графи

### Завдання 1

Створіть граф за допомогою бібліотеки networkX для моделювання певної реальної мережі (наприклад, транспортної мережі міста, соціальної мережі, інтернет-топології).

----

![Swiss RailRoad Map](https://github.com/sergiishevchenko/goit-algo-hw-06/blob/main/img/SwissMap.png)

![Swiss RailRoad Schema](https://github.com/sergiishevchenko/goit-algo-hw-06/blob/main/img/SwissSchema.png)

Кількість вершин: 19 <br>
Кількість ребер: 23 <br>
Ступінь кожної вершини: <br>
Geneve: 1 <br>
Lausanne: 4 <br>
Friburg: 2 <br>
Yverdon-les-Bains: 2 <br>
Montreux: 2 <br>
Neuchatel: 3 <br>
Basel: 2 <br>
Bern: 3 <br>
Thun: 2 <br>
Interlaken: 3 <br>
Luzern: 4 <br>
Disentis: 4 <br>
Mantigny: 2 <br>
Sion: 2 <br>
Brig: 2 <br>
St.Moritz: 1 <br>
Chur: 3 <br>
St.Gallen: 2 <br>
Zurich: 2 <br>

![Graph](https://github.com/sergiishevchenko/goit-algo-hw-06/blob/main/img/Завдання_1.png)


### Завдання 2

Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі, який було розроблено у першому завданні.
Далі порівняйте результати виконання обох алгоритмів для цього графа, висвітлить різницю в отриманих шляхах. Поясніть, чому шляхи для алгоритмів саме такі.

-----

Начальна станція - "Geneve", остання станція - "St.Gallen". <br>

### DFS <br>
[['Geneve', 'Lausanne', 'Friburg', 'Bern', 'Neuchatel', 'Basel', 'Luzern', 'Interlaken', 'Disentis', 'Chur', 'St.Gallen'], ['Geneve', 'Lausanne', 'Friburg', 'Bern', 'Neuchatel', 'Basel', 'Luzern', 'Chur', 'St.Gallen'], ['Geneve', 'Lausanne', 'Friburg', 'Bern', 'Neuchatel', 'Basel', 'Luzern', 'Zurich', 'St.Gallen'], ['Geneve', 'Lausanne', 'Friburg', 'Bern', 'Thun', 'Interlaken', 'Luzern', 'Chur', 'St.Gallen'], ['Geneve', 'Lausanne', 'Friburg', 'Bern', 'Thun', 'Interlaken', 'Luzern', 'Zurich', 'St.Gallen'], ['Geneve', 'Lausanne', 'Friburg', 'Bern', 'Thun', 'Interlaken', 'Disentis', 'Chur', 'Luzern', 'Zurich', 'St.Gallen'], ['Geneve', 'Lausanne', 'Friburg', 'Bern', 'Thun', 'Interlaken', 'Disentis', 'Chur', 'St.Gallen'], ['Geneve', 'Lausanne', 'Yverdon-les-Bains', 'Neuchatel', 'Basel', 'Luzern', 'Interlaken', 'Disentis', 'Chur', 'St.Gallen'], ['Geneve', 'Lausanne', 'Yverdon-les-Bains', 'Neuchatel', 'Basel', 'Luzern', 'Chur', 'St.Gallen'], ['Geneve', 'Lausanne', 'Yverdon-les-Bains', 'Neuchatel', 'Basel', 'Luzern', 'Zurich', 'St.Gallen'], ['Geneve', 'Lausanne', 'Yverdon-les-Bains', 'Neuchatel', 'Bern', 'Thun', 'Interlaken', 'Luzern', 'Chur', 'St.Gallen'], ['Geneve', 'Lausanne', 'Yverdon-les-Bains', 'Neuchatel', 'Bern', 'Thun', 'Interlaken', 'Luzern', 'Zurich', 'St.Gallen'], ['Geneve', 'Lausanne', 'Yverdon-les-Bains', 'Neuchatel', 'Bern', 'Thun', 'Interlaken', 'Disentis', 'Chur', 'Luzern', 'Zurich', 'St.Gallen'], ['Geneve', 'Lausanne', 'Yverdon-les-Bains', 'Neuchatel', 'Bern', 'Thun', 'Interlaken', 'Disentis', 'Chur', 'St.Gallen'], ['Geneve', 'Lausanne', 'Montreux', 'Mantigny', 'Sion', 'Brig', 'Disentis', 'Interlaken', 'Thun', 'Bern', 'Neuchatel', 'Basel', 'Luzern', 'Chur', 'St.Gallen'], ['Geneve', 'Lausanne', 'Montreux', 'Mantigny', 'Sion', 'Brig', 'Disentis', 'Interlaken', 'Thun', 'Bern', 'Neuchatel', 'Basel', 'Luzern', 'Zurich', 'St.Gallen'], ['Geneve', 'Lausanne', 'Montreux', 'Mantigny', 'Sion', 'Brig', 'Disentis', 'Interlaken', 'Luzern', 'Chur', 'St.Gallen'], ['Geneve', 'Lausanne', 'Montreux', 'Mantigny', 'Sion', 'Brig', 'Disentis', 'Interlaken', 'Luzern', 'Zurich', 'St.Gallen'], ['Geneve', 'Lausanne', 'Montreux', 'Mantigny', 'Sion', 'Brig', 'Disentis', 'Chur', 'Luzern', 'Zurich', 'St.Gallen'], ['Geneve', 'Lausanne', 'Montreux', 'Mantigny', 'Sion', 'Brig', 'Disentis', 'Chur', 'St.Gallen']] <br>
### BFS <br>
[['Geneve', 'Lausanne', 'Yverdon-les-Bains', 'Neuchatel', 'Basel', 'Luzern', 'Chur', 'St.Gallen'], ['Geneve', 'Lausanne', 'Yverdon-les-Bains', 'Neuchatel', 'Basel', 'Luzern', 'Zurich', 'St.Gallen'], ['Geneve', 'Lausanne', 'Friburg', 'Bern', 'Neuchatel', 'Basel', 'Luzern', 'Chur', 'St.Gallen'], ['Geneve', 'Lausanne', 'Friburg', 'Bern', 'Neuchatel', 'Basel', 'Luzern', 'Zurich', 'St.Gallen'], ['Geneve', 'Lausanne', 'Friburg', 'Bern', 'Thun', 'Interlaken', 'Luzern', 'Chur', 'St.Gallen'], ['Geneve', 'Lausanne', 'Friburg', 'Bern', 'Thun', 'Interlaken', 'Luzern', 'Zurich', 'St.Gallen'], ['Geneve', 'Lausanne', 'Friburg', 'Bern', 'Thun', 'Interlaken', 'Disentis', 'Chur', 'St.Gallen'], ['Geneve', 'Lausanne', 'Montreux', 'Mantigny', 'Sion', 'Brig', 'Disentis', 'Chur', 'St.Gallen'], ['Geneve', 'Lausanne', 'Yverdon-les-Bains', 'Neuchatel', 'Basel', 'Luzern', 'Interlaken', 'Disentis', 'Chur', 'St.Gallen'], ['Geneve', 'Lausanne', 'Yverdon-les-Bains', 'Neuchatel', 'Bern', 'Thun', 'Interlaken', 'Luzern', 'Chur', 'St.Gallen'], ['Geneve', 'Lausanne', 'Yverdon-les-Bains', 'Neuchatel', 'Bern', 'Thun', 'Interlaken', 'Luzern', 'Zurich', 'St.Gallen'], ['Geneve', 'Lausanne', 'Yverdon-les-Bains', 'Neuchatel', 'Bern', 'Thun', 'Interlaken', 'Disentis', 'Chur', 'St.Gallen'], ['Geneve', 'Lausanne', 'Friburg', 'Bern', 'Neuchatel', 'Basel', 'Luzern', 'Interlaken', 'Disentis', 'Chur', 'St.Gallen'], ['Geneve', 'Lausanne', 'Friburg', 'Bern', 'Thun', 'Interlaken', 'Disentis', 'Chur', 'Luzern', 'Zurich', 'St.Gallen'], ['Geneve', 'Lausanne', 'Montreux', 'Mantigny', 'Sion', 'Brig', 'Disentis', 'Interlaken', 'Luzern', 'Chur', 'St.Gallen'], ['Geneve', 'Lausanne', 'Montreux', 'Mantigny', 'Sion', 'Brig', 'Disentis', 'Interlaken', 'Luzern', 'Zurich', 'St.Gallen'], ['Geneve', 'Lausanne', 'Montreux', 'Mantigny', 'Sion', 'Brig', 'Disentis', 'Chur', 'Luzern', 'Zurich', 'St.Gallen'], ['Geneve', 'Lausanne', 'Yverdon-les-Bains', 'Neuchatel', 'Bern', 'Thun', 'Interlaken', 'Disentis', 'Chur', 'Luzern', 'Zurich', 'St.Gallen'], ['Geneve', 'Lausanne', 'Montreux', 'Mantigny', 'Sion', 'Brig', 'Disentis', 'Interlaken', 'Thun', 'Bern', 'Neuchatel', 'Basel', 'Luzern', 'Chur', 'St.Gallen'], ['Geneve', 'Lausanne', 'Montreux', 'Mantigny', 'Sion', 'Brig', 'Disentis', 'Interlaken', 'Thun', 'Bern', 'Neuchatel', 'Basel', 'Luzern', 'Zurich', 'St.Gallen']] <br>

### Висновки

Як видно з результатів розрахунків отримані шляхи, які будують два алгоритми DFS (Depth-First Search) та BFS (Breadth-First Search) , відрізняються один від одного. Пов'язано це з тим, що DFS вибирає один із шляхів і досліджує його глибше, перш ніж переходити до інших шляхів, а BFS навпаки досліджує всі можливі шляхи на одному рівні, перш ніж переходити на наступний рівень.

### Завдання 3

Реалізуйте алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі: додайте у граф ваги до ребер та знайдіть найкоротший шлях між всіма вершинами графа.


