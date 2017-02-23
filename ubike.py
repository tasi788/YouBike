import json, urllib.request, urllib.parse
import time
ubike_url = 'http://ntpc.youbike.com.tw/cht/'
sites_api = {'url': 'index.php', 'container': {'startswith': 'siteContent=\'', 'endswith': '\';siteContent=JSON'}}
areas_api = {'url': 'f12.php?loc=', 'container': {'startswith': 'arealist=\'', 'endswith': '\';arealist=JSON'}}
areas = {'taipei': '台北市', 'ntpc': '新北市', 'taichung': '台中市', 'chcg': '彰化縣', 'tycg': '桃園市', 'hccg': '新竹市'}

#def get_ubike_sites():
#	raw = urllib.request.urlopen(ubike_url + sites_api['url']).read().decode('utf-8')
#	raw = raw.split(sites_api['container']['endswith'], 2)[0].split(sites_api['container']['startswith'], 2)[1]
#	return json.loads(raw)

def get_ubike_sites_with_area_id(area_id):
	raw = urllib.request.urlopen(ubike_url + areas_api['url'] + area_id).read().decode('utf-8')
	raw = raw.split(areas_api['container']['endswith'], 2)[0].split(areas_api['container']['startswith'], 2)[1]
	return urllib.parse.unquote(raw)
print('Running')
# 拿所有資料
#sites = get_ubike_sites()
# 拿台北市的資料
while True:
	try:
		sites_taipei = get_ubike_sites_with_area_id('taipei')
		with open('ubike/ubike.json','w') as f:
			f.write(sites_taipei)
		ubike = json.loads(open('ubike/ubike.json','r').read())
		for x in ubike:
			taipei = open('ubike/ubike_taipei.txt','r').read()
			if ubike[x]['sarea'] not in taipei:
				with open('ubike/ubike_taipei.txt','a') as taipei:
					taipei.write(ubike[x]['sarea']+'\n')
					print('新站點!')
		time.sleep(60)
	except:
		raise
		with open('ubike/ubike.json','w') as f:
			f.write('UBike官網似乎斷線？')
		time.sleep(60)
