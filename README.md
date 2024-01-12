## Графи

### Завдання 1

Створіть граф за допомогою бібліотеки networkX для моделювання певної реальної мережі (наприклад, транспортної мережі міста, соціальної мережі, інтернет-топології).

----
За основу взяв мапу міст Швейцарії.

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

-----

Найкоротший шлях в розробленому графі від`Geneve` до інших станцій: **{'Geneve': 0, 'Lausanne': 3, 'Friburg': 7, 'Yverdon-les-Bains': 6, 'Montreux': 8, 'Neuchatel': 8, 'Basel': 10, 'Bern': 10, 'Thun': 11, 'Interlaken': 13, 'Luzern': 12, 'Disentis': 15, 'Mantigny': 11, 'Sion': 13, 'Brig': 17, 'St.Moritz': 17, 'Chur': 16, 'St.Gallen': 20, 'Zurich': 15}** <br>
Найкоротший шлях в розробленому графі від`Lausanne` до інших станцій: **{'Geneve': 3, 'Lausanne': 0, 'Friburg': 4, 'Yverdon-les-Bains': 3, 'Montreux': 5, 'Neuchatel': 5, 'Basel': 7, 'Bern': 7, 'Thun': 8, 'Interlaken': 10, 'Luzern': 9, 'Disentis': 12, 'Mantigny': 8, 'Sion': 10, 'Brig': 14, 'St.Moritz': 14, 'Chur': 13, 'St.Gallen': 17, 'Zurich': 12}** <br>
Найкоротший шлях в розробленому графі від`Friburg` до інших станцій: **{'Geneve': 7, 'Lausanne': 4, 'Friburg': 0, 'Yverdon-les-Bains': 7, 'Montreux': 9, 'Neuchatel': 7, 'Basel': 9, 'Bern': 3, 'Thun': 4, 'Interlaken': 6, 'Luzern': 11, 'Disentis': 8, 'Mantigny': 12, 'Sion': 14, 'Brig': 11, 'St.Moritz': 10, 'Chur': 13, 'St.Gallen': 17, 'Zurich': 14}** <br>
Найкоротший шлях в розробленому графі від`Yverdon-les-Bains` до інших станцій: **{'Geneve': 6, 'Lausanne': 3, 'Friburg': 7, 'Yverdon-les-Bains': 0, 'Montreux': 8, 'Neuchatel': 2, 'Basel': 4, 'Bern': 6, 'Thun': 7, 'Interlaken': 9, 'Luzern': 6, 'Disentis': 11, 'Mantigny': 11, 'Sion': 13, 'Brig': 14, 'St.Moritz': 13, 'Chur': 10, 'St.Gallen': 14, 'Zurich': 9}** <br>
Найкоротший шлях в розробленому графі від`Montreux` до інших станцій: **{'Geneve': 8, 'Lausanne': 5, 'Friburg': 9, 'Yverdon-les-Bains': 8, 'Montreux': 0, 'Neuchatel': 10, 'Basel': 12, 'Bern': 12, 'Thun': 13, 'Interlaken': 14, 'Luzern': 14, 'Disentis': 12, 'Mantigny': 3, 'Sion': 5, 'Brig': 9, 'St.Moritz': 14, 'Chur': 17, 'St.Gallen': 21, 'Zurich': 17}** <br>
Найкоротший шлях в розробленому графі від`Neuchatel` до інших станцій: **{'Geneve': 8, 'Lausanne': 5, 'Friburg': 7, 'Yverdon-les-Bains': 2, 'Montreux': 10, 'Neuchatel': 0, 'Basel': 2, 'Bern': 4, 'Thun': 5, 'Interlaken': 7, 'Luzern': 4, 'Disentis': 9, 'Mantigny': 13, 'Sion': 15, 'Brig': 12, 'St.Moritz': 11, 'Chur': 8, 'St.Gallen': 12, 'Zurich': 7}** <br>
Найкоротший шлях в розробленому графі від`Basel` до інших станцій: **{'Geneve': 10, 'Lausanne': 7, 'Friburg': 9, 'Yverdon-les-Bains': 4, 'Montreux': 12, 'Neuchatel': 2, 'Basel': 0, 'Bern': 6, 'Thun': 7, 'Interlaken': 7, 'Luzern': 2, 'Disentis': 9, 'Mantigny': 15, 'Sion': 16, 'Brig': 12, 'St.Moritz': 11, 'Chur': 6, 'St.Gallen': 10, 'Zurich': 5}** <br>
Найкоротший шлях в розробленому графі від`Bern` до інших станцій: **{'Geneve': 10, 'Lausanne': 7, 'Friburg': 3, 'Yverdon-les-Bains': 6, 'Montreux': 12, 'Neuchatel': 4, 'Basel': 6, 'Bern': 0, 'Thun': 1, 'Interlaken': 3, 'Luzern': 8, 'Disentis': 5, 'Mantigny': 14, 'Sion': 12, 'Brig': 8, 'St.Moritz': 7, 'Chur': 10, 'St.Gallen': 14, 'Zurich': 11}** <br>
Найкоротший шлях в розробленому графі від`Thun` до інших станцій: **{'Geneve': 11, 'Lausanne': 8, 'Friburg': 4, 'Yverdon-les-Bains': 7, 'Montreux': 13, 'Neuchatel': 5, 'Basel': 7, 'Bern': 1, 'Thun': 0, 'Interlaken': 2, 'Luzern': 7, 'Disentis': 4, 'Mantigny': 13, 'Sion': 11, 'Brig': 7, 'St.Moritz': 6, 'Chur': 9, 'St.Gallen': 13, 'Zurich': 10}** <br>
Найкоротший шлях в розробленому графі від`Interlaken` до інших станцій: **{'Geneve': 13, 'Lausanne': 10, 'Friburg': 6, 'Yverdon-les-Bains': 9, 'Montreux': 14, 'Neuchatel': 7, 'Basel': 7, 'Bern': 3, 'Thun': 2, 'Interlaken': 0, 'Luzern': 5, 'Disentis': 2, 'Mantigny': 11, 'Sion': 9, 'Brig': 5, 'St.Moritz': 4, 'Chur': 7, 'St.Gallen': 11, 'Zurich': 8}** <br>
Найкоротший шлях в розробленому графі від`Luzern` до інших станцій: **{'Geneve': 12, 'Lausanne': 9, 'Friburg': 11, 'Yverdon-les-Bains': 6, 'Montreux': 14, 'Neuchatel': 4, 'Basel': 2, 'Bern': 8, 'Thun': 7, 'Interlaken': 5, 'Luzern': 0, 'Disentis': 7, 'Mantigny': 16, 'Sion': 14, 'Brig': 10, 'St.Moritz': 9, 'Chur': 4, 'St.Gallen': 8, 'Zurich': 3}** <br>
Найкоротший шлях в розробленому графі від`Disentis` до інших станцій: **{'Geneve': 15, 'Lausanne': 12, 'Friburg': 8, 'Yverdon-les-Bains': 11, 'Montreux': 12, 'Neuchatel': 9, 'Basel': 9, 'Bern': 5, 'Thun': 4, 'Interlaken': 2, 'Luzern': 7, 'Disentis': 0, 'Mantigny': 9, 'Sion': 7, 'Brig': 3, 'St.Moritz': 2, 'Chur': 5, 'St.Gallen': 9, 'Zurich': 10}** <br>
Найкоротший шлях в розробленому графі від`Mantigny` до інших станцій: **{'Geneve': 11, 'Lausanne': 8, 'Friburg': 12, 'Yverdon-les-Bains': 11, 'Montreux': 3, 'Neuchatel': 13, 'Basel': 15, 'Bern': 14, 'Thun': 13, 'Interlaken': 11, 'Luzern': 16, 'Disentis': 9, 'Mantigny': 0, 'Sion': 2, 'Brig': 6, 'St.Moritz': 11, 'Chur': 14, 'St.Gallen': 18, 'Zurich': 19}** <br>
Найкоротший шлях в розробленому графі від`Sion` до інших станцій: **{'Geneve': 13, 'Lausanne': 10, 'Friburg': 14, 'Yverdon-les-Bains': 13, 'Montreux': 5, 'Neuchatel': 15, 'Basel': 16, 'Bern': 12, 'Thun': 11, 'Interlaken': 9, 'Luzern': 14, 'Disentis': 7, 'Mantigny': 2, 'Sion': 0, 'Brig': 4, 'St.Moritz': 9, 'Chur': 12, 'St.Gallen': 16, 'Zurich': 17}** <br>
Найкоротший шлях в розробленому графі від`Brig` до інших станцій: **{'Geneve': 17, 'Lausanne': 14, 'Friburg': 11, 'Yverdon-les-Bains': 14, 'Montreux': 9, 'Neuchatel': 12, 'Basel': 12, 'Bern': 8, 'Thun': 7, 'Interlaken': 5, 'Luzern': 10, 'Disentis': 3, 'Mantigny': 6, 'Sion': 4, 'Brig': 0, 'St.Moritz': 5, 'Chur': 8, 'St.Gallen': 12, 'Zurich': 13}** <br>
Найкоротший шлях в розробленому графі від`St.Moritz` до інших станцій: **{'Geneve': 17, 'Lausanne': 14, 'Friburg': 10, 'Yverdon-les-Bains': 13, 'Montreux': 14, 'Neuchatel': 11, 'Basel': 11, 'Bern': 7, 'Thun': 6, 'Interlaken': 4, 'Luzern': 9, 'Disentis': 2, 'Mantigny': 11, 'Sion': 9, 'Brig': 5, 'St.Moritz': 0, 'Chur': 7, 'St.Gallen': 11, 'Zurich': 12}** <br>
Найкоротший шлях в розробленому графі від`Chur` до інших станцій: **{'Geneve': 16, 'Lausanne': 13, 'Friburg': 13, 'Yverdon-les-Bains': 10, 'Montreux': 17, 'Neuchatel': 8, 'Basel': 6, 'Bern': 10, 'Thun': 9, 'Interlaken': 7, 'Luzern': 4, 'Disentis': 5, 'Mantigny': 14, 'Sion': 12, 'Brig': 8, 'St.Moritz': 7, 'Chur': 0, 'St.Gallen': 4, 'Zurich': 7}** <br>
Найкоротший шлях в розробленому графі від`St.Gallen` до інших станцій: **{'Geneve': 20, 'Lausanne': 17, 'Friburg': 17, 'Yverdon-les-Bains': 14, 'Montreux': 21, 'Neuchatel': 12, 'Basel': 10, 'Bern': 14, 'Thun': 13, 'Interlaken': 11, 'Luzern': 8, 'Disentis': 9, 'Mantigny': 18, 'Sion': 16, 'Brig': 12, 'St.Moritz': 11, 'Chur': 4, 'St.Gallen': 0, 'Zurich': 5}** <br>
Найкоротший шлях в розробленому графі від`Zurich` до інших станцій: **{'Geneve': 15, 'Lausanne': 12, 'Friburg': 14, 'Yverdon-les-Bains': 9, 'Montreux': 17, 'Neuchatel': 7, 'Basel': 5, 'Bern': 11, 'Thun': 10, 'Interlaken': 8, 'Luzern': 3, 'Disentis': 10, 'Mantigny': 19, 'Sion': 17, 'Brig': 13, 'St.Moritz': 12, 'Chur': 7, 'St.Gallen': 5, 'Zurich': 0}** <br>