import os, requests, time

API_KEY = "https://api.nasa.gov/"

class colors:
  RESET =  "\033[0m"
  BRIGHT_RED = "\033[38;2;255;0;0m"
  BRIGHT_ORANGE = "\033[38;2;255;127;0m"
  BRIGHT_YELLOW = "\033[38;2;255;255;0m"
  BRIGHT_GREEN = "\033[38;2;0;255;0m"
  BRIGHT_CYAN = "\033[38;2;0;255;255m"
  BRIGHT_BLUE = "\033[38;2;0;0;255m"
  BRIGHT_PURPLE = "\033[38;2;98;0;255m"
  BRIGHT_MAGENTA = "\033[38;2;148;0;211m"

def download(date:str):
  print(f"[{colors.BRIGHT_GREEN}+{colors.RESET}] - Downloading...")
  
  link = "https://api.nasa.gov/planetary/apod?api_key={api}&date={date}".format(api = API_KEY, date = date)

  r = requests.get(link)
  json_respone = r.json()
  
  title = str(json_respone["title"])
  for item in ["\\", "|", "/", ":", "*", "?", '"', "<", ">"]:
    try: title = title.replace(item, "")
    except: pass
  img_url = json_respone["hdurl"]
  info = json_respone["explanation"]
  
  img = requests.get(img_url, stream=True)
  content_type = img.headers["content-type"]
  if img.status_code == 200 and (
    content_type == "image/jpeg"
    or content_type == "image/gif"
    or content_type == "image/png"
  ):
    ext = img.headers["content-type"][6:]
  if not os.path.exists("Download/"): os.mkdir("Download/")
  path = f"Download/{title} ({date})/"
  
  if not os.path.exists(path): os.mkdir(path)
  img_path = path + f"NASA_APOD {title}.{ext}"
  info_path = path + "Information.txt"
  
  with open(img_path, "wb") as f:
    for chunk in img:
      f.write(chunk)
  
  info = info.replace(".  ", ".\n")
  info = info.replace(". ", ".\n")
  with open(info_path, "w+") as f:
    f.write(info)

  print(f"[{colors.BRIGHT_GREEN}+{colors.RESET}] - Download complete!\n")

def random_date(end, prop):
    tf = '%d-%m-%Y'
    stime = time.mktime(time.strptime("18-6-1999", tf))
    etime = time.mktime(time.strptime(end, tf))

    ptime = stime + prop * (etime - stime)

    return time.strftime(tf, time.localtime(ptime))
