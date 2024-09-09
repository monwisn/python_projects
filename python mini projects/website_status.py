
# Simple website status checker that tell us whether a website is online and also going to give us back
# some basic information regarding the website, such as the response time
import requests
from requests import Response, RequestException
from requests.structures import CaseInsensitiveDict


# Function will return none because we'll only display information to the user.
def check_website_status(url: str) -> None | str:
    try:
        # # If neither 'https' nor 'http' is found, it will print 'test'.
        # if 'https' not in url and 'http' not in url:
        #     print('Your url should contain https or http protocol.')
        # else:
        response: Response = requests.get(url)

        # Information
        status_code: int = response.status_code
        # url: str = response.url
        headers: CaseInsensitiveDict[str] = response.headers

        # using case-insensitive dict we can use 'Content-Type' or 'content-type' and it's going to be treated the same
        content_type: str = headers.get('content-type', 'unknown')
        server: str = headers.get('server', 'unknown')
        response_time: float = response.elapsed.total_seconds()

        print(f'URL: {url}')
        print(f'Status Code: {status_code}')
        print(f'Content Type: {content_type}')
        print(f'Server: {server}')
        print(f'Response Time: {response_time:.2f} seconds')

    except RequestException as e:
        return f"Error: {e}"


def main():
    url_to_check: str = 'htt://www.udemy.com'
    # website_url = input("Enter the URL to check: ")
    check_website_status(url=url_to_check)


if __name__ == '__main__':
    main()

