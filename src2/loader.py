from pathlib import Path
from langchain_community.document_loaders import (
    PyPDFLoader,
    JSONLoader,
    TextLoader,
    Docx2txtLoader,
    UnstructuredExcelLoader
)

class load_data:
    def __init__(self, data_path: str):
        self.path = data_path

    def load_all_data(self):
        documents = []
        base_path = Path(self.path).resolve()

        loaders = [
            ("**/*.pdf", PyPDFLoader),
            ("**/*.json", JSONLoader),
            ("**/*.txt", TextLoader),
            ("**/*.docx", Docx2txtLoader),
            ("**/*.xlsx", UnstructuredExcelLoader),
        ]

        for pattern, LoaderClass in loaders:
            files = list(base_path.glob(pattern))
            print(f"{pattern} files found: {len(files)} -> {[f.name for f in files]}")

            for file in files:
                loader = LoaderClass(str(file))
                documents.extend(loader.load())

        return documents
