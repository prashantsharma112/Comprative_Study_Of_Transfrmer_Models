


import sacrebleu
# from codebleu import calc_codebleu

def bleu_score(reference: str, hypothesis: str) -> float:
    bleu = sacrebleu.corpus_bleu([hypothesis], [[reference]])
    return bleu.score
