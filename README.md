## Welcome to My Laboratory :)

There are experimental implementations some useful method and algorithm.

- k-means (k_means.rb)
	- Using [Iris Data Set](http://archive.ics.uci.edu/ml/datasets/Iris)
	- Reference: [Visualizing K-Means Algorithm](http://tech.nitoyon.com/ja/blog/2009/04/09/kmeans-visualise/). (in Japanese)

- BP(Back Propagation) Neural Network
	- Learning 6bit symmetry recognition problem.
	- Implementation in Ruby is too slow. Maybe, I will re-implement in C or C++.
	- Reference:
		- S. Araya, *"Jinkou Chinou Gairon(2nd Edition) [Introduction to Artificial Intelligence]"*, Kyoritsu Shuppan, pp. 121-124, 2004. (in Japanese)
		- S. Asakawa, [Back Propagation(Lecture Handout)](http://www.cis.twcu.ac.jp/~asakawa/waseda2002/bp.pdf). (PDF, in Japanese)

- tf-idf (tf_idf.rb)
	- Calculate tf*idf value for each word of given Japanese documents.
	- Noun will be index word. Other categories are ignored.
	- Reference:
		- T. Tokunaga, *"Jouhou Kensaku To Gengo Shori [Information Retrieval and Natural Language Processing]"*, University of Tokyo Press, pp. 27-28, 1999. (in Japanese)
