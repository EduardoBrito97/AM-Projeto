# Projeto Aprendizagem de Máquina CIn-UFPE 2020.1
Replicação do artigo 'From neighbors to strengths - the k-strongest strengths (kSS) classification algorithm', disponível em https://doi.org/10.1016/j.patrec.2020.06.020, para o projeto da cadeira de Aprendizagem de Máquina, com o professor George Darmiton da Cunha Cavalcanti.

[Link](https://www.overleaf.com/9922382639qvdrrdyjgwhc) para o relatório em LaTeX.

Grupo:
* Eduardo Barreto Brito (ebb2);
* Juliana do Nascimento Damurie da Silva (jnds);
* Lucas Augusto Mota de Alcantara (lama2);
* Natália Souza Soares (nss2).

Datasets retirados do [UCI Repository](https://archive.ics.uci.edu/ml/index.php):
* [Ecoli](https://archive.ics.uci.edu/ml/datasets/Ecoli)
* [Glass Identification](https://archive.ics.uci.edu/ml/datasets/Glass+Identification)
* [Haberman's Survival](https://archive.ics.uci.edu/ml/datasets/Haberman%27s+Survival)
* [Ionosphere](https://archive.ics.uci.edu/ml/datasets/Ionosphere)
* [Iris](https://archive.ics.uci.edu/ml/datasets/Iris)
* [Pima](https://www.kaggle.com/uciml/pima-indians-diabetes-database)
* [Sonar](https://archive.ics.uci.edu/ml/datasets/Connectionist+Bench+%28Sonar%2C+Mines+vs.+Rocks%29)
* [Thyroid](https://archive.ics.uci.edu/ml/datasets/Thyroid+Disease)
* [Vehicle](https://archive.ics.uci.edu/ml/datasets/Statlog+%28Vehicle+Silhouettes%29)
* [WDBC](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29)
* [Wine](https://archive.ics.uci.edu/ml/datasets/Wine)

Alguns datasets mudaram de número de features, assim como não estão mais disponíveis no site indicado pelo artigo (aqui indicados como os que não possuem links). Os modificados foram:
* Ecoli: 7 features (no artigo) -> 8 features (atualmente)
* Glass Identification: 9 features (no artigo) -> 10 features (atualmente)
* WDBC (Breast Cancer Wisconsin (Diagnostic)) -> 30 features (no artigo) -> 32 features (atualmente)

Além disso, [Thyroid](https://archive.ics.uci.edu/ml/datasets/Thyroid+Disease) possui mais de um dataset, e o escolhido foi o 'new-thyroid'.

Para avaliação, foi utilizado um K = 7 para o KSS (K Strongest Strengths) e o 10-Fold Cross-Validation.

Os algoritmos utilizados para comparação com o algoritmo do artigo são:
* kNN, com K = 7, da biblioteca SKLearn, documentado [neste link](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html);
* DWkNN (Distance Weighted kNN), com K = 7, da biblioteca SKLearn, documentado [neste link](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html), com o parâmetro weights = 'distance';
* GFRNN, da biblioteca NeuPy, documentado [neste link](http://neupy.com/apidocs/neupy.algorithms.rbfn.grnn.html);
* DTree, com profundidade máxima = 7, da biblioteca SKLearn, documentado [neste link](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html);
* Gaussian Naive Bayes, da biblioteca SKLearn, documentado [neste link](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html);
* SVM, da biblioteca SKLearn, com kernel = RBF e C = 8.5, documentado [neste link](https://scikit-learn.org/stable/modules/svm.html);
* MLP, com função de ativação = relu, 3 hidden layers de 12 perceptrons cada e no máximo 500 interações, da biblioteca SKLearn, documentado [neste link](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html);

O artigo ainda compara com outros algoritmos, que não possuem implementação em bibliotecas externas:
* WAF (Weighted Attraction Force), utilizando CC como função de massa.
    * Aguilera, J., González, L.C., Montes-y Gómez, M., Rosso, P., 2018. A new weighted k-nearest neighbor algorithm based on newton’s gravitational force, in: Progress in Pattern Recognition, Image Analysis, Computer Vision, and Applications, Springer International Publishing. pp. 305–313.
* WAF (Weighted Attraction Force), utilizando CD como função de massa.
    * Aguilera, J., González, L.C., Montes-y Gómez, M., Rosso, P., 2018. A new weighted k-nearest neighbor algorithm based on newton’s gravitational force, in: Progress in Pattern Recognition, Image Analysis, Computer Vision, and Applications, Springer International Publishing. pp. 305–313.
* Im-GFRNN (Improved Gravitational Fixed Radius Nearest Neighbor).
    * Shabani-kordshooli, M., Nikpour, B., Nezamabadi-pour, H., 2017. An improvement to gravitational fixed radius nearest neighbor for imbalanced problem, in: 2017 Artificial Intelligence and Signal Processing Conference (AISP), pp. 262--267. doi:10.1109/AISP.2017.8324109.