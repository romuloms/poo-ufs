links = [
    "www.google.com",
    "www.youtube.com",
    "www.wikipedia.com"
]

# links = [x[4:] for x in links]
# print(links)

for link in links:
    print(link.removeprefix("www."))