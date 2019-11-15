# 24 octobre 2018
- Animateur: Dorian Cazau
- Question concrète: approche multimodale, consistant à apprendre conjointement des features sur la vidéo et le son, améliore t-elle la reconnaissance automatique de scènes acoustiques issues de vidéos youtube ?
- Méthode machine learning: multimodal deep auto-encoder
- Dataset formatté et benchmarké: Google Audio Set ([https://research.google.com/audioset](https://research.google.com/audioset))

## Présentation
[How LSTM works.pdf](https://github.com/amlb/amlb.github.io/blob/master/Sessions2018-2019/2018-10-24_LSTM-CNN_GoogleAudioSet/How%20LSTM%20works.pdf)

## Notebooks et fichiers data:
- [AtelierML-24102018.ipynb](https://github.com/amlb/amlb.github.io/blob/master/Sessions2018-2019/2018-10-24_LSTM-CNN_GoogleAudioSet/AtelierML-24102018.ipynb): notebook de l'atelier
- [associatedLabels.npy](https://github.com/amlb/amlb.github.io/blob/master/Sessions2018-2019/2018-10-24_LSTM-CNN_GoogleAudioSet/associatedLabels.npy): labels associés à chaque matrice de dataMat.npy et de tensors.npy
- [dataMat.npy](https://github.com/amlb/amlb.github.io/blob/master/Sessions2018-2019/2018-10-24_LSTM-CNN_GoogleAudioSet/dataMat.npy): MFCCs (matrice pour chaque fichier)
- [tensors.npy](https://github.com/amlb/amlb.github.io/blob/master/Sessions2018-2019/2018-10-24_LSTM-CNN_GoogleAudioSet/tensors.npy): 4 frames extraites et réunies pour former un tenseur pour chaque vidéo

## Theoretical point & doc sources

### Liens

#### How a LSTM works ?
- [https://www.analyticsvidhya.com/blog/2017/12/fundamentals-of-deep-learning-introduction-to-lstm](https://www.analyticsvidhya.com/blog/2017/12/fundamentals-of-deep-learning-introduction-to-lstm)
- [http://colah.github.io/posts/2015-08-Understanding-LSTMs](http://colah.github.io/posts/2015-08-Understanding-LSTMs)

#### Vanishing gradient problem
- [https://medium.com/@anishsingh20/the-vanishing-gradient-problem-48ae7f501257](https://medium.com/@anishsingh20/the-vanishing-gradient-problem-48ae7f501257)
