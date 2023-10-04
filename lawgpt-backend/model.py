from transformers import pipeline

def generate_response(text):

    model=pipeline(task='fill-mask',model='complete_pipeline',tokenizer='complete_pipeline')
    #model=pipeline('fill-mask',model='nlpaueb/legal-bert-base-uncased',tokenizer='nlpaueb/legal-bert-base-uncased')
    words=text.split()

    for i,k in enumerate(words):
        if k[0]=='<' and k[-1]=='>':
            words[i]='[MASK]'

    #encoded string
    encoded_text= ' '.join(map(str, words))

    pred=model(encoded_text)

    words=encoded_text.split()
    token_replace_count=0
    for i,word in enumerate(words):

        if word=='[MASK]':
            words[i]=pred[token_replace_count][0]['token_str'] #replaced on sorting by best probability scores
            token_replace_count+=1
    
    prompt_generated = ' '.join(map(str, words))

    return prompt_generated
 

# print(generate_response("When a district court resolves a purely [MASK] issue against a party at summary [MASK] , that issue is preserved for [MASK] \
# review. There is new requirement that if the case then progresses to a jury trial, the\
# aggrieved party must make two additional motions\
# repeating the same legal argument simply to\
# ensure the issue remains live for review on\
# appeal. That follows from the final judgment\
# rule, the history of appellate review, the\
# history of the [MASK] Rules of Civil Procedure,"))