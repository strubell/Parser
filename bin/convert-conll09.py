
conll09_fname = "/home/strubell/research/data/CoNLL2009-ST-English/CoNLL2009-ST-English-train.txt"

with open(conll09_fname, 'r') as f:
  for line in f:
    line = line.strip()
    if line:
      # ID FORM LEMMA PLEMMA POS PPOS FEAT PFEAT HEAD PHEAD DEPREL PDEPREL
      split_line = line.split()
      id = split_line[0]
      word = split_line[1]
      gold_pos = split_line[4]
      pred_pos = split_line[5]
      gold_head = split_line[8]
      # pred_head = split_line[9]
      gold_dep = split_line[10]
      # pred_dep = split_line[11]
      predicate_tf = split_line[12]
      predicate = split_line[13]
      predicate_word, predicate_sense = predicate.split('.') if predicate_tf == 'Y' else '-', '-'
      srls = split_line[14:]

      print("_\t_\t%s\t%s\t%s\t%s\t%s\t%s\t_\t%s\t%s\t_\t_\t%s" %
            (id, word, gold_pos, pred_pos, gold_head, gold_dep, predicate_word, predicate_sense, '\t'.join(srls)))