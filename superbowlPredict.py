import numpy as np 
import pandas as pd 
from sklearn import ensemble, svm, preprocessing, model_selection, metrics, linear_model

def main():

	df = pd.read_excel('superbowl.xlsx')

	teams = dict(enumerate(np.asarray(df['Team Name'])))

	#df = shuffle(df)
	convert_to_num_(df)

	x = np.asarray(df.drop('Playoffs', 1).drop('Team Name',1))
	y = np.asarray(df['Playoffs'])

	x = preprocessing.scale(x)

	x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=.2, shuffle=False)

	#kf = model_selection.KFold(n_splits=10)
	#for train_index, test_index in kf.split(x):
	#	x_train, x_test = x[train_index], x[test_index]
	#	y_train, y_test = y[train_index], y[test_index]


	print()
	print('Model Statistics')

	clf = linear_model.SGDClassifier()
	clf.fit(x_train, y_train)
	print('Accuracy ', clf.score(x_test, y_test))
	
	predictions = clf.predict(x_test)
	print('Precision ', metrics.precision_score(y_test, predictions))
	print('Recall ', metrics.recall_score(y_test, predictions))

	print()
	print('2017 NFL Playoffs \n')

	print('2017 NFL Playoffs \n')
	playoff_teams = [teams[i] for i in range(len(x_train), len(x_train)+len(x_test)) if predictions[i-len(x_train)]==1]

	for i in playoff_teams:
		print('The', i, 'will make the Playoffs')

	print()
	features = list(df.columns)[1:10]
	print('FEATURE IMPORTANCES')
	#for i in list(zip(features, clf.feature_importances_)):
	#	print(i)

#End of Main --

def convert_to_num_(df):
	columns = df.columns.values

	def to_key(input):
		return keys[input]

	for col in columns:
		keys = {}
		datatype = df[col].dtype
		if not (datatype == np.int64 or datatype == np.float64):
			j = 1
			for i in df[col]:
				if not i in keys:
					keys[i] = j
					j+=1
			df[col] = df[col].apply(to_key)

def shuffle(df):
	return df.reindex(np.random.permutation(df.index))

if __name__ == '__main__':
	main()