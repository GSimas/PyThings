# linear_regression
Este código é um "How to" para regressões lineares.


## Visão geral

Este código usa um pequeno dataset (base de dados) que mostra a relação entre notas de alunos e horas dedicadas de estudo. Intuitivamente existe uma relação certo ? É senso comum, que tem estuda por mais tempo, tem melhores notas. Vamos usar a regressão linear para provar o senso comum. 

Alguns links que podem te ajudar:

#### Visualização do Gradiente Descendente
https://raw.githubusercontent.com/mattnedrich/GradientDescentExample/master/gradient_descent_example.gif


#### Fórmula que calcula a distância dos quadrados/erro (otimização da reta linear)
https://spin.atomicobject.com/wp-content/uploads/linear_regression_error1.png

#### Derivadas parciais de  b e m 
https://spin.atomicobject.com/wp-content/uploads/linear_regression_gradient1.png

## Dependências do algoritmo

* numpy

Python 2 e 3 ambos podem ser usados. Use [pip](https://pip.pypa.io/en/stable/) para instalar qualquer dependência.

## Uso

Rode python assim ``python3 demo.py`` e veja os resultados:

   ```
Iniciando gradiente descendente de b = 0, m = 0, error = 5565.107834483211
Calculando...
Depois de 1000 iterações temos b = 0.08893651993741346, m = 1.4777440851894448, error = 112.61481011613473
   ```

## Créditos

## Siraj Raval - How to make prediction 
https://www.youtube.com/watch?v=vOppzHpvTiQ&index=1&list=PL2-dafEMk2A7YdKv4XfKpfbTH5z6rEEj3
