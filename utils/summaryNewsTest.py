from langdetect import detect, LangDetectException  # 언어 감지 및 예외 처리
import torch
from transformers import pipeline  # 영어 기사 요약
from transformers import BartForConditionalGeneration, PreTrainedTokenizerFast  # 한국어 기사 요약


def summary_news(text):
    try:
        lang = detect(text)      # 입력된 언어 감지
    except LangDetectException:  # 언어 감지 실패 (너무 짧은 입력 or 지원언어 아님)
        lang = None

    if lang == 'en':             # 감지된 언어 영어
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        summary_eng = summarizer(text, max_length=256, min_length=64, do_sample=False)
        summary = summary_eng[0]['summary_text']
    elif lang == 'ko':           # 감지된 언어 한국어
        sum_tokenizer = PreTrainedTokenizerFast.from_pretrained('gogamza/kobart-summarization')
        sum_model = BartForConditionalGeneration.from_pretrained('gogamza/kobart-summarization')

        raw_input_ids = sum_tokenizer.encode(text)
        input_ids = [sum_tokenizer.bos_token_id] + raw_input_ids + [sum_tokenizer.eos_token_id]

        summary_ids = sum_model.generate(torch.tensor([input_ids]), max_length=256, min_length=64, num_beams=5)
        summary = sum_tokenizer.decode(summary_ids.squeeze().tolist(), skip_special_tokens=True)
    elif not lang:               # 언어 감지에 실패한 경우
        summary = "error1"
    else:                        # 감지된 언어가 영어나 한국어가 아닐 경우 (ex. 일본어, 중국어 등)
        summary = "error2"

    return summary
