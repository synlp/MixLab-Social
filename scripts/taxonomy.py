AREAS = {
    'sentiment': ('Sentiment analysis', 'Identifying opinion targets and interpreting sentiment in text, images, video and audio. This research includes aspect-level analysis, multimodal learning and data augmentation.', 'sentiment'),
    'extraction': ('Information extraction', 'Organizing unstructured language into entities, relations and semantic roles. The work combines semantic augmentation, linguistic structure, memory mechanisms and pre-training.', 'extraction'),
    'data': ('Data & benchmark construction', 'Building event-centered social media resources that connect discussion and sentiment over time with textual evidence and interaction structure.', 'resources'),
    'safety': ('Content safety', 'Understanding harmful meaning across image and text, and studying methods for reducing toxic language model outputs.', 'safety'),
    'foundations': ('Language foundations & tools', 'Developing Chinese text processing methods and tools that connect language models with local task models.', 'foundations'),
}

def classify(item):
    key=item['id']
    if key=='LLM4SM': return 'foundations','Language model orchestration'
    if key=='SURGE': return 'data','Event-centered datasets'
    if key in ['MABSA-LLMPlug','PRISM','RD-AC']: return 'sentiment','Multimodal sentiment & affect'
    if item['category']=='sentiment': return 'sentiment','Text & aspect-based sentiment'
    if item['category']=='extraction':
        return 'extraction', 'Named entity recognition' if key in ['SANER','AESINER'] else ('Semantic role labeling' if key=='SRL-MM' else 'Relation extraction')
    if item['category']=='safety': return 'safety','Language model detoxification' if key=='LLM-Detoxic' else 'Multimodal content safety'
    return 'foundations','Chinese word segmentation & tagging'
