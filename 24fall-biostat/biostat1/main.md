# Random events and probability

## Random experiments

Properties of random experiments:

* repeatability: can be repeated under identical condition;
* clarity: all possible results can be clearly expressed;
* uncertainty: the result of one specific experiment cannot be predicted.

**Definition 1.1.1** The possible results of experiment S is a **sample point**, denoted ω ; The set comprised of all sample points is a **sample space** $\Omega$. A sample space can be finite countable, infinite countable or infinite uncountable. If $A\subseteq \Omega$, and $\Omega$ has finite sample points, A is called an **event**. When $\omega\in A$ we say A **happens** and vice versa. Usually upper-characters are used to denote events. An empty set is called an **impossible event**, and $\Omega$ is called a **certain event**.

The calculations of events include containment, union, intersection, complementation and theoretic difference, which is same as tradition. The definition of union and intersection can be extended to countable sets and uncountable sets.

## σ-algebra and probability

**Definition 1.1.2** The set comprised of subsets of S is called a **σ-algebra**, denoted as B, if it satisfies:

* $\emptyset \in B$ ;
* close to complementation;
* close to countable union.

Two common example is B={∅，S} and B={all subsets of S}.

**Definition 1.1.3** Kolmogorov's definition of probability function: Given sample space S and the sigma-algebra B, a probability function P is defined on B with the following axioms and is denoted probability space (S, B, P).

* P(A)≥0,∀A∈B
* P(S)=1
* If $A_1,A_2,\dots,\in B$ is unintersected sets, $P(\bigcup_{i=1}^\infty A_i)=\sum_{i=1}^\infty P(A_i)$

**Definition 1.1.4** S is a finite set S={s1,s2,⋯,sn} and B is a σ-algebra on S. If p1,p2,⋯,pn is a set of non-negative number with ∑i=1n=1 , for ∀A∈B , define the probability of A is P(A)=∑i:i∈Api , then P is the **probability function** on B. Similar definition is also valid for countable sample spaces. It's easy to prove that it satisfies the previous definition.

**Classical probability:** The sample space is finite, and the probability is $p(s_i)=p_i=1/n$ . The probability function is $P(A)=\frac{\# \text{ }of \text{ }elements \text{ }in \text{ }A}{\#\text{ } of\text{ } elements\text{ } in \text{ }S}$

**Property 1.1.1**(Formulas of probability) If P is a probability function and A, B is two sets from sigma-algebra, then:

* $P(A)=P(A\cap B)+P(A\cap \bar{B})$
* P(A∪B)=P(A)+P(B)−P(A∩B)
* P(A∩B)≤P(A)+P(B)
* P(A∩B)≥P(A)+P(B)−1 (Bonferroni inequality)
* ifA⊂B,P(A)≤P(B)
* For any partition of the sample space $C_1,C_2,\dots, P(A)=\sum_{i=1}^\infty P(A\cap C_i)$
* For ant sets $A_1,A_2,\dots, P(\bigcup_{i=1}^\infty)≤\sum_{i=1}^\infty P(A_i)$

## Conditional probability, Total probability and Bayesian probability

**Definition 1.1.5** If A, B is events in sample space S and P(B)>0, the **conditional probability** of A under B, denoted P(A|B), is defined as P(A|B)=P(A∩B)P(B) , and the sample space is reduced to B. Easy to prove the 3 axioms of probability.

Events A, B is called statistical independent, if P(A∩B)=P(A)P(B) . A set of events Ai is called mutually independent if for any sub combinations Aik , P(⋃j=1kAij)=∏j=1kP(Aij) .
