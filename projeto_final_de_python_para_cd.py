# -*- coding: utf-8 -*-
"""Projeto Final de Python para CD

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ziGLPyiuvmYak_MGYT7iMg3sDFg6i09Q
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

class Modelo():
    def __init__(self):
        self.dataset = None
        self.model = None

    def CarregarDataset(self, path):
        """Carrega o dataset Iris e o armazena no atributo self.dataset."""
        names = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
        self.dataset = pd.read_csv(path, header=None, names=names)
        print("Dataset carregado com sucesso!")

    def TratamentoDeDados(self):
        """Realiza o pré-processamento do dataset."""
        # Verificar e tratar valores faltantes
        if self.dataset.isnull().sum().sum() > 0:
            self.dataset.dropna(inplace=True)
            print("Dados faltantes tratados!")
        print("Tratamento de dados concluído!")

    def Treinamento(self):
        """Treina um modelo Random Forest com o dataset Iris."""
        # Dividir em X (features) e y (target)
        X = self.dataset.drop('Species', axis=1)
        y = self.dataset['Species']

        # Divisão em treino e teste
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        # Treinar o modelo
        self.model = RandomForestClassifier(random_state=42)
        self.model.fit(X_train, y_train)

        # Avaliar o modelo
        y_pred = self.model.predict(X_test)
        print(f"Acurácia no conjunto de teste: {accuracy_score(y_test, y_pred):.2f}")
        print("Relatório de classificação:")
        print(classification_report(y_test, y_pred))

        # Matriz de confusão
        conf_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
        sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
        plt.title("Matriz de Confusão")
        plt.show()

    def Train(self):
        """Fluxo completo de treinamento do modelo."""
        self.CarregarDataset("iris.data")
        self.TratamentoDeDados()
        self.Treinamento()

# Exemplo de uso
modelo = Modelo()
modelo.Train()