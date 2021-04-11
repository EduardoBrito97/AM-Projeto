# Projeto Aprendizagem de Máquina CIn-UFPE 2020.1
Replicação do artigo 'From neighbors to strengths - the k-strongest strengths (kSS) classification algorithm', disponível em https://doi.org/10.1016/j.patrec.2020.06.020, para o projeto da cadeira de Aprendizagem de Máquina, com o professor George Darmiton da Cunha Cavalcanti.

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