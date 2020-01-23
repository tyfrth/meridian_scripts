# coding: utf-8
import zipfile, requests, io, re

print('beginning sdk file download...')

# rsdkDownloads = requests.get('https://docs.meridianapps.com/article/481-sdk-downloads')

url1 = 'https://files.meridianapps.com/{}/meridian-ios-sdk-{}.zip'
riOS = requests.get(url1.format('meridian-ios-sdk', '5.10.0'))

url2 = 'https://files.meridianapps.com/{}/meridian-android-sdk-{}.zip'
rAndroid = requests.get(url2.format('meridian-android-sdk', '5.10.0'))
# r1 = re.findall('http.*meridian-ios-sdk*/.zip', rsdkDownloads.text)
# r2 = re.findall('http.*meridian-android-sdk*/.zip', rsdkDownloads.text)

# riOS = requests.get(r1)
# rAndroid = requests.get(r2)

iosSDK = zipfile.ZipFile(io.BytesIO(riOS.content))
androidSDK = zipfile.ZipFile(io.BytesIO(rAndroid.content))

iosSDK.extractall('/Users/tylerfrith/Desktop/SDK/iOS')
androidSDK.extractall('‎⁨‎⁨/Users/tylerfrith/Desktop/SDK/Android')


print('sdk downloads complete!')

