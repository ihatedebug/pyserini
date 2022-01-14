# Copyright 2020 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
from pathlib import Path
import csv
import json
import os


def main(src_file: Path, dest_file: Path):
    file = open(src_file, 'r')
    a = file.readline()

    # The first line consist of headings of the record
    # so we will store it in an array and move to
    # next line in input_file.
    titles = ["id", "text", "title"]
    with open(dest_file, 'w', encoding='utf-8', ) as output_file:
        for line in file:
            d = {}
            for t, f in zip(titles, line.split('\t')):

                # Convert each row into dictionary with keys as titles
                d[t] = f.strip()

                # we will use strip to remove '\n'.
            store_d = dict(id="doc"+d["id"], contents=d["title"]+"\n"+d["text"])
            output_file.write(json.dumps(store_d, ensure_ascii=False)+"\n")
            # we will append all the individual dictionaires into list
            # and dump into file.
    file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # Required parameters
    parser.add_argument(
        "--src",
        type=str,
        default="/data1/jongho/nq/downloads/data/wikipedia_split/psgs_w100.tsv",
        help="Path to input tsv wiki (from facebookresearch/dpr)",
    )
    parser.add_argument("--dest", type=str, default="/data1/jongho/serini/wiki",
                        help="Path to the output json wiki.")
    args = parser.parse_args()

    src_file = Path(args.src)
    #dest_file = f"converted-{src_file.name}" if args.dest is None else args.dest
    dest_file = os.path.splitext(os.path.basename(src_file))[0]
    dest_file = os.path.join(Path(args.dest), dest_file+".jsonl")
    assert src_file.exists()
    main(src_file, dest_file)
