from flask import Flask, render_template,request,send_file
from hashtag_search import getHashtagMedia, getHastagInfo
from defines import getCreds
import pandas as pd


app = Flask(__name__)
out_dir ="static"


def set_data_todf(columns,post):
    raw = dict()
    for item in columns:
        try:
            raw[item] = (post[item])
        except:
            raw[item] = ("no info") 
    raw = pd.Series(raw)   
    return raw     
        


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrap', methods=['POST'])
def scrap():
    
    if request.method == 'POST':
        hashtag = request.form['search_keyword']
        file_name = hashtag+'.csv'
        full_name = out_dir + '/' + file_name

        if request.method == 'POST':
            out_list = (request.form.getlist('info'))
            
        columns=['id']+out_list+['permalink']
        
        df_pic = pd.DataFrame(columns=columns)
        df_pic.to_csv(full_name,sep=',',index=None)

        params = getCreds() 
        params['hashtag_name'] = hashtag 
        hashtagInfoResponse = getHastagInfo( params )
        try:
            assert hashtagInfoResponse['json_data']['data']
            hashtag =  hashtagInfoResponse['json_data']['data'][0]['id']
            
            params['hashtag_id'] = hashtag
            params['type'] = 'top_media'
            
            hashtagTopMediaResponse = getHashtagMedia( params )
            for post in hashtagTopMediaResponse['json_data']['data']:
                raw_output = set_data_todf(columns,post)
                df_pic = df_pic.append(raw_output, ignore_index=True)
            df_pic.to_csv(full_name,sep=',',index=None,header=None,mode='a')
 


            assert hashtagInfoResponse['json_data']['data']
            hashtag =  hashtagInfoResponse['json_data']['data'][0]['id']
            
            params['hashtag_id'] = hashtag
            params['type'] = 'recent_media'
            
            hashtagTopMediaResponse = getHashtagMedia( params )
            for post in hashtagTopMediaResponse['json_data']['data']:
                raw_output = set_data_todf(columns,post)
                df_pic = df_pic.append(raw_output, ignore_index=True)
            df_pic.to_csv(full_name,sep=',',index=None,header=None,mode='a')

            return send_file("static"+"/"+file_name, attachment_filename=file_name)   
        
        except:
            return hashtagInfoResponse['json_data']['error']['message']  

        
      

     
            
        
               



        