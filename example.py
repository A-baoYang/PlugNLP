import torch

text_list = [
    "台郡董座 鄭明智續任 軟板大廠台郡（6269）（6269）昨（31）日召開股東常會，董事長鄭明智主持，股東會昨天完成改選以及通過配息5元等議案。隨後召開董事會，推舉鄭明智續任董座。鄭明智指出，面對2022年大環境挑戰，台郡優先重視三件事，包含對客戶承諾的服務、對員工健康安全的照護及對營運目標的達成，創新技術及人才是營運發展的首要。近七年來台郡獲利能力穩定，每股獲利皆達8元以上，每年配發5元股息回饋股東。鄭明智強調，因應5G、智慧車及低軌道衛星運用等趨勢，持續再開發Neuro Circuit（神經網路）的FPC3.0次世代技術，不僅可深化低耗能高效率生產模式，更可提供客戶對高頻、多層及薄化的先進設計需求。鄭明智提到，雖然上半年疫情嚴峻、國際局勢動盪，但台郡仍繳出亮眼營運成果，今年前四月營收112.1億元，年增17.8%。台郡去年營收356億元，年增19.1%，稅後純益28.8億元，年減1.7%，每股純益8.19元。",  # noqa E501
]
device_ids = list(range(torch.cuda.device_count()))


def run_ner_cpu():
    from RippleFiNER.ner import NER

    ner = NER(use_ray=False, device_ids=-1)
    results = ner.predict(input_text_list=text_list)
    print(results)


def run_ner_gpu():
    from RippleFiNER.ner import NER

    ner = NER(use_ray=False, device_ids=device_ids)
    results = ner.predict(input_text_list=text_list)
    print(results)


def run_ner_cpu_ray():
    from RippleFiNER.ner import NER

    ner = NER(use_ray=True, device_ids=-1)
    results = ner.predict(input_text_list=text_list)
    print(results)


def run_ner_gpu_ray():
    from RippleFiNER.ner import NER

    ner = NER(use_ray=True, device_ids=device_ids)
    results = ner.predict(input_text_list=text_list)
    print(results)


run_ner_gpu()
