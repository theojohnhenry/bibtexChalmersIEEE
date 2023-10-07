from pybtex.database.input import bibtex


parser = bibtex.Parser()
bibData = parser.parse_file("data.bib")
print(bibData.entries._keys())