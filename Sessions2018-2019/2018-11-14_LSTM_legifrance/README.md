# 14 novembre 2018
- Animateur: Erwan Keribin
- Question concrète: A quel point les LSTM donnent de meilleurs résultats en génération de text que des Chaînes de Markov ?
- Méthode machine learning: LSTM
- Dataset formatté et benchmarké: Corpus issu de la législation française

## Présentation
[LSTM versus Markov chain in text generation.pdf](https://github.com/amlb/amlb.github.io/blob/master/2018-11-14_LSTM_legifrance/LSTM%20versus%20Markov%20chain%20in%20text%20generation.pdf)

## Notebooks et fichiers data:
- [Dataset.ipynb](https://github.com/amlb/amlb.github.io/blob/master/2018-11-14_LSTM_legifrance/Dataset.ipynb): notebook pour le téléchargement et formattage du dataset
- [MarkovChain.ipynb](https://github.com/amlb/amlb.github.io/blob/master/2018-11-14_LSTM_legifrance/MarkovChain.ipynb): notebook test des chaînes de markov basé sur les paquets [markovify](https://github.com/jsvine/markovify) et [pykovy](https://github.com/justanr/pykovy)
- [LSTM1.ipynb](https://github.com/amlb/amlb.github.io/blob/master/2018-11-14_LSTM_legifrance/LSTM1.ipynb): premier essai LSTM, quasi identique à LSTM2.ipynb (il vaut mieux regarder ce dernier)
- [LSTM2.ipynb](https://github.com/amlb/amlb.github.io/blob/master/2018-11-14_LSTM_legifrance/LSTM2.ipynb): second essai LSTM basé sur [https://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras](https://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras)
- [LSTM3.ipynb](https://github.com/amlb/amlb.github.io/blob/master/2018-11-14_LSTM_legifrance/LSTM3.ipynb): troisième essai LSTM basé sur [https://github.com/keras-team/keras/blob/master/examples/lstm_text_generation.py](https://github.com/keras-team/keras/blob/master/examples/lstm_text_generation.py)
- [legfrance.txt](https://github.com/amlb/amlb.github.io/blob/master/2018-11-14_LSTM_legifrance/legfrance.txt): fichier texte contenant les données formattés (il est possible que ce soit un traitement partiel mais de toute façon seul une partie est utilisé dans les notebooks)
