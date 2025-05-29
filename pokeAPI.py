from hashlib import md5
from requests import get
from datetime import datetime
import shutil 

class RestMarvel:
    timestamp = datetime.now().strftime('%y-%m-%dH:%M:%S')
    pub_key = 'b671c7d7b1988730a096480c6cd933f0'
    priv_key ='5fe3338ccba73fa322753ba66b00021831623721'

    def hash_params(self):
        hash_md5 =md5()
        hash_md5.update(f'{self.timestamp}{self.priv_key}{self.pub_key}'.encode('utf-8'))
        hashed_params =hash_md5.hexdigest()
        return hashed_params
    
    def get_heroes(self):
        params={'ts':self.timestamp,'apikey':self.pub_key,'hash':self.hash_params()}
        results = get('https://gateway.marvel.com:443/v1/public/characters',params=params)

        data =results.json()
        print(data)
        print(data['status'])
        
    def get_gen1_pokemon_images(self):
        base_url ="https://raw.githubusercontent.com/pokeAPI/sprites/master/sprites/pokemon/"
        return [f"{base_url}{i}.png" for i in range(1, 152)]
    
    def descargar_imagen(self, url, file_name):

        res = get(url, stream = True)
        if 200==res.status_code:
            with open(file_name,'wb')as f:
                shutil.copyfileobj(res.raw, f)
                print('imagen descartada corectamente')
        else:
            print('No seencontro la imagen')

    




restamarvel = RestMarvel()
restamarvel.get_heroes()
urls = restamarvel.get_gen1_pokemon_images()
i=0
for url in urls:
    i = i+1
    restamarvel.descargar_imagen(url, str(i)+'.png')