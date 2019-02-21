

import json

def parseChannel(file_name):
  with open(file_name, encoding='utf8') as f:
    channel_json = f.read()
  return json.loads(channel_json)

def saveChannelInfo(file_name, json_data):
  with open(file_name, 'w', encoding='utf8') as f:
    json.dump(json_data, f, ensure_ascii=False, separators=(',', ':'))

def convertChannelOfSK(channel):
  sk_channel = []
  for single_chan in channel:
    new_info = {
      'tvg-id': single_chan['Id'],
      'tvg_logo': single_chan['Icon_url'],
      'tvh-chnum': single_chan['SKCh'],
      'tvh-tags': single_chan['SK Name'],
      'tvh-name': single_chan['Name']
    }
    sk_channel.append(new_info)

  return sk_channel

def main():
  channel = parseChannel('json/Channel.json')
  print(channel)
  sk_channel = convertChannelOfSK(channel)
  print(sk_channel)
  saveChannelInfo('json/channel_info_test.json', sk_channel)

if __name__ == "__main__":
  main()