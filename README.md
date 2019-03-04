# Ateliers Machine Learning Brest (ALLOHa)
Lien Github: [https://github.com/amlb/amlb.github.io](https://github.com/amlb/amlb.github.io)

## Description de l'évènement

L'atelier machine learning se déroule au PNBI un mercredi sur deux (sauf vacances) de 10h30 à 12h. Il s'agit d'une recontre de co-apprentissage impulsée par un animateur. Ce dernier aborde une question concrète avec une méthode de machine learning sur un dataset formatté (et de préférence benchmarké). Les présentations s'articulent surtout autour de Jupyter Notebook et de méthodes de deep learning. Le speaker présente la théorie de la méthode choisie ainsi qu'une implementation concrète sur sa question.

C'est avant tout un moment d'échanges conviviaux et d'apprentissage collaboratif. L'animateur présente ses recherches et tests. Cependant plus qu'une simple transmission de connaissances, ce sont les questions et échanges des participants qui font l'intérêt de cet atelier.

Que vous soyez un simple novice curieux ou un expert de machine learning, tous sont bienvenus à l'atelier. Vous pouvez vous inscrire depuis la page suivante: [http://www.campus-mondial-de-la-mer.fr/Center-for-ocean-innovation-and-sustainability-3043-0-0-0.html#Atelier%20Machine%20Learning](http://www.campus-mondial-de-la-mer.fr/Center-for-ocean-innovation-and-sustainability-3043-0-0-0.html#Atelier%20Machine%20Learning).

Si vous souhaitez participer en tant qu'animateur ou juste obtenir plus d'informations vous pouvez contacter Anouck Hubert (anouck.hubert\[AT\]tech-brest-iroise.fr).

## Sessions

### 12 Mars 2019 (à venir)
- Animateur: Clément Dechesne
- Question concrète: Comparaison entre Support Vector Machine (SVM) et une méthode de Deep Learning. Différents cas d'utilisation
- Méthode machine learning: Un SVM sera comparé à un Multi Layer Perceptron (MLP)
- Dataset formatté et benchmarké: Données synthétiques

### [26 Février 2019](/2019-02-26_ReinforcementLearning)
- Animateur: Yoann Sola
- Question concrète: Comment un algorithme peut-il apprendre un comportement à partir de ses interactions avec un environnement inconnu?
- Méthode machine learning: Deep Q-Learning, un algorithme de Deep Reinforcement Learning
- Dataset formatté et benchmarké: Les environnements d'OpenAI Gym simulant des jeux Atari 2600

### 29 Janvier 2019
- Animateur: Jean-Marie prigent
- Question concrète: Classification d’espèces de poissons dans des conditions variables d’illumination sur petite base de données issue d’images sous-marines. Réaliste ?
- Méthode machine learning: Deep Learning avec CNN, transfer learning et fine-tuning. Comment s’aider de tensorboard pour historiser et régler les paramètres du réseau?
- Dataset formatté et benchmarké: Base de données ‘unbalanced’ d’images sous-marines de poisson (468 classes)

### [15 Janvier 2019](/2019-01-15_MNIST_TransferLearning)
- Animateurs: Myriam Chabah, Jerome Habonneau et Yann Le Gall
- Question concrète: Classification Mine vs Rocher sur images sonar - Deep Learning sur des petites bases de données ?
- Méthode machine learning: Transfer learning à partir de CNN pré-entrainés sur images optiques, Classifieurs Machine Learning (SVM, Random Forest)
- Dataset formatté et benchmarké: Base MNIST réduite

### [12 Décembre 2018](/2018-12-12_RandomForests)
- Animateur: Arnaud Gaillot
- Question concrète: Comment prédire la nature des sédiments marins avec le machine learning?
- Méthode machine learning: Random Forest
- Dataset formatté et benchmarké: Modèle hydrodynamique, bathymétrie et ses dérivées, réflectivité acoustique, prélèvements sédimentaires (Baie de Somme)

### [28 Novembre 2018](/2018-11-28_Outils_deep_learning)
- Animateur: Clément Dechesne
- Question concrète: Comment représenter les données avec des outils deep learning pour mieux appréhender nos problèmes ?
- Méthode machine learning: Autoencoder & Réseau totalement convolutionels
- Dataset formatté et benchmarké: MNIST (chiffres écrits à la main) et Base de donnée d'image pour segmentation sémantique

### [14 Novembre 2018](/2018-11-14_LSTM_legifrance)
- Animateur: Erwan Keribin
- Question concrète: A quel point les LSTM donnent de meilleurs résultats en génération de text que des Chaînes de Markov ?
- Méthode machine learning: LSTM
- Dataset formatté et benchmarké: Corpus issu de la législation française

### [24 Octobre 2018](/2018-10-24_LSTM-CNN_GoogleAudioSet)
- Animateur: Dorian Cazau
- Question concrète: Approche multimodale, consistant à apprendre conjointement des features sur la vidéo et le son, améliore t-elle la reconnaissance automatique de scènes acoustiques issues de vidéos youtube ?
- Méthode machine learning: multimodal deep auto-encoder
- Dataset formatté et benchmarké: Google Audio Set ([https://research.google.com/audioset](https://research.google.com/audioset))

### [10 Octobre 2018](/2018-10-10_CNN_Whales)
- Animateur: Paul Nguyen Hong Duc
- Question concrète: Approche classique image pour traiter le son, consistant à apprendre des features sur des MFCCs (mel frequency cepstrum coefficients), améliore-t-elle la reconnaissance automatique de scènes acoustiques?
- Méthode machine learning: CNN 1 couche
- Dataset formatté et benchmarké: DCLDE 2018 LF (website does not work [sabiod.univ-tln.fr/DCLDE](sabiod.univ-tln.fr/DCLDE))

## Liens et autres informations
- [AtelierML-base.ipynb](https://github.com/amlb/amlb.github.io/blob/master/Extra/AtelierML-base.ipynb): template de Jupyter Notebook envoyant des statistiques de classification à un [benchmark en ligne](https://stok.shinyapps.io/aml_shiny) (demandez à Sean les accès MongoDB).
