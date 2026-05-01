import pandas as pd
from datasets import Dataset

class UnlearnHarmDataset:
    def __init__(self, data_path, tokenizer, input_column="text", max_length=2048, **kwargs):
        self.data_path = data_path
        self.tokenizer = tokenizer
        self.input_column = input_column
        self.max_length = max_length
        self.dataset = self._load_and_tokenize()

    def _load_and_tokenize(self):
        df = pd.read_csv(self.data_path)
        assert self.input_column in df.columns, f"Column '{self.input_column}' not found in {self.data_path}"
        hf_ds = Dataset.from_pandas(df)

        def preprocess(examples):
            tokens = self.tokenizer(
                examples[self.input_column],
                truncation=True,
                padding="max_length",
                max_length=self.max_length,
            )
            tokens["labels"] = tokens["input_ids"].copy()
            return tokens

        return hf_ds.map(preprocess, batched=True, remove_columns=[self.input_column])

    def __getitem__(self, idx):
        return self.dataset[idx]

    def __len__(self):
        return len(self.dataset)