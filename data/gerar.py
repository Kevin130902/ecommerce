import pandas as pd
import os

data = {
    "tituloProduto": ["furadeira", "bomba"],
    "preco": [400, 1500],
    "descricao": ["Fura bem", "Bomba combustável"],
    "imagemProduto": ["/image", "/image"],
    "categoriaProduto": ["Ferramentas", "Auto"],
    "classProduto": ["Casa", "Carro"],
    "exibirNome": [True, False],
}

df = pd.DataFrame(data)


df.to_csv(os.getcwd().replace("\\", "/") + "/data/ferramentas.csv", index=False)