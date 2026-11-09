"""Build the curated public catalogue from verified team repository records."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
items = []

def paper(repo, title, year, venue, category, description, anthology=None, status='Published', note=''):
    items.append(dict(id=repo, title=title, year=year, venue=venue, category=category,
        description=description, paper=f'https://aclanthology.org/{anthology}/' if anthology else '',
        github=f'https://github.com/synlp/{repo}', status=status, note=note,
        source=f'https://github.com/synlp/{repo}'))

paper('SANER', 'Named Entity Recognition for Social Media Texts with Semantic Augmentation', 2020, 'EMNLP', 'extraction', 'Recognizes entities in informal social media text by enriching word representations with semantic information from similar words.', '2020.emnlp-main.107')
paper('AESINER', 'Improving Named Entity Recognition with Attentive Ensemble of Syntactic Information', 2020, 'Findings of EMNLP', 'extraction', 'Combines complementary syntactic analyses to improve named entity recognition.', '2020.findings-emnlp.378')
paper('RE-AGCN', 'Dependency-driven Relation Extraction with Attentive Graph Convolutional Networks', 2021, 'ACL', 'extraction', 'Uses word dependencies and attentive graph convolution to identify semantic relations between entities.', '2021.acl-long.344')
paper('RE-TaMM', 'Relation Extraction with Type-aware Map Memories of Word Dependencies', 2021, 'Findings of ACL', 'extraction', 'Models typed word dependencies with map memories for relation extraction.', '2021.findings-acl.221')
paper('RE-NGCN', 'Relation Extraction with Word Graphs from N-grams', 2021, 'EMNLP', 'extraction', 'Builds word graphs from n-grams to capture informative local structures for relation extraction.', '2021.emnlp-main.228', note='The linked repository currently announces a forthcoming code release.')
paper('RE-DMP', 'Improving Relation Extraction through Syntax-induced Pre-training with Dependency Masking', 2022, 'Findings of ACL', 'extraction', 'Encourages syntax-aware representations through dependency masking during pre-training.', '2022.findings-acl.147')
paper('RE-AMT', 'Enhancing Relation Extraction via Adversarial Multi-task Learning', 2022, 'LREC', 'extraction', 'Uses adversarial multi-task learning to improve relation extraction.', '2022.lrec-1.666')
paper('RE-CCG', 'Combinatory Grammar Tells Underlying Relevance among Entities', 2022, 'Findings of EMNLP', 'extraction', 'Studies how combinatory categorial grammar can reveal underlying connections between entities.', '2022.findings-emnlp.424', note='The linked repository currently announces a forthcoming code release.')
paper('DGSA', 'Joint Aspect Extraction and Sentiment Analysis with Directional Graph Convolutional Networks', 2020, 'COLING', 'sentiment', 'Jointly extracts opinion targets and predicts their sentiment with directional graph convolutions.', '2020.coling-main.24')
paper('ASA-WD', 'Enhancing Aspect-level Sentiment Analysis with Word Dependencies', 2021, 'EACL', 'sentiment', 'Uses dependency information to connect each opinion target with the words expressing sentiment about it.', '2021.eacl-main.326')
paper('ASA-TGCN', 'Aspect-based Sentiment Analysis with Type-aware Graph Convolutional Networks and Layer Ensemble', 2021, 'NAACL', 'sentiment', 'Combines typed dependency graphs and representations across model layers for aspect-level sentiment prediction.', '2021.naacl-main.231')
paper('ASA-TM', 'Improving Federated Learning for Aspect-based Sentiment Analysis via Topic Memories', 2021, 'EMNLP', 'sentiment', 'Uses topic memories to support aspect-based sentiment analysis in federated learning.', '2021.emnlp-main.321')
paper('ASA-CLD', 'Complementary Learning of Aspect Terms for Aspect-based Sentiment Analysis', 2022, 'LREC', 'sentiment', 'Learns complementary information about aspect terms for fine-grained sentiment prediction.', '2022.lrec-1.760')
paper('ASA-CCG', 'End-to-end Aspect-based Sentiment Analysis with Combinatory Categorial Grammar', 2023, 'Findings of ACL', 'sentiment', 'Uses combinatory categorial grammar to support joint aspect extraction and sentiment classification.', '2023.findings-acl.859')
paper('ASA-CD', 'Aspect-based Sentiment Analysis with Context Denoising', 2024, 'Findings of NAACL', 'sentiment', 'Uses task-specific diffusion to reduce lexical, bag-of-words and syntactic noise around an opinion target.', '2024.findings-naacl.194', note='The linked repository currently announces a forthcoming code release.')
paper('MABSA-LLMPlug', 'Multimodal Aspect-based Sentiment Analysis with Plugin-enhanced Large Language Models', 2025, 'IEEE TNNLS', 'multimodal', 'Adapts a multimodal language model with visual and textual plugins connected through a memory hub.')
paper('MemRCRHMD', 'Learning Multimodal Contrast with Cross-modal Memory and Reinforced Contrast Recognition', 2024, 'Findings of ACL', 'safety', 'Learns image–text contrast with cross-modal memory and self-rejection sampling for tasks including hateful meme detection.', '2024.findings-acl.391', note='The linked repository currently announces a forthcoming code release.')
paper('SURGE', 'SURGE — Social-media Unified Reaction-Graph Event Dataset', None, 'Dataset & benchmark', 'resources', 'Pairs event-level discussion intensity and sentiment time series with temporally aligned text and reply / repost interaction structure.', status='Open project')
items[-1]['website']='https://synlp.github.io/SURGE/'
paper('PRISM', 'Learning Shared Sentiment Prototypes for Adaptive Multimodal Sentiment Analysis', None, 'Multimodal sentiment', 'multimodal', 'Studies shared sentiment prototypes for adaptive analysis of language, visual and acoustic signals.', status='Open project')
paper('RD-AC', 'Representation Decomposition for Learning Similarity and Contrastness Across Modalities for Affective Computing', None, 'Affective computing', 'multimodal', 'Decomposes multimodal representations to learn shared and contrasting information for affective computing.', status='Open project')
paper('RDA-ABSA', 'Relation-aware Data Augmentation for Aspect-Based Sentiment Analysis', None, 'Data augmentation', 'sentiment', 'Provides a relation-aware pipeline for generating augmented data and evaluating aspect-based sentiment models.', status='Open project')
paper('LLM-Detoxic', 'Detoxification for LLMs via Projection Alignment', None, 'Language model safety', 'safety', 'Provides teacher training, projection alignment, generation and evaluation tools for language model detoxification.', status='Open project')
paper('TOSA-HMD', 'TOSA-HMD', None, 'Hateful meme detection', 'safety', 'Provides a core method using aligned representations, complementary fusion and soft prompts for hateful meme detection with Qwen2-VL.', status='Open project', note='The release contains the core method. It does not include the full set of paper experiment scripts.')
paper('LLM4SM', 'LLM4SM', None, 'Model orchestration', 'resources', 'Connects a large language model to local task models through configurable task and model descriptions.', status='Open project')
paper('WMSeg', 'Improving Chinese Word Segmentation with Wordhood Memory Networks', 2020, 'ACL', 'foundations', 'Uses wordhood memories to support Chinese word segmentation, a foundation for downstream text analysis.', '2020.acl-main.734')
paper('TwASP', 'Joint Chinese Word Segmentation and Part-of-speech Tagging via Two-way Attentions of Auto-analyzed Knowledge', 2020, 'ACL', 'foundations', 'Jointly models segmentation and part-of-speech tags with automatically analyzed linguistic knowledge.', '2020.acl-main.735')
paper('McASP', 'Joint Chinese Word Segmentation and Part-of-speech Tagging via Multi-channel Attention of Character N-grams', 2020, 'COLING', 'foundations', 'Uses character n-gram attention for joint segmentation and part-of-speech tagging.', '2020.coling-main.187')
paper('GCASeg', 'Federated Chinese Word Segmentation with Global Character Associations', 2021, 'Findings of ACL', 'foundations', 'Learns global character associations for Chinese word segmentation across federated data sources.', '2021.findings-acl.376')
paper('SRL-MM', 'Syntax-driven Approach for Semantic Role Labeling', 2022, 'LREC', 'extraction', 'Uses syntactic information to identify predicate–argument roles in text.', '2022.lrec-1.772')

old_path=ROOT/'data'/'publications.json'
old={x['id']:x for x in json.loads(old_path.read_text())} if old_path.exists() else {}
for x in items:
    for key in ('authors','bibtex'):
        if old.get(x['id'],{}).get(key): x[key]=old[x['id']][key]
items.sort(key=lambda x: (x['year'] or 9999, x['id']), reverse=True)
(ROOT/'data').mkdir(exist_ok=True)
(ROOT/'data'/'publications.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
print(f'Wrote {len(items)} works')
