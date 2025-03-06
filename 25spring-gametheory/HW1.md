# Problem 1 the Hawk-Dove Game

在“鹰-鸽”(Hawk-Dove)博弈中，两名博弈者各有两种可选策略：强硬攻击性的鹰派策略(H)，或者是温和退让性的鸽派策略(D)。从任意一名博弈者的角度，他的偏好如下：如果对方采取鹰派策略，他宁愿采取鸽派策略；如果对方采取鸽派策略，他则宁愿采用鹰派策略；给定他自己的策略（无论是鹰还是鸽），对方采取鸽派策略时他获得的获益比较大，对方采取鹰派策略时他的收益较小。

a. 根据以上描述画出这一博弈的收益矩阵（收益的具体数值可以自己任取，只要能表达上面的偏好次序即可。不妨把双方都采取鹰派策略时每个博弈者的收益定为 0。注意收益矩阵中标出双方的策略）。

| player 1\player 2 | Hawk | Dove |
| --- | --- | --- |
| Hawk | 0, 0 | 2, -1 |
| Dove | -1, 2 | 1, 1 |

b. 根据收益矩阵找到每个博弈者的最优反应函数（在收益矩阵上标明即可）。

For each player, f(H)=H, f(D)=H.

c. 纳什均衡是什么？

The Nash equilibrium is (H,H).

d. 简要解释为什么行动组合（鸽，鸽）不是纳什均衡。

Action profile (D,D) has lower payoff (1) when a player unilaterally changes his action to H (2).

# Problem 2 Circle Game

在游戏“棒子棒子鸡”中，两名博弈者各自可以在“棒子”、“老虎”、“鸡”、“虫子”中选择一种策略。按照规则，棒子胜老虎，老虎胜鸡，鸡胜虫子，虫子胜棒子。其他情况为平局。

a. 根据以上描述画出这一博弈的收益矩阵（注明对应的策略）。

| player 1\player 2 | stick | tiger | chicken | worm |
| --- | --- | --- | --- | --- |
| stick | 0, 0 | 1, -1 | 0,0 | -1, 1 |
| tiger | -1, 1 | 0, 0 | 1, -1 | 0, 0 |
| chicken | 0, 0 | -1, 1 | 0, 0 | 1, -1 |
| worm | 1, -1 | 0, 0 | -1, 1 | 0, 0 |

b. 根据收益矩阵，请标出每一位博弈者的最优反应函数。

For each player, f(stick)=worm, f(tiger)=stick, f(chicken)=tiger, f(worm)=chicken.

c. 本博弈有没有（单纯策略的）纳什均衡？

No. Proof: suppose there exists a NE of (a, b). When the second player remains b action, the first player can always find a strategy to win. If a is already the winning strategy, then for the second player, when the first player remains a action, he can choose the action winning over a (must be different from b). Then that is not a NE.

# Problem 3 Three-Player Game

下面的练习帮助我们学习如何用收益矩阵来表示三人参与的博弈并寻找纳什均衡。

考虑一个三人参与的“猎鹿博弈”。每个人可选的行动有两种：去捕牡鹿或是去捕野兔。牡鹿的个头很大，只有当三个人全都选择捕捉牡鹿时，才能捕捉成功，此时每个人的收益为 10。如果任何一个人选择去捕捉野兔，他都能够成功的为自己捕到野兔，获得收益 3；而此时其他选择捕捉牡鹿的博弈者的收益则为 0。

a.请按以下方法写出这个三人博弈的收益矩阵。先固定博弈者 3 的一种行动（例如“捕鹿”），写出此时博弈者 1 和博弈者 2 的不同行动构成的 2×2 的收益矩阵，注意在每一格（即每一种行动组合）中写出三名博弈者各自的收益。然后针对博弈者 3 的另一行动（例如“捕兔”），再写出另一个相应的 2×2 的收益矩阵。这样我们就用两个收益矩阵表达了这个三人博弈的所有的（2×2×2=8 个）行动组合及相应的收益。

Payoff matrix 1 (player 3 catching deer)

| player 1\player 2 | deer | rabbit |
| --- | --- | --- |
| deer | 10, 10, 10 | 0, 3, 0 |
| rabbit | 3, 0, 0 | 3, 3, 0 |

Payoff matrix 2 (player 3 catching rabbit)

| player 1\player 2 | deer | rabbit |
| --- | --- | --- |
| deer | 0, 0, 3 | 0, 3, 3 |
| rabbit | 3, 0, 3 | 3, 3, 3 |

b.找出每个人的最优反应函数。(根据最优反应的定义，设法在收益矩阵上依次确定博弈者 1、2、3 的最优反应。)

For each player, f(deer, deer)=deer, f(others)=rabbit.

c.本博弈的（单纯策略）纳什均衡有哪些？

There are two Nash equilibriums: (deer, deer, deer) and (rabbit, rabbit, rabbit).

# Problem 4 Generalized Cournot Duopoly

现在考虑n个厂商进行库诺特竞争。每一厂商选择自己生产的数量 $q_i$，供应市场的总量是 $Q=q_1+q_2+…+q_n$。厂商的生产成本为 $c·q_i$，其中c为常数。市场的需求函数（P是价格，a是常数且a>c）在不溢出的情况下遵循：$P(Q)=a-Q$；厂商的收益 $\pi_i(q_i, q_{-i})=P·q_i-c·q_i$. 

a. 写出厂商i的最优反应函数。

Gain function $\pi_i(q_i,q_{-i})=(a-c-q_{-i})q_i-q_i^2$. The extreme value point is $q_i=\frac{a-c-q_{-i}}{2}$, or $f(q_{-i})=\frac{a-c-q_{-i}}{2}$.

b. 根据最优反应函数求出纳什均衡。

The Nash equilibrium is the crossing point of all best response functions. That gives: $2q_i+\sum_{j\neq i}q_j=a-c$ for any i. Add all equations up we have: $(n+1)\sum q_i =n(a-c)$, and that solves $q_i=\frac{1}{n+1}(a-c)$.

c. 当n趋于无穷时，纳什均衡时的总产量接近多少？价格呢？厂商利润呢？

When n approaches infinity, the total product is $Q=\frac{n}{n+1}(a-c)\rightarrow (a-c)$; the price is $P=a-Q=c$; the profits are zero.