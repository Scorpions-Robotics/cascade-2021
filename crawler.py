from icrawler.builtin import BingImageCrawler

classes = input("Name: (Split by commas): ").split(",")
number = int(input("Amount: "))
path = input("Path: ")

for c in classes:
    bing_crawler = BingImageCrawler(
        storage={"root_dir": f'{path}/{c.replace(" ",".")}'}
    )
    bing_crawler.crawl(keyword=c, filters=None, max_num=number, offset=0)
