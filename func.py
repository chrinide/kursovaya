import math
import numpy as np
def dist(p1, p2):
	return math.sqrt(sum((p1 - p2)**2))
def k_nearest(X, k, obj):
	sub_X = X[:, :-1]
	m = np.mean(sub_X, axis = 0)
	s = np.std(sub_X, axis = 0)
	sub_X = (sub_X - m) / s
	obj = (obj - m) / s
	dists = [dist(obj, i) for i in sub_X]
	argsort = np.argsort(dists)
	nearest_classes = X[argsort[:k], -1]
	unique, counts = np.unique(nearest_classes, return_counts = True)
	object_class = unique[np.argmax(counts)]
	return object_class