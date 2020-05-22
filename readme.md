Identifying Synthetic Lethal Interations n Genes Using Node2Vec and Random Forest
----
# Abstract

Recent advancements in the machine learning field has helped predictions on features of network become more effective. For example, programs from such as Node2Vec have been able to learn continuous feature representations for nodes in networks and learn how to map nodes to a feature dependant dimensional space. As such, Node2Vec has opened the door to much potential research that was not previously easily delved into. In this paper, we investigate the application of Node2Vec to genetic interactions, specifically trying to predict synthetic lethality among interactions. Distinguishing between synthetic lethal and non-synthetic interactions is helpful to the cancer research field, as synthetic lethal interactions can used as a mechanism to target tumor-specific mutations, helping in the development of anticancer therapeutics. The collection of genetic interactions in a species is a network, and therefore, we can use Node2Vec to assist with the learning about the gene interaction network features, such as the type of interaction (synthetic lethal or non-synthetic lethal) between two genes. By using Node2Vec and different machine learning classification models, we demonstrate the proof on concept that by starting with only the genetic interaction network (without the knowledge of each type of interaction), we can make fairly accurate predictions on weather an interaction is synthetic lethal or non-synthetic lethal. Additionally, we explore the idea of merging species by overlapping different species network and connecting them with homologous interactions, seeing if we can get better, more accurate, predictions on genetic interactions.

### Paper Draft and Presentation
* Paper draft: https://github.com/aravindkoneru/CMSC396H/blob/master/SL%20paper/SL.pdf
* Presentation: https://docs.google.com/presentation/d/1np09Ax7NE1pL-f8gmu7dEV6CXpxrI8MBsLHkw2vUnfc/edit?usp=sharing

## Authors

* Cameron Simmons
* Aravind Koneru
* Hunter Klamut
* Namrita Perincherry
