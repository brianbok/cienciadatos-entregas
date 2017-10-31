import pandas as pd

def roc_and_roll(dataset, nombre_columna):
	feature = dataset[nombre_columna]
	etiqueta = dataset["tipo"]

	feature_etiquetado = zip(feature,etiqueta)

	feature_etiquetado = sorted(feature_etiquetado)

	sorted_feature = sorted(feature)

	cols = ["tpr", "fpr"]
	df_res = pd.DataFrame(columns=cols)
	for x in sorted_feature :
		filtrados = filter(lambda x0: x0[0] <= x,feature_etiquetado)
		false_positives = filter(lambda x0: x0[1] == "disminuido", filtrados)
		false_positives = float(len(false_positives))

		true_positives = float((len(filtrados) - false_positives))
		false_negatives = 10 - true_positives
		true_negatives = 10 - false_positives

		true_positive_ratio =  true_positives / (true_positives + false_negatives)
		false_positive_ratio = false_positives / (false_positives + true_negatives)
		
		var = pd.DataFrame(data=[[false_positive_ratio, true_positive_ratio]], columns=cols)
		df_res = df_res.append(var)

	return df_res