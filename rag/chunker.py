from langchain_text_splitters import RecursiveCharacterTextSplitter

class DocumentChunker:

    def __init__(self):

        self.text_splitter= (
            RecursiveCharacterTextSplitter(
                chunk_size=800,
                chunk_overlap=150,
                separators=["\n\n","\n" , ". "," ",""]
            )
        )

    def split_document(self,text: str):

        return self.text_splitter.split_text( text)