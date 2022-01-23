import json
import requests
from bs4 import BeautifulSoup



def get_first_news():   ##########################ФУНКЦИЯ НАЗВАНИЕ##############################
	headers = {
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
	}

	url = 'https://telemetr.me/content/avitov/1'
	r = requests.get(url=url, headers=headers)

	soup = BeautifulSoup(r.text, "lxml")
	medias_pic = soup.find_all("img", class_="media_pic")




	##################################КОД ПАРСИНГ######################################################


	
	news_dict = {}
	
	for media in medias_pic:
		

		media_url = f'{media.get("src")}'

		print(f"{media_url}")









		media_id = media_url.split("/")[-1]
		media_id = media_id[:-4]




		###################################################ВСЯ ИНФА ТОК УРЛ##############################################################

		print(f"{media_url}")

		news_dict[media_id] = {
			"media_url": media_url
		}


	with open("news_dict.json", "w") as file:
		json.dump(news_dict, file, indent=4, ensure_ascii=False)





def main():
	get_first_news()





if __name__ == '__main__':
	main()



