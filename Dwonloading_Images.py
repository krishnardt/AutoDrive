from bs4 import BeautifulSoup as bs
import urllib3
import urllib

http = urllib3.PoolManager()
link = "https://github.com/ndrplz/self-driving-car/tree/master/project_4_advanced_lane_finding/camera_cal";
link = http.request('GET', link);
data = bs(link.data)
'''
images = [img for img in data.findAll("img")]
print("count of images are:   "+str(len(images)))

img_links = [i.get("a") for i in images]

print(img_links)
'''

table = data.find('table', {'class':'files js-navigation-container js-active-navigation-container'})
rows = table.findAll('tr')
links = []
for row in rows:
	data = row.find("td",{"class":"content"}).get("a")
	#td = row.find("td",{"class":"content"}).get("href")
	#print(data[1].find("a"))
	links.append(str(data))#.get('href')
	#links = links.split(" ")[2]#.split("=")[1]
	#print(links["href"])
	print("\n\n\n")

print(links[1])#.split(" ")[2].split("=")[1])


