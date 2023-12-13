import openai
import os
import re
from dotenv import load_dotenv, find_dotenv
import json
import ast
import time

_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_TOKEN')

def get_completion(prompt, temp,model="gpt-3.5-turbo"): 
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temp, # this is the degree of randomness of the model's output
        max_tokens=2000
    )
    return response.choices[0].message["content"]

def Creadortexto(title,duration):
    if duration>1:
        minwords=int(float(duration)*150)
        maxwords=minwords+int(0.2*minwords)
    else:
        minwords=110
        maxwords=130
    maxwords=minwords+int(0.2*minwords)
    menor=True
    mayor=True


    prompt1 = f"""
    Your task is to generate a text of {minwords} words, aimed at a general audience on the topic of the title (it is important that\
             the text supports the title and does not contradict it, and you should not give your opinion about the title, in fact do not make reference\
                 straight to the title).

     Generate the text using the title below, which is between triple accents, in at most {maxwords} words.

     Title: ```{title}```

     Your response must be only the created text.
    """
    response = get_completion(prompt1,0)
    i=0
    palabras=len(re.findall(r'\w+', response))
    if palabras>=minwords:
            menor=False
    if palabras<maxwords:
        mayor=False
    while menor or mayor:
        time.sleep(15)
        while menor:
            
            prompt2 = f"""
            Your task is to rewrite and extend the following text so that it contains more words but does not exceed {maxwords} words:

             Rewrites the text, delimited by triple accents, and adds content to extend it, \
                 making sure it does not contain more than {maxwords} words. (do not refer directly to the number of words)

             Text: ```{response}```

             You can add additional details, examples, or explanations to make the text more complete and meaningful.
            """
            response = get_completion(prompt2,0)
            palabras=len(re.findall(r'\w+', response))
            i=i+1
            if palabras>=minwords or i>7:
                menor=False
            else:
                menor=True
            if palabras<maxwords or i>7:
                mayor=False
            else:
                mayor=True
            

        while mayor:
            
            prompt2 = f"""
            Your task is to rewrite the following text in a range of {minwords}-{maxwords} words:

             Rewrite the text, delimited by triple accents, more concisely while ensuring that it contains \
                 at least {minwords} words and do not exceed {maxwords} words. (do not make direct reference to the number of words)

             Text: ```{response}```
            """
            response = get_completion(prompt2,0)
            palabras=len(re.findall(r'\w+', response))
            i=i+1
            if palabras>=minwords or i>7:
                menor=False
            else:
                menor=True
            if palabras<maxwords or i>7:
                mayor=False
            else:
                mayor=True
            
            

    return response

    

def jasonmomoa(guion):
    division=[]
    tematicas=[]
    prompt=f"""
        Your task is to write a short 50 character description in spanish of the text below, which is delimited by triple backticks.

        Text: ```{guion}```
        """
    descripcion=get_completion(prompt,0.7)
    prompt2=f"""
        Your task is to write a string of 5 tags in spanish, separated from each other by commas, which represent the content of the text below, which is delimited by triple backticks.
        Text: ```{descripcion}```
        """
    tags=get_completion(prompt2,0.7)
    prompt3=f"""
        Your task is to divide the text below, which is delimited by triple backticks, into short 20 word (no longer than 25 words) parts (it must be done so in a way in which if one unites all of the parts, it generates the original text) and put them in a Python list.
        Text: ```{guion}```
        """
    pdivision=get_completion(prompt3,0)
    division=ast.literal_eval(pdivision)
    
    for i,text in enumerate(division):
        prompt4=f"""
            Your task is to examine the theme of the text below, which is delimited by triple backticks(for exemple: happy, erotic, conflict).
            Examine the theme/sentiment of the text and resume it in 2 or 3 words. 
            Your answer must only be the return of the resultant theme/sentiment(always in english).

            Text: ```{text}```
            """
        tematicas.append(get_completion(prompt4,1))
        i+=1
        time.sleep(5)
    
    return [descripcion,tags,division,tematicas]

def sinonimo(text):
    prompt=f"""
            Your task is to change this word/words, which is/are between triple backticks, for a synonym. 
            Your response must only be the resultant synonym without any backtick.(always in english)

            Word/words: ```{text}```
            """
    
    return get_completion(prompt,1.5)
    
