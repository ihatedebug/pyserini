export PYTHONPATH=`pwd`

python pyserini/encode/__main__.py input   --corpus /data1/jongho/serini/wiki --shard-id 2 --shard-num 3 --fields title text  output  --embeddings /data1/jongho/serini/indexes/fb_to_ser_dpr_nq-2 --to-faiss  encoder --encoder /data1/jongho/serini/models/dpr_nq_ctx --fields title text --device cuda:2
                                  #--batch 32 

