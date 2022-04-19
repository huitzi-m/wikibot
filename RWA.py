import requests
import wikipedia
from bs4 import BeautifulSoup


# get the randome article
def genPage():
	url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
	soup = BeautifulSoup(url.content, "html.parser")
	global title
	title = soup.find(class_="firstHeading").text
	showInfo()

	return
	
def showInfo():
	try:
		print("your article is about : " + title)
		choice = input("Do you wanna see the full article ? [yes/no] :")

		if choice == "yes":
		
			topic = wikipedia.page(title)
			print("")
			print("Here is a summary : " + wikipedia.summary(str(title)))
			print("")
			print("Article link : " + topic.url)

		elif choice == "no":		
			genPage()

		return	
	
	except UnicodeEncodeError:
		print("Article link : " + topic.url)
	

if __name__ == '__main__':
	genPage()
		
	