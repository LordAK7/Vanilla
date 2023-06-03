import webbrowser


def web_open(website):
    # Check if the website is a valid URL.
    if not website.startswith("http://") and not website.startswith("https://"):
        website = "http://" + website

        # Open the website in the default web browser.
        webbrowser.open(website)
