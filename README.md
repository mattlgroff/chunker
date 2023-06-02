## Python PDF Chunker

This is a python script that will take PDF file(s) and split them into chunks of 1000 characters.

It will output a JSON array of these 1000 chunk strings (one .json file for each PDF file provided).

### Usage

```bash
docker build -t chunker .

docker run -v $(pwd):/app chunker
```

It will output a file called `your_original_pdf_filename.json` in the current directory. If your PDF filename is `my_pdf.pdf`, then the output file will be `my_pdf.json`.

Make sure the file is in the same folder as this README.md and everything else.