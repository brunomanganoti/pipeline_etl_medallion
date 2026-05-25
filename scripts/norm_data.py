# Script para normalização dos dados de diferentes tipos de arquivo
import os
import pandas as pd

class NormalizeData:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def converte_coluna_string(self, df):
        for column in df.columns:
            if df[column].dtype == 'object':
                df[column] = df[column].apply(lambda x: str(x) if isinstance(x, list) else x)
        return df

    def normalize_data(self):
        for file in os.listdir(self.input_dir):
            input_path = os.path.join(self.input_dir, file)
            filename, extension = os.path.splitext(file)
            output_path = os.path.join(self.output_dir, f"{filename}.parquet")
        
            if extension == '.csv':
                df = pd.read_csv(input_path)
            elif extension == '.json':
                try:
                    df = pd.read_json(input_path)
                except ValueError:
                    df = pd.read_json(input_path, lines=True)
            else:
                print(f"Arquivo {filename} ignorado, formato não suportado: ({extension})")
                continue

            df = self.converte_coluna_string(df)
            df = df.drop_duplicates().reset_index(drop=True)

            df.to_parquet(output_path, index=False)
            print(f"Arquivo {filename} normalizado e salvo em {output_path}")

if __name__ == "__main__":
    normalize_data = NormalizeData(input_dir="01-bronze", output_dir="02-silver")
    normalize_data.normalize_data()