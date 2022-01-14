from pyserini.dsearch import SimpleDenseSearcher

searcher = SimpleDenseSearcher(
    'indexes/dindex-sample-dpr-multi-full', '/data1/jongho/serini/models/dpr_nq_question'
)
hits = searcher.search('what is a lobster roll')

for i in range(0, 10):
    print(f'{i+1:2} {hits[i].docid:7} {hits[i].score:.5f}')