import re

def parse(s):

    pattern = r'src=\"(?P<url>https?://(?:www\.)?youtube\.com/embed/(?P<video_id>[\w-]+))\"'

   
    if match := re.search(pattern, s):
        video_url = "https://youtu.be/" + match.group("video_id")
        return video_url
    else:
        return None

def main():
    html_input = input("HTML: ")
    video_url = parse(html_input)
    if video_url:
        print(video_url)
    else:
        print("No YouTube video URL found.")

if __name__ == "__main__":
    main()
