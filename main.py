import ctypes, datetime, random
from utils import API_KEY, colors, download, random_date

def main():
  
  print(f"NASA Astronomy Picture of the Day downloader - made by {colors.BRIGHT_MAGENTA}P{colors.BRIGHT_PURPLE}io{colors.BRIGHT_BLUE}mb{colors.BRIGHT_GREEN}ac{colors.BRIGHT_YELLOW}ci{colors.BRIGHT_ORANGE}ai{colors.BRIGHT_RED}o{colors.RESET}")
  if API_KEY == "https://api.nasa.gov/":
    print(f"{colors.BRIGHT_RED}Get your own api key at https://api.nasa.gov/ before using and set it up in utils.py{colors.RESET}")

  while True:

    print(f"[{colors.BRIGHT_CYAN}1{colors.RESET}] - Download today's image\n[{colors.BRIGHT_CYAN}2{colors.RESET}] - Download image from date\n[{colors.BRIGHT_CYAN}3{colors.RESET}] - Download random image\n[{colors.BRIGHT_CYAN}Q{colors.RESET}] - Quit")
    user = input(">> ").upper()

    while user not in ["1", "2", "3", "Q"]:
      print(f"[{colors.BRIGHT_RED}X{colors.RESET}] - Invalid choice. Retry")
      user = input(">> ").upper()
    
    if user == "Q":
      quit(0)
    
    if user == "1":
      try: download(datetime.datetime.today().strftime('%Y-%m-%d'))
      except Exception as e: print(f"[{colors.BRIGHT_RED}X{colors.RESET}] - Error! {e}\n")

    if user == "2":
      print(f"First available image is from: {colors.BRIGHT_CYAN}18th June 1999{colors.RESET}")
      year = input("Provide the year of the photo (YYYY) >> ")
      while not year.isdigit() or len(year) != 4:
        print(f"[{colors.BRIGHT_RED}X{colors.RESET}] - Year format not valid. Retry")
        year = input(">> ")

      month = input("Provide the month of the photo (MM) >> ")
      while not month.isdigit() or len(month) != 2:
        print(f"[{colors.BRIGHT_RED}X{colors.RESET}] - Month format not valid. Retry")
        month = input(">> ")
      
      day = input("Provide the day of the photo (DD) >> ")
      while not day.isdigit() or len(day) != 2:
        print(f"[{colors.BRIGHT_RED}X{colors.RESET}] - Day format not valid. Retry")
        day = input(">> ")

      try: download(f"{year}-{month}-{day}")
      except Exception as e: print(f"[{colors.BRIGHT_RED}X{colors.RESET}] - Error! {e}\n")

    if user == "3":
      print("Dowloading random picture")
      date = random_date(datetime.datetime.today().strftime('%d-%m-%Y'), random.random())
      day,month,year = date.split("-")
      print(f"Day: {colors.BRIGHT_CYAN}{date}{colors.RESET}")

      try: download(f"{year}-{month}-{day}")
      except Exception as e: print(f"[{colors.BRIGHT_RED}X{colors.RESET}] - Error! {e}\n")

if __name__ == '__main__': 
  ctypes.windll.kernel32.SetConsoleTitleW(f'NASA APOD Downloader')
  main()