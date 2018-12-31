#Stop words are words like 'a' and 'the'. They appear so frequently that they don't require tagging.
#Spacy holds a built in list of some 305 English stop words.

import spacy
nlp =spacy.load('en_core_web_sm')

print(nlp.Defaults.stop_words)

#Results
#{'only', 'another', 'although', 'give', 'have', 'seemed', 'using', 'whenever', 'became', 'moreover',
# 'among', 'please', 'sometimes', 'around', 'two', 'against', 'has', 'eight', 'however', 'him', 'mostly',
# 'seem', 'take', 'by', 'below', 'ourselves', 'hereupon', 'almost', 'was', 'whom', 'in', 'he', 'every',
#  'four', 'more', 'nine', 're', 'done', 'until', 'being', 'since','beside', 'there', 'because', 'very', 
# 'did', 'toward', 'whereas', 'most', 'other', 'before', 'about', 'everything', 'must','or', 'then', 
# 'while', 'us', 'into', 'also', 'no', 'part', 'something', 'where', 'once', 'as', 'yours', 'namely', 
# 'does', 'herself', 'rather', 'otherwise', 'from', 'regarding', 'across', 'their', 'either', 'via', 
# 'been', 'get', 'make', 'why', 'latterly', 'again', 'an', 'anyhow', 'sometime', 'five', 'thru', 
# 'behind', 'our', 'hence', 'when', 'that', 'cannot', 'her', 'under', 'already', 'with', 'beyond', 
# 'whose', 'none', 'latter', 'the', 'those', 'not', 'serious', 'but', 'ten', 'bottom', 'over', 'say', 
# 'own', 'for', 'of', 'yourselves', 'themselves', 'herein', 'whereby', 'fifteen', 'within', 'so', 
# 'during', 'one', 'and', 'them', 'which', 'anything', 'last', 'ever', 'anywhere', 'first', 'whence', 
# 'becoming', 'both', 'nothing', 'per', 'still', 'full', 'ca', 'thereby', 'is', 'these', 'this', 'few',
#  'due', 'just', 'move', 'through', 'everyone', 'former', 'formerly', 'can', 'thence', 'nevertheless',
#  'together', 'throughout', 'after', 'put', 'up', 'whereupon', 'become', 'your', 'whither', 'were', 
# 'than', 'really', 'we', 'enough', 'some', 'now', 'it', 'who', 'afterwards', 'besides', 'his', 
# 'wherein', 'i', 'several', 'hereby', 'somewhere', 'had', 'call', 'sixty', 'well', 'becomes', 'be', 
# 'therein', 'anyway', 'whatever', 'nor', 'hers', 'wherever', 'mine', 'to', 'whoever', 'further', 'its', 
# 'off', 'show', 'a', 'beforehand', 'meanwhile', 'on', 'thereupon','except', 'side', 'towards', 'fifty', 
# 'at', 'twenty', 'else', 'me', 'perhaps', 'seeming', 'such', 'too', 'quite', 'third', 'back', 'forty',
#  'onto', 'various', 'how', 'if', 'thus', 'someone', 'along', 'many', 'all', 'though', 'yet', 
# 'therefore', 'even', 'alone', 'here', 'next', 'could', 'whether', 'never', 'indeed', 'thereafter', 
# 'others', 'twelve', 'keep', 'eleven', 'myself', 'much', 'will', 'himself', 'what', 'least', 'any', 
# 'might', 'amongst', 'whereafter', 'whole', 'between', 'same', 'down', 'used', 'am', 'may', 
# 'hereafter', 'seems', 'upon', 'would', 'elsewhere', 'empty', 'everywhere', 'out', 'amount', 'top',
# 'anyone', 'six', 'somehow', 'yourself', 'you', 'hundred', 'nowhere', 'name', 'see', 'itself', 
# 'neither', 'are', 'my', 'go','front', 'she', 'above', 'often', 'each', 'unless', 'made', 'less', 
# 'nobody', 'ours', 'do', 'noone', 'without', 'doing', 'three', 'always', 'should', 'they'}